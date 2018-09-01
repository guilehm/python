import numpy as np
import pandas as pd

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'. split())
print(df)

print(df[['W', 'Z']])

df['new'] = df['W'] + df['X']
print(df)

print(df.loc['A', 'X'])

print(df.loc['A'])
