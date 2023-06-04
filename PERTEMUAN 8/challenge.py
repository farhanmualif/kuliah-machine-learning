import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# baca file
df = pd.read_excel('challenge8.xlsx')

sns.set(style = 'dark')
ax = sns.countplot(x="Gender", data = df)

numerik = df.select_dtypes(include='float64')
numerikIndex = numerik.columns # menampilkan kolom
df.hist(column=numerikIndex, figsize=(15,15), layout=(4,1))
plt.show()