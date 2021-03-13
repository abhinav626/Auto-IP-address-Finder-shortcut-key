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


#keyboard.press(Key.alt)             #to maximise window
#keyboard.press(Key.space)
#keyboard.release(Key.space)
#keyboard.release(Key.alt)

#=======================================================================
#closing
#=======================================================================
time.sleep(5)
#keyboard.press(Key.enter)           #to run the command
#keyboard.release(Key.enter)

time.sleep(0.5)

keyboard.type('exit')
time.sleep(1)
keyboard.press(Key.enter)           #to run the command
keyboard.release(Key.enter)





























#{def on_press(key):
    
 #   try:
 #       k = key.name  # single-char keys
 #   except:
  #      k = key.char  # other keys
  #  if k in ['alt']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        #(unhash)print('Key pressed: ' + k)
        
       
       # return False  # stop listener; remove this if want more keys

#listener = keyboard.Listener(on_press=on_press)
#listener.start()  # start to listen on a separate thread
#listener.join()  # remove if main thread is polling self.keys










    
