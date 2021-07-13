import geojson
from pyproj import Transformer

with open('D:\\KND\\svg\\N26E053.json') as f:
    gj = geojson.load(f)

features = gj['features']
for feature in features:
    cordinates = feature['geometry']['coordinates']

    for cordinate in cordinates:
        print(cordinate)
        _lat = cordinate[1]
        _lon = cordinate[0]
        transformer = Transformer.from_crs("epsg:4326", "epsg:3857")
        x,y = transformer.transform( _lon, _lat)
        print(x,y)
    
    print('---------------------------------------')