#!/usr/bin/python3

import numpy as np

f=open("file.txt","w")
a=np.random.random((3,2))
b=np.random.random((5,2))

f.write("matrix a:\n")
f.write(str(a))
f.write("\n")
f.write("matrix b:\n")
f.write(str(b))
