import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


df = pd.read_csv("soal.csv")

def tampilDataAsli():
    print(df.to_string())


def hitungJumlahNull():
    input_user = input("mising value pada kolom: ")
    cek = df[input_user].isna().sum()
    print("="*25)
    print('jumlah keseluruhan null ', cek)

def dataBaru():
     le = LabelEncoder()

     df.loc[3, "kode_barang"] = "B457"
     df.loc[2, "nama_barang"] = "kaos"
     df.loc[4, "nama_barang"] = "anduk"
     df.loc[7, "jumlah_barang"] = float(16)
     df["jenis_barang"].fillna("sandang", inplace=True)
     
     for col in df.columns[1:].values:
          if df[col].dtype == "object":
               data = df[col].append(df[col])
               le.fit(data.values)
               df[col]=le.transform(df[col])
     print(df.to_string())

def featureScaling():
     scaler = MinMaxScaler()
     df[["jumlah_barang"]] = scaler.fit_transform(df[["jumlah_barang"]])
     print(df)

def menu():
        print('-'*25)
        print('1. menampilkan data asli')
        print('2. menampilkan jumlah nul pada kolom')
        print('3. data setelah dilakukan perubahan dari non numerik menjadi numerik')
        print('4. menampilkan setelah feature scaling')
        print('5. keluar')
        print('-'*25)

def main():
    while True:
        menu()
        pilihMenu = int(input('pilih Menu : '))
        if pilihMenu == 1:
            tampilDataAsli()
        elif pilihMenu == 2:
            hitungJumlahNull()  
        elif pilihMenu == 3:
            dataBaru()
        elif pilihMenu == 4:
            featureScaling()
        elif pilihMenu == 5:
             exit()
        else:
             print("Input Invalid")

main()