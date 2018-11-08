import array


# List Comprehension
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

# Generators Expressions - tuples
tuple(ord(symbol) for symbol in symbols)
array.array('I', (ord(symbol) for symbol in symbols))

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

# Unpacking
t = (20, 8)
quotient, remainder = divmod(*t)
a, b, *rest = range(5)
print(a, b, rest)
a, b, *body, d, e = range(10)
print(a, b, body, d, e)


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9} |'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f} |'
for name, cc, pop, (latitude, longitude) in metro_areas:
    # if longitude <= 0:
    print(fmt.format(name, latitude, longitude))
