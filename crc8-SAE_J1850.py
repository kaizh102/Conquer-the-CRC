def crc8_SAE_J1850(data:bytearray):
    '''
    poly = 0x1D, Initial = 0xFF, Final Xor = 0xFF, no reflection
    '''
    poly = 0x1D
    crc = 0xFF

    for byte in data:
        #print("current byte: ", hex(byte))
        crc ^= byte
        #print(hex(crc))
        for _ in range(0,8):
            if (crc & 0x80):
                crc = (crc << 1) ^ poly
                crc &= 0xFF
                #print("--", hex(crc))
            else:
                crc <<= 1
                crc &= 0xFF
                #print("oo", hex(crc))
     
    return crc^0xFF

input = "20 20 00 00 70 04 00 "
input = input.replace(" ", "")

content = input
data = bytearray.fromhex(content)
print(hex(crc8_SAE_J1850(data))
