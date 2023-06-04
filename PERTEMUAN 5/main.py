import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np


df = pd.read_csv('data_scala copy.csv')

scal = MinMaxScaler()


# params = df.loc[0:2, 'nilai'].reshape(-1,1)
# params = np.array(df['nilai']).reshape(-1,1)
# params = df.iloc[:,:-1].values
# min_max = df['nilai'] = scal.fit_transform(params)

# df.iloc[:0,:-1] = scal.fit_transform(df['nilai'])
# print(min_max)
# print(df['nilai'])


# challenge
# df.iloc[:0,:-1] = scal.fit_transform(df[0:2,'nilai'])
# min_max = df['nilai'] = scal.fit_transform(params)

scaler = MinMaxScaler()
min_max = df[['nilai']] = scaler.fit_transform(df[['nilai']])
print(df)
print(min_max)
