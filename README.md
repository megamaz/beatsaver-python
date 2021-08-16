# Python BeatSaver API
This is the python API for communicating with BeatSaver.\
Installation:\
```
python -m pip install ??????
```

# Samples
### Getting map from ID
```py
>>> import beatsaver as bs # easier to type really
>>> hardestmap = bs.maps.get_map_from_id('25f')
>>> hardestmap.name
'DM DOKURO - Reality Check Through The Skull'
>>> hardestmap.uploader.name
'rickput'
>>> # maps that don't exist return None
>>> doesnotexist = bs.maps.get_map_from_id('z')
>>> doesnotexist is None
True
```
### Bonus
```py
>>> import beatsaver as bs
>>> rcttc = bs.maps.get_map_from_id('25f')
>>> class smth:
...     def __eq__(self, a):
...         return True
...
>>> bad = smth()
>>> rcttc == bad
True
```