import numpy as np

# Define the parameters
c = 3 * 10**8  # Speed of light in m/s
f = 900 * 10**6  # Frequency in Hz
D = 1  # Distance in meters

# Calculate wavelength
lamda = c / f

# Calculate Fraunhofer distance
df = 2 * (D**2) / lamda
print("Fraunhofer distance = ")
print(df)

# Calculate Path Loss
PL = -10 * np.log10((lamda**2) / (((4 * np.pi)**2) * (df**2)))
print("Path Loss = ")
print(PL)
