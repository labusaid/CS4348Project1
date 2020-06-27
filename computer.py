#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

dev = Popen(['python', 'device.py', sys.argv[1]], stdout=PIPE, stdin=PIPE, bufsize=-1)

reset = [0x03,0x01] # Reset Command
fetch = [0x03,0x00] # Fetch Command

done = False

while not done:
    dev.stdin.write(bytes(fetch))
    dev.stdin.flush()
    reply = bytearray(dev.stdout.read(2))
    if reply[1] == 0x00:
        done = True
    else:
        sys.stdout.write(bytearray([reply[1]]).decode())


# Tell device process to exit
fetch[0] = 0x80
dev.stdin.write(bytes(fetch))
dev.stdin.flush()

# Wait for device process to exit
dev.wait()
