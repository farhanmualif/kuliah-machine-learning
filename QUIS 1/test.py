import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np

df = pd.read_csv("soal.csv")

def numIsMissingValue():
    count = 0
    for i in df['jumlah_barang']:
        try: 
          df['jumlah_barang'].isnull()
          int(i)
          df.loc[count,'jumlah_barang'] = np.nan
        except:
          pass
        count += 1
    print(df)

def minmax():
   scal = MinMaxScaler()
   df[['jumlah_barang']] = scal.fit_transform(df[['jumlah_barang']])
   print(df)

# mengubah non numerik menjadi numerik
def toNumber():
   le = LabelEncoder()
   for i in df.columns.values:
      if df[i].dtypes == 'object':
         data = df[i].append(df[i])
         le.fit(data.values)
         df[i] = le.transform(df[i])
   print(df)


toNumber()