import numpy as np

# Load coefficients from package data
def load_coefficients():
    coeff1 = np.genfromtxt('data/coeff1.txt', delimiter=',', invalid_raise=False)
    coeff2 = np.genfromtxt('data/coeff2.txt', delimiter=',', invalid_raise=False)
    return np.concatenate((coeff1, coeff2))

# Initialize global coefficients
coeff = load_coefficients()

# Generalized B-spline function to calculate values for both time and longitude
def bspl4(i, x1, t_knots):
    order = 4  # cubic b-spline (order 4 means degree 3)

    # Wrap around if x1 is smaller than the current knot
    x = x1 if x1 >= t_knots[i] else x1 + (24 if max(t_knots) < 25 else 360)

    # Initialize B-spline coefficient matrix
    b = np.zeros((20, 20))

    # Initial B-spline values
    for j in range(i, i + order):
        if t_knots[j] <= x < t_knots[j + 1]:
            b[j, 0] = 1.0

    # Recursively compute higher-order B-spline values using de Boor's algorithm
    for j in range(1, order):
        for k in range(i, i + order - j):
            delta_1 = (t_knots[k + j] - t_knots[k])
            if delta_1 != 0:
                b[k, j] = (x - t_knots[k]) / delta_1 * b[k, j - 1]

            delta_2 = (t_knots[k + j + 1] - t_knots[k + 1])
            if delta_2 != 0:
                b[k, j] += (t_knots[k + j + 1] - x) / delta_2 * b[k + 1, j - 1]

    return b[i, order - 1]


# Function to calculate seasonal and solar flux-dependent function values (funct)
def g(param, xl):
    flux = np.clip(param[1], 75, 230)
    cflux = flux
    a = 0

    # Setting `a` and `sigma` based on DOY ranges
    if 120 <= param[0] <= 240:
        a = 170.0
        sigma = 60.0
    elif param[0] <= 60 or param[0] >= 300:
        a = 170.0
        sigma = 40.0

    # Applying Gaussian smoothing to flux if flux is low (<= 95) and a is set
    if flux <= 95 and a != 0:
        gauss = np.exp(-0.5 * ((xl - a) ** 2) / (sigma ** 2))
        cflux = gauss * 95 + (1 - gauss) * flux

    funct = np.zeros(6)

    # Seasonal function values
    # check if doy falls within
    if 135 <= param[0] <= 230:
        funct[0] = 1
    if param[0] <= 45 or param[0] >= 320:
        funct[1] = 1
    if 75 < param[0] < 105 or 260 < param[0] < 290:
        funct[2] = 1

    # Transitions
    if 45 <= param[0] <= 75:
        funct[1] = 1 - (param[0] - 45) / 30
        funct[2] = 1 - funct[1]
    elif 105 <= param[0] <= 135:
        funct[2] = 1 - (param[0] - 105) / 30
        funct[0] = 1 - funct[2]
    elif 230 <= param[0] <= 260:
        funct[0] = 1 - (param[0] - 230) / 30
        funct[2] = 1 - funct[0]
    elif 290 <= param[0] <= 320:
        funct[2] = 1 - (param[0] - 290) / 30
        funct[1] = 1 - funct[2]

    # Flux adjustments
    funct[3] = (cflux - 140) * funct[0]
    funct[4] = (cflux - 140) * funct[1]
    funct[5] = (flux - 140) * funct[2]

    return funct


# Main function to calculate equatorial vertical drift (the model)
def vdrift_model(xt, xl, param):
    # Wrap around solar local time (ensure it's in the 0-24 hour range)
    xt = xt % 24

    # Get function values based on season and solar flux (using g function)
    funct = g(param, xl)

    # Initialize the drift value to zero
    y = 0.0

    # Knot points for time and longitude
    t_t = np.array([0.00, 2.75, 4.75, 5.50, 6.25, 7.25, 10.00, 14.00, 17.25,
                    18.00, 18.75, 19.75, 21.00, 24.00, 26.75, 28.75, 29.50,
                    30.25, 31.25, 34.00, 38.00, 41.25, 42.00, 42.75, 43.75,
                    45.00, 48.00, 50.75, 52.75, 53.50, 54.25, 55.25, 58.00,
                    62.00, 65.25, 66.00, 66.75, 67.75, 69.00, 72.00])
    t_l = np.array([0, 10, 100, 190, 200, 250, 280, 310, 360, 370, 460, 550,
                    560, 610, 640, 670, 720, 730, 820, 910, 920, 970, 1000,
                    1030, 1080])

    # Loop over local time index (13 splines for local time)
    for i in range(13):
        # Loop over longitude index (8 splines for longitude)
        for il in range(8):
            kk = 8 * i + il  # Calculate index for current position
            # Loop over season/flux indices (6 spline functions for these)
            for j in range(6):
                ind = 6 * kk + j  # Index into the coefficients array
                # Calculate the b-spline values for time and longitude
                bspl_time = bspl4(i, xt, t_t)
                bspl_long = bspl4(il, xl, t_l)
                bspl_result = bspl_time * bspl_long
                # Sum up the contribution of the current b-spline and function values
                y += bspl_result * funct[j] * coeff[ind]

    return y