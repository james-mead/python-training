"""Example of date and time."""

import numpy as np
temperature = [12, 13, 28, 36, 19, 21, 50, 54, 65]

print(min(temperature))
print(max(temperature))
print(np.mean(temperature))
print(np.median(temperature))
print(np.percentile(temperature, 75))
