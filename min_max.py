import numpy as np

a = np.random.randn(100)
# a = [3,1,5,9,5,4,434,23,1,354]
min = 9999999**4
max = 0.9999999999999999**4


split = 2
N = len(a)
for i in range(N-1):
    pair = a[i:split+i]
    for ix in pair:
        if ix>max:
            
            max = ix
        elif ix<min:
            
            min = ix


print("min",min)
print("max",max)