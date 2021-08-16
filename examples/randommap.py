import time
import random
import beatsaver

while True:
    mapID = hex(random.randint(1, 0xffff))[2:]

    if beatsaver.maps.get_map_from_id(mapID) is None:
        time.sleep(5)
        continue
    else:
        input(f'Map {mapID} is your random ID.')