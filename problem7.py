# Import necessary library
import numpy as np

# (A)
print('(A)')
Tn = 150  # in microseconds
N = 70
delT = Tn / N
print(f'delT = {delT} us')

# (B)
print('(B)')
Tn = 4  # in microseconds
MBW = 2 / delT
print(f'The maximum Bandwidth that the SMRCIM model can accurately represent = {MBW} MHz')

delT = (Tn / N) * 1000  # convert to nanoseconds
print(f'delT for SMRCIM urban microcell model is {delT} ns')

RFBW = (2 / delT) * 1000  # convert to MHz
print(f'The maximum RF bandwidth that can be represented is {RFBW} MHz')

# (C)
print('(C)')
Exdel = 500  # in nanoseconds
delT = Exdel / N
print(f'For indoor channel {delT} ns')

RFBW = (2 / delT) * 1000  # convert to MHz
print(f'The maximum RF bandwidth for the indoor channel model is {RFBW} MHz')
