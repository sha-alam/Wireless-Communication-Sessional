# Define the parameters
c = 3 * 10**8  # Speed of light in m/s
f = 900 * 10**6  # Frequency in Hz

# Calculate wavelength
lamda = c / f

# Calculate vehicle speed in m/s
vehicle_speed = 70 * (1000 / (60 * 60))

print('(A)')
print("The Vehicle is moving directly toward the transmitter")
The_received_frequency_of_A_is = int(f + (vehicle_speed / lamda))
print(f"The received frequency of A is: {The_received_frequency_of_A_is} Hz")

print('(B)')
print("The Vehicle is moving directly away from the transmitter")
The_received_frequency_of_B_is = int(f - (vehicle_speed / lamda))
print(f"The received frequency of B is: {The_received_frequency_of_B_is} Hz")

print('(C)')
print("The Vehicle is moving perpendicular to the angle of arrival of the transmitted signal")
print("The received signal frequency is the same as the transmitted frequency 900MHz")
