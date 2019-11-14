# James Park
# Prof. Kounavelis
# Lab 8 matplotlib pie chart

import matplotlib.pyplot as plt
from sys import argv

# Get file
inFile = open(argv[1], "r")
# Setup parts
labels = 'Rent', 'Gas', 'Food', 'Clothing', 'Car payment', 'Misc'
sizes = []
# Feed in data
for x in inFile:
    sizes.append(x)
# Setup and show pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')

plt.show()
