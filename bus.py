import sys
import atexit

from subprocess import Popen, PIPE

def exit_handler():
    print('exiting')
    # Kill off processes
    iomod.kill()
    buff.kill()
    transf.kill()
    print('exited')

atexit.register(exit_handler)

# Spawns iomodule with inputFile
buff = Popen(['python3', 'buffer.py'], stdout=PIPE, stdin=PIPE, bufsize=-1)
iomod = Popen(['python3', 'iomodule.py', sys.argv[1]], stdout=PIPE, stdin=PIPE, bufsize=-1)
transf = Popen(['python3', 'transferdevice.py'], stdout=PIPE, stdin=PIPE, bufsize=-1)

while True:
    pass