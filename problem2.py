import math

R_SI = 15
io = 6
n = [4, 3]

for a in range(2):
    N = 7
    Q = round(math.sqrt(3 * N), 2)
    print('n :', n[a])
    print('Frequency reuse factor:', Q)
    SI = round(10 * math.log10((1 / io) * (Q ** n[a])), 2)
    print('Signal to interference ratio:', SI)
    if R_SI < SI:
        print('N=' + str(N) + ' can be used')
    else:
        print('N=' + str(N) + ' cannot be used')
    if SI < R_SI:
        i = 2
        j = 2
        N = (i ** 2) + (i * j) + (j ** 2)
        Q = round(math.sqrt(3 * N), 2)
        print('n :', n[a])
        print('Frequency reuse factor:', Q)
        SI1 = round(10 * math.log10((1 / io) * (Q ** n[a])), 2)
        print('Signal to interference ratio:', SI1)
        print('N=' + str(N) + ' can be used')
