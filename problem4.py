# Import necessary libraries
import numpy as np

# Define the parameters
blocking_p = 2 / 100
lamda = 2
H = 3 / 60
Au = lamda * H

# System A
print('For system A')
channel_a = 19
cell_A = 394
A = 12
print('Number of users in System A')
Ua = A / Au
print(Ua)
print('Total number of subscribers in System A')
subscriber_A = Ua * cell_A
print(subscriber_A)
percentage_market_penetration_for_A = (subscriber_A / 2000000) * 100
print(percentage_market_penetration_for_A)

# System B
print('For system B')
channel_b = 57
cell_B = 98
Ab = 45
print('Number of users in System B')
Ub = Ab / Au
print(Ub)
print('Total number of subscribers in System B')
subscriber_B = Ub * cell_B
print(subscriber_B)
percentage_market_penetration_for_B = (subscriber_B / 2000000) * 100
print(percentage_market_penetration_for_B)

# System C
print('For system C')
channel_c = 100
cell_C = 49
Ac = 88
print('Number of users in System C')
Uc = Ac / Au
print(Uc)
print('Total number of subscribers in System C')
subscriber_C = Uc * cell_C
print(subscriber_C)
percentage_market_penetration_for_C = (subscriber_C / 2000000) * 100
print(percentage_market_penetration_for_C)

# Total number of subscribers and market penetration for all three systems
Total_number_of_subscriber = subscriber_A + subscriber_B + subscriber_C
Market_penetration_for_three_system = (Total_number_of_subscriber / 2000000) * 100
print('Total number of subscribers:', Total_number_of_subscriber)
print('Market penetration for the three systems:', Market_penetration_for_three_system)
