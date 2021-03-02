import numpy as np
import pandas as pd

path_to_file = '/Users/Ksenia/Desktop/cmder/games001.csv'
G = pd.read_csv(path_to_file, sep=';')
path_to_file1 = '/Users/Ksenia/Desktop/cmder/rates001.csv'
R = pd.read_csv(path_to_file1, sep=';')

RATES = []
for i in range(len(list(G.iterrows()))):
    RATES.append(R[R['id'] == (i+1)]['mark'].mean())
    
G['mean'] = RATES
G.head()
G1 = G.sort_values(by='mean', ascending=False).head(3)

for i in G1.iterrows():
    print(G['name'].iloc[i[0]], round(G['mean'].iloc[i[0]], 3))
    
G2 = G[G['mean'] > 8.0]   #таблица с играми рейтингом выше 8.0
G3 = pd.DataFrame(G2.groupby('company')['name'].count()) 
G3 = G3.sort_values(by='name', ascending=False)
print(G3.index[0],G3['name'][0])

