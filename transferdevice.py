import sys
import os

stdin = os.fdopen(sys.stdin.fileno(), 'rb')
stdout = os.fdopen(sys.stdout.fileno(), 'wb')

done = False
signalbus = [0x00, 0x00]

i = 0

bufReg = 0x00

if i < len(sys.argv[1]):
    bufReg = str.encode(sys.argv[1][i])[0]
    i = 1

while not done:
    signalbus = bytearray(stdin.read(2))
    if signalbus[0]&0x80 > 0:
        done = True
    elif signalbus[0]&0x03 == 0x03: #Is this message addressed to me
        if signalbus[1] == 0x00: # Fetch
            signalbus = [0x00, bufReg]
            stdout.write(bytes(signalbus))
            stdout.flush()
            if i < len(sys.argv[1]):
                bufReg = str.encode(sys.argv[1][i])[0]
            else:
                bufReg = 0x00
            i=i+1
        elif signalbus[1] == 0x01: #Reset
            i=0
