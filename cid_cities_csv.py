import csv
from collections import defaultdict
filename = 'files/cid_cities.csv'

cities_list = defaultdict(list)

with open(filename) as f:
    reader = csv.reader(f)

    for num, row in enumerate(reader):
        if num % 2 == 0:
            code = row[0]
        else:
            cities_list[code] = row[0]

with open('files/cid.csv', 'w') as f:
    fieldnames = ['cid', 'city']
    writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    for cid, city in cities_list.items():
        writer.writerow({'cid': cid, 'city': city})
