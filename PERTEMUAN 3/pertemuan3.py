import pandas as pd

exampleDataNull = pd.read_csv('data_example_null.csv')

# print(exampleDataNull.to_string())
# print('jumlah null\n',exampleDataNull.isnull().sum())

# print('jumlah total null ',exampleDataNull.isnull().sum().sum())
# print(exampleDataNull)
# print('')
# print(exampleDataNull['Nama'].isnull().values)

# mengubah nilai menjadi nilai null

dataMissing = pd.read_csv('data_example_null.csv', na_values=['n/n'])
print(dataMissing)















# checkName = input('masukan nama yang akan dicari : ')
# if checkName in exampleDataNull['Nama']:
#     print('nama ada')
# else:
#     print('nama tidak ada')
