import pandas as pd

from sklearn.model_selection import train_test_split 

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score

data = pd.read_excel('KNN.xlsx')
print(data)

x_fitur = data.iloc[:, 1:5]     
y_label = data.iloc[:, -1]     

#print(x_fitur)
#print(y_label)

x_training, x_testing, y_training, y_testing = train_test_split(x_fitur , y_label, train_size = 0.8, test_size = 0.2, random_state = 2)

scaller = StandardScaler()
x_training_sc = scaller.fit_transform(x_training)
x_testing_sc = scaller.transform(x_testing)

classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(x_training_sc, y_training)

y_prediksi = classifier.predict(x_testing_sc)

akurasi = accuracy_score(y_testing, y_prediksi)
print('akurasi model adalah', format(akurasi*100),'%')