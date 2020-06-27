import sys
import os

stdin = os.fdopen(sys.stdin.fileno(), 'rb')
stdout = os.fdopen(sys.stdout.fileno(), 'wb')

done = False
#message = [0x00, 0x00]

i = 0

bufReg = 0x00

if i < len(sys.argv[1]):
    bufReg = str.encode(sys.argv[1][i])[0]
    i = 1

while not done:
    message = bytearray(stdin.read(2))
    if message[0]&0x80 > 0:
        done = True
    elif message[0]&0x03 == 0x03: #Is this message addressed to me
        if message[1] == 0x00: # Fetch
            message = [0x00, bufReg]
            stdout.write(bytes(message))
            stdout.flush()
            if i < len(sys.argv[1]):
                bufReg = str.encode(sys.argv[1][i])[0]
            else:
                bufReg = 0x00
            i=i+1
        elif message[1] == 0x01: #Reset
            i=0
