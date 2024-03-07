# Python BeatSaver API
This is the unofficial python API for communicating with BeatSaver.\
Installation:
```
python -m pip install beatsaver
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
>>> # maps that don't exist raise BeatSaverNotFoundException
>>> try:
...     doesnotexist = bs.maps.get_map_from_id('z')
... except bs.models.exceptions.BeatSaverNotFoundException:
...     print("oops")
...
oops
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