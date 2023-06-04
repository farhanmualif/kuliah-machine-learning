import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans


class Kmeans:
    def __init__(self):
        self.data = None

    def inputFile(self):
        fileName = input('masukan nama file: ')
        if fileName:
            df = pd.read_csv(fileName)
            print('berhasil menemukan file: ', fileName)
            self.data = df
        else:
            print('tidak ada')

    def tampilHasil(self):
        self.data = self.data.fillna(self.data.mean())
        feature = self.data.iloc[:, 6:]
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(feature)
        self.data['result_cluster'] = kmeans.labels_
        print(self.data)


class Naive_bayes:
    def __init__(self):
        self.data = None

    def inputFile(self):
        fileName = input('masukan nama file: ')
        if fileName:
            df = pd.read_csv(fileName)
            print('berhasil menemukan file: ', fileName)
            self.data = df
        else:
            print('tidak ada')

    def tampilHasil(self):
        # mengisi missing value
        self.data = self.data.fillna(self.data.mean())
        # menentukan featues
        x_features = self.data.iloc[:, 6:]
        # menentukan label
        y_label = self.data['Customer Type']
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
        print('+'*20)
        print('accuracy = ', format(accuracy*100))
        print('+'*20)


def main():
    while True:
        try:
            menu()
            choice = int(input)
        except:
            print('An exception occurred')


def menu():
    print('1. naiv-bayes\n2. k-means')
