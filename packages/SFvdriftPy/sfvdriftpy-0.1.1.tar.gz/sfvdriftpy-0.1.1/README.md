# SFvdriftPy

**SFvdriftPy** is a Python package for modeling equatorial vertical drift as a function of solar local time, longitude, day of the year, and solar flux.
This package models the vertical drift as described by [Scherliess and Fejer (1999)](https://doi.org/10.1029/1999JA900025). The fortran code that this model has been refactored from is attributed to the [sami2py](https://github.com/sami2py/sami2py) development team.

## Installation

To install the package from PyPI:

```bash
pip install SFvdriftPy
```

## Quick Start

### Importing SFvdriftPy

To begin, import the `vdrift_model` function, which is the main function for calculating vertical drifts:


```python
from SFvdriftPy import vdrift_model
```

### Example Usage

The **`vdrift_model`** function calculates the equatorial vertical drift for given parameters. 

#### Parameters:
- `xt` (float): Solar local time (hours, in 0-24 range).
- `xl` (float): Geographic longitude (degrees).
- `param` (list): A list of two elements, `[doy, f107]`:
  - `doy` (int): Day of the Year (DOY).
  - `f107` (float): Solar flux (F10.7 index).

#### Example Code

```python
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
```

## Functions Overview

### `vdrift_model`

The main function to calculate the equatorial vertical drift.

**Parameters**:
- `xt` (float): Solar local time (0-24 hours).
- `xl` (float): Geographic longitude in degrees.
- `param` (list): Contains `[DOY, F10.7]`, where `DOY` is the day of the year, and `F10.7` is the solar flux index.

**Returns**:
- `float`: The vertical drift in meters per second (m/s).

### `g`

The **seasonal and solar flux-dependent weighting function**, which adjusts for seasonal and flux conditions in the drift calculations.

**Parameters**:
- `param` (list): Contains `[DOY, F10.7]` for day of the year and solar flux.
- `xl` (float): Geographic longitude in degrees.

**Returns**:
- `np.array`: Array of function weights for seasonal and solar flux adjustments.

### `bspl4`

A **B-spline function** used to generate values for both time and longitude as part of the main model.

**Parameters**:
- `i` (int): Index for current spline interval.
- `x1` (float): The input value (e.g., SLT or longitude) for the spline calculation.
- `t_knots` (np.array): Knot points array for B-spline intervals.

**Returns**:
- `float`: B-spline interpolated value for the input.

## Plotting Example

Here’s how to plot the vertical drift across a range of solar local times for a fixed day of the year and solar flux:

```python
import matplotlib.pyplot as plt
import numpy as np
from SFvdriftPy import vdrift_model

# Define parameters
xl = 150.0  # Geographic longitude in degrees
doy = 100  # Day of the year
f107 = 150  # Solar flux
slt_range = np.linspace(0, 24, 100)  # Solar local time range

# Calculate vertical drifts
drifts = [vdrift_model(slt, xl, [doy, f107]) for slt in slt_range]

# Plot the result
plt.figure(figsize=(10, 5))
plt.plot(slt_range, drifts)
plt.xlabel('Solar Local Time (hours)')
plt.ylabel('Vertical Drift (m/s)')
plt.title(f'Equatorial Vertical Drift on DOY={doy} for F10.7={f107}')
plt.grid(True)
plt.show()
```

## References

Part of this work uses the SAMI2 ionosphere model originally written and developed by the Naval Research Laboratory.
 When referring to this package, please additionally cite the following sources:

	•	Scherliess, L., & Fejer, B. G. (1999). “Radar and satellite global equatorial F region vertical drift model.” Journal of Geophysical Research: Space Physics, 104(A4), 6829–6842. https://doi.org/10.1029/1998JA900062
	•	Huba, J. D., Joyce, G., & Krall, J. (2000). “SAMI2 (SAMI2 is Another Model of the Ionosphere): A new low-latitude ionosphere model.” Journal of Geophysical Research: Space Physics, 105(A10), 23035-23053. https://doi.org/10.1029/2000JA000035
	•	Klenzing, J., Stoneback, R., Sanny, J., Lingerfelt, E., & Heelis, R. (2019). “sami2py: A Python implementation of the SAMI2 model.” https://doi.org/10.5281/zenodo.2875800.


## License

This project is licensed under the MIT License.