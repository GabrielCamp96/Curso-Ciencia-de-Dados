import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')

print(base.shape)

# np.random.seed(2345)
amostra = np.random.choice(a = [0, 1], size = 50, replace = True, p = [0.5, 0.5])

print(len(amostra))
print(len(amostra[amostra == 1]))
print(len(amostra[amostra == 0]))
base_final = base.loc[amostra]
print(base_final)