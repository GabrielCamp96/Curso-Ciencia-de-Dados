import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
# np.random.seed() define uma seed para gerar números aleatórios

amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])
amostra = list(amostra)

newbase = pd.DataFrame(data=base)

for i in amostra:
    if i==0:
        newbase.drop(newbase.index[amostra.index(i)], inplace=True)
newbase.to_csv('newiris.csv')