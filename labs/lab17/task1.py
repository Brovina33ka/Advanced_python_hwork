import numpy as np
import pandas as pd

N,M = map(int, input().split())
data = []
for i in range(N):
    data.append(list(map(int, input().split())))
df1 = pd.DataFrame(data)
print(np.sum((df1 < -5).sum(axis=1)), 'площадь клеточек, глубина больше меньше 5')
print(int(abs(np.sum(df1[(df1 < 0)].sum()))), 'объем суши')
print(int(max(df1[(df1 > 0)].max())), 'максимум высоты над уровнем моря')

