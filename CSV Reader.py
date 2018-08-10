import csv

filename = "files/sitka_weather_07-2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    akdt, max_temp, mean_temp, min_temp, max_wind_speed = [], [], [], [], []
    for num, row in enumerate(reader):
        akdt.append(row[0])
        max_temp.append(row[1])
        mean_temp.append(row[2])
        min_temp.append(row[3])
        try:
            max_wind_speed.append(int(row[16]))
            print("{number:3} adicionado à lista.".format(number=int(row[16])))
        except ValueError:
            print(
                'Valor inválido para linha {num}. Foi adicionado "{row}" à lista.'.format(
                    num=num, row=row[16]
                )
            )
            max_wind_speed.append(row[16])
