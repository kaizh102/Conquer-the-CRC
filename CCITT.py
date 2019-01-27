def pword(crc):
    for j,b in zip(range(0,16), crc):
        if(j%4)==0:
            print(" ", end='')
        print("{:1d}".format(crc[j]), end='')

    print(" ", hexlify(crc.tobytes()))
#========================================

from binascii import *

msg = '1234567890'
msg = msg + '0000'

ply = "1021"

b_msg = unhexlify(msg)
b_ply = unhexlify(ply)

from bitarray import *

bit_msg = bitarray()
bit_ply = bitarray()
bit_msg.frombytes(b_msg)
bit_ply.frombytes(b_ply)

crc = bit_msg[1:17]
p = bit_msg[0] # poped bit
for i in range(17,len(bit_msg)):

    print("   | {:1d}".format(p), end = '')
    pword(crc)
    if p:
        crc ^= bit_ply
    p = crc[0]
    crc = crc[1:]
    crc.append(bit_msg[i])
print("   | {:1d}".format(p), end = '')
pword(crc)
if p:
    crc ^= bit_ply
print('final:', end = '')
pword(crc)


