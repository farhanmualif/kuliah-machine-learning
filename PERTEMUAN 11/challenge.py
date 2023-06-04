import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans


def inputFile(NamaFile):
    try:
        df = pd.read_csv(NamaFile)
        print('berhasil input file', NamaFile)
        return df
    except:
        print('File Tidak ada')


def k_means(df):
    df = df.fillna(df.mean())
    feature = df.iloc[:, 6:]
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(feature)
    df['result_cluster'] = kmeans.labels_
    print(df)


def naive_bayes(df):
    # mengisi missing value
    df = df.fillna(df.mean())
    # menentukan featues
    x_features = df.iloc[:, 6:]
    # menentukan label
    y_label = df['Customer Type']
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


def menu():
    print('1. Naive bayes')
    print('2. K-means')
    print('3. exit')


def menuProgram():
    print('1. Input file')
    print('2. Tampil hasil')


def runAlgorithm(algo):
    while True:
        menuProgram()
        choice = int(input('masukan pilihan: '))
        if choice == 1:
            namafile = input('nama file: ')
            df = inputFile(namafile)
        elif choice == 2:
            if algo == 1:
                naive_bayes(df)
                return
            elif algo == 2:
                k_means(df)
                return


def main():
    menu()
    while True:
        try:
            algo = int(input('masukan jenis algoritma: '))
            runAlgorithm(algo)
        except:
            print('terjadi kesalahan')
            break


main()
