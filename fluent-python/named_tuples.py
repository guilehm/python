from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo.population)
print(tokyo.coordinates)
print()

LatLong = namedtuple('LatLong', 'lat long')
tokyo = City('Tokyo', 'JP', 36.933, LatLong(35.689722, 139.691667))

print(tokyo.coordinates)
print(tokyo.coordinates.lat)
print(tokyo.coordinates.long)
print()
print(tokyo._fields)
print(tokyo._asdict())
