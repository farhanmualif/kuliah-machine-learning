import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans


# baca file
df = pd.read_csv('test.csv')
# mengisi missing value
# df = df.fillna(df.mean())
# # menentukan featues
# x_features = df.iloc[:, 6:]
# # menentukan label
# y_label = df['Customer Type']
# # membagi data training dan testing
# x_training, x_testing, y_training, y_testing = train_test_split(
#     x_features, y_label, test_size=0.2, random_state=2)
# # model naive bayes
# model = GaussianNB()
# # training model menggunakan data training
# model.fit(x_training, y_training)
# # membuat prediksi
# y_predict = model.predict(x_testing)
# # menghitung nilai accuracy
# accuracy = accuracy_score(y_testing, y_predict)
# print('accuracy = ', format(accuracy*100))

df = df.fillna(df.mean())
feature = df.iloc[:, 6:]
kmeans = KMeans(n_clusters=3)
kmeans.fit(feature)
df['result_cluster'] = kmeans.labels_
print(df)
