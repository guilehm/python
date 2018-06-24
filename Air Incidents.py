import csv

from collections import Counter

filename = 'files/oco.csv'


reader = csv.DictReader(open(filename))

fields = reader.fieldnames
codes = []

for row in reader:
    codes.append(row['codigo_ocorrencia'])

codes_counter = dict(Counter(codes))
print(codes_counter)

