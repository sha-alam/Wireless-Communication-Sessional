import numpy as np

Gos = 0.5 / 100
Au = 0.1
A = np.array([0.005, 1.13, 3.96, 11.1, 80.9])
c = np.array([1, 5, 10, 20, 100])

print('Blocking probability =', Gos)
print('Traffic intensity per user =', Au)
print('Traffic intensity', A)
print('Channel', c)

U = np.ceil(A / Au)
print('Number of users')
print(U)
