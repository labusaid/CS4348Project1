byteBuffer = bytearray(128) # simulated RAM

def access(mode, index, toWrite=None):
    if mode == 'read':
        print(byteBuffer[index])
    elif mode == 'write':
        byteBuffer[index] = toWrite

# Test Code
access('read', 0)
access('write', 0, 7)
access('read', 0)