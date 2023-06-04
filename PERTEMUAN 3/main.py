import pandas as pd

dataExample = pd.read_csv('data_example.csv')
exampleDataNull = pd.read_csv('data_example_null.csv')
rekapNilai = pd.read_csv('rekap_penilaian.csv')


# cek null
# cekNull = dataExample.isnull()
# print(cekNull)
# cek null (array)
# cekNull = dataExample.isnull().values
# print(cekNull)
# cek null 3 (keseluruhan)
# cekNull = dataExample.isnull().values.any()
# print(cekNull)

# print('rekap penilaian')
# print(exampleDataNull.isnull().values)


# chalange 1
# def data_example():
#     cekNull = dataExample.isnull().values.any()
#     if cekNull == False:
#         print('tidak terdapat data null')
#     else:
#         print('ada data null')


# def example_data_null():
#     cekNull = exampleDataNull.isnull().values.any()
#     if cekNull == False:
#         print('tidak terdapat data null')
#     else:
#         print('ada data null')

# data_example()
# example_data_null()

# if dataExample.isnull().values.any() and exampleDataNull.isnull().values.any() == False:
#     print('tidak ada data null')
# else:
#     print('ada data null')

# print(exampleDataNull.to_string())

# cekNull1 = dataExample.isnull().values.any()
# cekNull12 = exampleDataNull.isnull().values.any()

# cek = [cekNull1, cekNull12]
# for i in cek:
#     print(i)


# data = exampleDataNull['Samaran'].values
# print(data)
# for i in range(len(data)):
#     if data[i] == 'n/n':
#         data[i] = 'Gbs'
# print(data)

# data = exampleDataNull['Nama']
# print(data)

# print(exampleDataNull['Agama'].isnull())
# exampleDataNull['Agama'].fillna(20, inplace=True)
# print(exampleDataNull.to_string())


# check = input('masukan nama yang akan dicari : ')
# nama = any(exampleDataNull['Nama'] == check)
# if nama == True:
#     print('data yang anda cari tersedia')
# else:
#     print('data tidak ada')















import os
df = pd.read_csv('challenge_2.csv')


def tampilDataAsli():
    print(df.to_string())

def tammpilDataModif():
    df = pd.read_csv('challenge_2.csv', na_values=['--',"?"])
    print(df.to_string())

def cekNullKeseluruhan():
    cek = df.isnull().values.any()
    if cek == True:
        print('tedapat nilai null')
    else:
        print('tidak ada nilai null')

def hitungJumlahNull():
    cek = df.isnull().sum().sum()
    print('jumlah keseluruhan null ', cek)

def membacaKolom():
    cek = input('masukan kolom yang ingin di baca :')
    if any(df.columns.values == cek):
      print(df[cek])
    else:
        print('tidak')    

def menu():
        print('-'*25)
        print('1. tampilkan data asli')
        print('2. tampilkan data modif')
        print('3. cek null keseluruhan')
        print('4. hitung jumlah null')
        print('5. membaca perkolom')
        print('6. exit')
        print('-'*25)

def main():
    while True:
        menu()
        pilihMenu = int(input('pilih Menu : '))
        match(pilihMenu):
            case 1: 
                tampilDataAsli()
            case 2:
                os.system('cls')
                tammpilDataModif()
            case 3:
                cekNullKeseluruhan()
            case 4:
                hitungJumlahNull()
            case 5:
                membacaKolom()
            case 6:
                exit()

main()


