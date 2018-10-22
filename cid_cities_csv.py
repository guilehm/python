import csv
import json
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


with open('files/cid.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    my_dict = {rows[0]: rows[1] for rows in reader}

    with open('files/cid.json', 'w') as outfile:
        json.dump(my_dict, outfile)
