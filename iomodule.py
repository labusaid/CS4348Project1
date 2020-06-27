import time

inputBuffer = bytearray(1)

inputFile = open('os_in.txt')

controlMode = None

while True:
    # TODO: make program wait for buffer to be cleared
    controlMode = inputFile.read(1) # read a line in
    if controlMode == 't':
        print(inputFile.readline())
        # TODO: make this work
    elif controlMode == 'n': # set buffer to newline
        print('newline read')
        inputBuffer[0] = 10 # ASCII for \n
    elif controlMode == 'd': # delay for read int milliseconds
        print('sleeping')
        time.sleep(int(inputFile.readline())/1000)