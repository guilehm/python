import csv

filename = 'files/oco.csv'


reader = csv.DictReader(open(filename))

fields = reader.fieldnames
codes = []

for row in reader:
    codes.append(row['codigo_ocorrencia'])

print(len(codes))

