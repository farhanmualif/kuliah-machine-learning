import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
# baca file
df = pd.read_csv('iris.csv')

# split data fitur(x) label (y)
x_features = df.iloc[:, 1:5]
y_label = df.iloc[:, -1]

# membagi data training dan testing
x_training, x_testing, y_training, y_testing = train_test_split(
    x_features, y_label, test_size=0.2, random_state=2)

# model naive bayes
model = GaussianNB()

# training model menggunakan data training
model.fit(x_training, y_training)

# membuat prediksi
y_predict = model.predict(x_testing)

# menghitung nilai accuracy
accuracy = accuracy_score(y_testing, y_predict)
print('accuracy = ', format(accuracy*100))
