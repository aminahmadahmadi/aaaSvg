import geojson
from pyproj import Proj, transform

with open('D:\\KND\\svg\\N26E053.json') as f:
    gj = geojson.load(f)

features = gj['features']
for feature in features:
    cordinates = feature['geometry']['coordinates']

    for cordinate in cordinates:
        print(cordinate)
        _lat = cordinate[1]
        _lon = cordinate[0]
        print(transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'),  _lon, _lat))  # longitude first, latitude second.
    
    print('---------------------------------------')