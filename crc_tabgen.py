
PLY = 0x1021
CRC = 0
print('crc_tbl=[', end='')
for i in range(0x0,0x100):
    ply = PLY
    crc = (i<<8) & 0xFFFF
    for j in range(0,8):
        if crc & 0x8000:
            crc = (crc<<1) & 0xFFFF
            crc ^= ply
        else:
            crc = (crc<<1) & 0xFFFF

    print('0x{:04X}'.format(crc), end='')
    if i != 0xFF:
        print(', ', end='')
    else:
        print(']')
    if (i%16)==15:
        print('\n         ', end='')
