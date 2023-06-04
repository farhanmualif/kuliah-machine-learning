import pandas as pd
import numpy as np


df = pd.read_csv('data_example_4_challenge.csv')

cek = 0
for row in df['Nama']:
    try :
        df['Nama'].isnull()
        int(row)
        df.loc[cek, 'Nama'] = np.nan
        ubah_nama =  df['Nama'].fillna("noname", inplace = True) 
    except ValueError:
        cek = cek + 1
        print(df, '\n')


# user = int(input("masukkan nilai"))
# ubah_Agama = df['MTK'].fillna(user, inplace = True)
# print(df, '\n')