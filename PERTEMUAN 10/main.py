import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('Iris.csv')

# tentukan feature
feature = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
# tentukan jumlah cluster
k = 3
# membuat model
kmeans = KMeans(n_clusters=k)
kmeans.fit(feature)
# menambahkan kolom untuk hasil cluster
df['result_cluster'] = kmeans.labels_
print(df)