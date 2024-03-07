import beatsaver
import pytest

# beatsaver.maps
def test_getMapFromID():
    # test expected result
    with pytest.raises(beatsaver.models.exceptions.BeatSaverNotFoundException):
        beatsaver.maps.get_map_from_id('z') # map does not exist
    
    machinegun = beatsaver.maps.get_map_from_id('9e5c')
    
def test_getMapFromHash():
    ov = "f402008042efaca4291a6633ebb6b562e4adcd87" # this is the ov hash lol
    beatsaver.maps.get_map_from_hash(ov)
    with pytest.raises(beatsaver.models.exceptions.BeatSaverNotFoundException):
        beatsaver.maps.get_map_from_hash("not a hash that would work ever")

def test_getMapsFromUser():
    beatsaver.maps.get_maps_from_user(4286427)
    with pytest.raises(beatsaver.models.exceptions.BeatSaverNotFoundException):
        beatsaver.maps.get_maps_from_user(2**30) # this aint gonna happen for a while

def test_getLatestMaps():
    beatsaver.maps.get_latest_maps(automapper=False)

def test_getMostPlayedMaps():
    beatsaver.maps.get_maps_by_plays()

# users
def test_getUserInfo():
    beatsaver.users.get_user_info(4286427)
    with pytest.raises(beatsaver.models.exceptions.BeatSaverNotFoundException):
        beatsaver.users.get_user_info(2**30)
    
    assert len(beatsaver.users.get_users_info(4286427, 4285227)) == 2

def test_getUserFromUsername():
    beatsaver.users.get_user_info_by_name('megamaz')
    with pytest.raises(beatsaver.models.exceptions.BeatSaverNotFoundException):
        beatsaver.users.get_user_info_by_name("kdhfgjkadhfljahsdjkf absjkfvajkvrhewuvryauewtrywtgbkjcwm,hbduOBKLASY AKSJDF") # it's hard to come up with a non-existing user...



if __name__ == "__main__":
    # for debugging purposes.
    test_getUserFromUsername()