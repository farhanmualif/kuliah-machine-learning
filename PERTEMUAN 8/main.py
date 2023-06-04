import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# baca file
df = pd.read_excel('Mall_Customers.xlsx')
df.info() # menampilkan informasi file

# menghitung nilai atribut
count_gender = df.Gender.value_counts()
print(count_gender)

# menampilkan data
# sns.set(style = 'darkgrid')
# ax = sns.countplot(x="Gender", data = df)

# hitung setiap jumlah nilainya
# for x in ax.patches:
#     height = x.get_height()
#     ax.text(x.get_x() + x.get_width()/2. , height , '{:1.0f}'.format((height)), ha="center")

# menampilkan data bernilai numerik
numerik = df.select_dtypes(include='int64')
numerikIndex = numerik.columns # menampilkan kolom
df.hist(column=numerikIndex, figsize=(10,10), layout=(4,2))
plt.show()