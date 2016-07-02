import time
import signal
import sys
from h_swapi import SWAPI

start_time = time.time()

my_api = SWAPI("star_wars.db")

def signal_handler(signal, frame):
        print("Cancel!")
        my_api.stop()
        print time.time() - start_time
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

my_api.start()
while not my_api.is_done():
    pass

signal.pause()
