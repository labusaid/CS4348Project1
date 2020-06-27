import sys
import time

inputBuffer = bytearray(1)

inputFile = open(sys.argv[1])

while True:
    # gets control character
    controlMode = inputFile.read(1)

    # exits if end of file is reached
    if controlMode == '':
        exit()

    # read a line in
    if controlMode == 't':
        print(inputFile.readline())
        # TODO: make this work
    # set buffer to newline
    elif controlMode == 'n':
        print('newline read')
        inputBuffer[0] = 10 # ASCII for \n
    # delay for read int milliseconds
    elif controlMode == 'd':
        print('sleeping')
        time.sleep(int(inputFile.readline())/1000)

    # stalls until buffer is emptied to continue
    while inputBuffer[0] != 0:
        time.sleep(.001)