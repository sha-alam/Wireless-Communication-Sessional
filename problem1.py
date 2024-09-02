bw = 30000
schannel_bw = 25

print('Channel Bandwidth  :')
dup_ch_bw = 2 * schannel_bw
t_ch = bw / dup_ch_bw
print(dup_ch_bw)
print('Total available channel :')
print(t_ch)

cc_bw = 1000
t_cc = cc_bw / dup_ch_bw
print('Total control channel  :')
print(t_cc)

N = [4, 7, 12]
for i in range(3):
    ch = t_ch / N[i]
    ch_per_cell = int(ch)
    print('Channel per cell :')
    print(N[i])
    print(ch_per_cell)
    c = t_cc / N[i]
    cc = round(c)
    v = ch_per_cell - cc
    vc = round(v)
    print('Control channel and voice channel are :')
    print(cc)
    print(vc)