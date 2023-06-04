import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score

# ambil data
df = pd.read_excel('KNN.xlsx')

# memisahkan features(x_features) dengan label
x_features = df.iloc[:, 1:5] # ambil features
y_label = df.iloc[:, -1] # ambil label

# membagi antara data training dengan data testing
x_train, x_test, y_train, y_test = train_test_split(x_features, y_label, test_size = 0.8, train_size=0.2, random_state = 2)

# feature scalling
# menstandarisasi nilai pada attribut features
scaler = StandardScaler()
x_train_sc = scaler.fit_transform(x_train)
x_test_sc = scaler.transform(x_test)

# scaler = MinMaxScaler()
# x_train_sc = scaler.fit_transform(x_train)
# x_test_sc = scaler.transform(x_test)

# training KNN
KNN = KNeighborsClassifier(n_neighbors=3)
KNN.fit(x_train_sc, y_train)

# prediksi
y_pred = KNN.predict(x_test_sc)

# menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print('akurasi model: ',format(accuracy*100), '%')

