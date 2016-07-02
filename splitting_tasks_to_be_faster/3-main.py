import time
from h_swapi import SWAPI

start_time = time.time()

my_api = SWAPI("star_wars.db")
my_api.start()
while not my_api.is_done():
    pass

print time.time() - start_time
