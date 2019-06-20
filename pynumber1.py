#!/usr/bin/python3

import numpy as np

print("Enter Dimensions:")
r=int(input("Row:"))
c=int(input("Column:"))

arr = np.random.randint(low=1,high=10,size=(r,c))
print(arr)

with open("pynumfile.txt","w") as f:
    f.write(str(arr))
