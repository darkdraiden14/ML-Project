import numpy as np


for low in range(100,125):
    high= low +80
    arr=np.arange(low,high,5).reshape(8,2)
    print()
    print(arr)
