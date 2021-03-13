import time
from pynput.mouse import Button,Controller
mouse=Controller()
from pynput.keyboard import Key, Controller
keyboard= Controller()

#keyboard.press(Key.alt)             #to minimise window
#keyboard.press(Key.space)
#keyboard.release(Key.space)
#keyboard.release(Key.alt)
#time.sleep(0.1)
#keyboard.press('n')
#keyboard.release('n')
#time.sleep(0.1)

keyboard.press(Key.cmd)             #open run
keyboard.press('r')
keyboard.release('r')
keyboard.release(Key.cmd)

time.sleep(0.25)

keyboard.type('cmd')                #entering cmd in run

time.sleep(0.5)

keyboard.press(Key.enter)           #to open cmd
keyboard.release(Key.enter)

time.sleep(1)

keyboard.type('ipconfig')           #entering IPCONFIG

keyboard.press(Key.enter)           #to run the command
keyboard.release(Key.enter)



#=======================================================================
#closing
#=======================================================================
time.sleep(5)
#keyboard.press(Key.enter)           #to run the command UNHASH IF CLOSING DOSENT WORK
#keyboard.release(Key.enter)

time.sleep(0.5)

keyboard.type('exit')
time.sleep(1)
keyboard.press(Key.enter)           #to run the command
keyboard.release(Key.enter)



