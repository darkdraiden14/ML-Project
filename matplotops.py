#!/usr/bin/python3

import matplotlib.pyplot as plt
#Only Importing pyplot(python oriented) from matplotlb

x=[2,3]
y=[9,5]
x1=[4,3,8]
y1=[2,9,7]
plt.xlabel("time")
plt.ylabel("speed")
plt.bar(x,y,label="water") # this will generate a straight line
plt.bar(x1,y1,label="sand")
plt.grid(color="green") # to form grid in graph
plt.legend()# to show label with plot
plt.xlim(0,12) # to show min and max number in x axis
plt.ylim(0,15) # y axis
plt.show()

