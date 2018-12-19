import csv
from matplotlib import pyplot as plt

filename = 'Overwatch_edopic.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dps_car = []
    for row in reader:
        try:
            dps = int(row[1])
            dps_car.append(dps)
        except ValueError:
            dps = 0
            dps_car.append(dps)

    print(dps_car)

    char_nme = []

    for index, column_header in enumerate(header_row):
        print(index, column_header)

fig = plt.figure(dpi=128, figsize=(10, 6))
print(len(char_nme))
print(len(dps_car))
plt.plot(dps_car, c='red')
plt.title("Overwatch Deaths Per Second", fontsize=24)
plt.xlabel('Hero Names', fontsize=16)
plt.ylabel("DPS", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
