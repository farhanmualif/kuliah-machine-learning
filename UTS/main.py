import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# membaca data
df = pd.read_csv('Iris.csv')

# Memisahkan antara fitur (x) dan label (y)
x = df.drop(['Id', 'Species'], axis=1)
y = df['Species']

# Membagi dataset menjadi data latih dan data uji
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# melakukan normalisasi
scaler = MinMaxScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# proses training KNN
KNN = KNeighborsClassifier(n_neighbors=5)
KNN.fit(x_train_scaled, y_train)

# prediksi
y_prediction = KNN.predict(x_test_scaled)
print('hasil prediksi: \n',y_prediction)

# akurasi model
accuracy = accuracy_score(y_test, y_prediction)
print('akurasi model: ',accuracy)