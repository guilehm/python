import csv
import operator
from collections import Counter

filename = 'files/oco.csv'


reader = csv.DictReader(open(filename))

fields = reader.fieldnames
print(fields)

codes = []
ocurrencies_type = []

for row in reader:
    codes.append(row['codigo_ocorrencia'])
    ocurrencies_type.append(row['ocorrencia_tipo'])

codes_counter = dict(Counter(codes))
ocurrencies_type_counter = dict(Counter(ocurrencies_type))

otc = ocurrencies_type_counter
sorted_otc_by_value = sorted(otc.items(), key=lambda kv: kv[1])

print(sorted_otc_by_value)
