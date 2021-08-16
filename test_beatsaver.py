import beatsaver

def test_getMapFromID():
    doesNotExist = beatsaver.maps.get_map_from_id('99999') # map does not exist
    assert doesNotExist == None
    machinegun = beatsaver.maps.get_map_from_id('9e5c')
    assert machinegun.uploader.name == 'de125'
    
def test_getMapFromHash():
    ov = "f402008042efaca4291a6633ebb6b562e4adcd87" # this is the ov hash lol
    sacrament = beatsaver.maps.get_map_from_hash(ov)
    assert sacrament.uploader.name == "rogdude"

def test_getMapsFromUser():
    user = beatsaver.extras.get_user_from_username('megamaz')
    megamaps = beatsaver.maps.get_maps_from_user(user.id)
    assert megamaps != None

def test_getLatestMaps():
    latest = beatsaver.maps.get_latest_maps(False)
    assert latest != None

def test_getMostPlayedMaps():
    mostplayed = beatsaver.maps.get_most_played_maps()
    assert mostplayed != None

def test_getUserFromUsername():
    user = beatsaver.extras.get_user_from_username('megamaz')
    assert user.name == 'megamaz'