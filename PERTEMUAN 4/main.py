import pandas as pd
import numpy as np


df = pd.read_csv('data_example_4_challenge.csv')

# mengubah data non numerik menjadi numerik
for i in df['Nama']:
    cek = 0
    try:
        df['Nama'].isnull()
        int(i)
        df.loc[cek, 'Nama'] = np.nan
        change = df['Nama'].fillna('noname', inplace=True)
    except ValueError:
        pass
        cek+=1
        print(df['Nama'])