import numpy as np


path_A = input()
path_b = input()
X = np.array(list(map(float, input().split())))

with open(path_A) as f:
    A = np.array([list(map(float, row.split())) for row in f.readlines()])
    
with open(path_b) as f1:
    b = np.array(list(map(float, f1.read().split())))

A2 = A.dot(A)
r3 = A2.dot(X)
r3 = r3.dot(b)
print(r3)

