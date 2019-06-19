#!/usr/bin/python3

import matplotlib.pyplot as plt
#Only Importing pyplot(python oriented) from matplotlb
runs =[150,160,105]
players=["virat","dhoni","pandya"]
plt.xlabel("players")
plt.ylabel("runs")
plt.bar(players,runs,label="water") # this will generate a straight lines
plt.grid(color="green") # to form grid in graph
plt.legend()# to show label with plot
plt.xlim(0,12) # to show min and max number in x axis
plt.show()

