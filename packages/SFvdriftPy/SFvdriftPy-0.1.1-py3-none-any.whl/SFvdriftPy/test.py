import numpy as np
from SFvdriftPy import vdrift_model

# Example input parameters
xt = 12.0  # Solar local time (hours)
xl = 150.0  # Geographic longitude (degrees)
doy = 100  # Day of the year (e.g., April 10th)
f107 = 150  # Solar flux (F10.7 index)

# Calculate vertical drift
param = [doy, f107]
vertical_drift = vdrift_model(xt, xl, param)

print(f"Vertical drift at SLT={xt}, longitude={xl}, DOY={doy}, F10.7={f107} is {vertical_drift:.2f} m/s")