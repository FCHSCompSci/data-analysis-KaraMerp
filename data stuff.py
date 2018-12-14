import csv
from matplotlib import pyplot as plt

filename = 'Overwatch_edopic.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    Heroes = []
    for row in reader:
        Heroes.append(row[0])
    print(Heroes)

    DPS = []
    for row in reader:
        DPS.append(row[1])
    print(DPS)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(DPS, c='red')

plt.title("Overwatch Hero Deaths Per Second", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("DPS", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

#python crash course pg 353