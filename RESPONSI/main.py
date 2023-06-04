# nama : Farhan Mualif
# NPM : 5210411219



import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('soal.csv')

def hitung_jumlah_null():
    print('total jumlah null setiap kolom\n',df.isna().sum())

def feature_scaling():
    df[' jenis_  barang '].fillna('sandang', inplace=True)
    df['  nama_barang'].fillna('kaos', inplace=True)

    le = MinMaxScaler()
    df.loc[3,'  jumlah _barang'] = float(5)
    df[['  jumlah _barang']] = le.fit_transform(df[['  jumlah _barang']])

    for i in df.columns.values:
        if df[i].dtypes == 'object':
          data = df[i].append(df[i])
          lb = LabelEncoder()
          lb.fit(data.values)
          df[i] = lb.transform(df[i])
          pass
    print('\nhasil feature scaling pada kolom jumlah barang\n',df)

hitung_jumlah_null()
# print(df)
feature_scaling()