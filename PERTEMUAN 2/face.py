import pandas as pd

dataExample = pd.read_csv('data_example.csv')
exampleDataNull = pd.read_csv('data_example_null.csv')
rekapNilai = pd.read_csv('rekap_penilaian.csv')


# cek null
# cekNull = getData.isnull()
# print(cekNull)
# cek null (array)
# cekNull = getData.isnull().values
# print(cekNull)
# cek null 3 (keseluruhan)


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
print(exampleDataNull.to_string())