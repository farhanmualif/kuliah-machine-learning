import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier



def inputFile(NamaFile):
    try:
        df = pd.read_csv(NamaFile)
        return df
    except:
        print('File Tidak ada')


# =========== KNN ===============
def inputNilaiK():
    nilai = int(input('masukan nilai K: '))
    return nilai

def inputRandomState():
    nilai = int(input('input random state: '))
    return nilai

def bagiLatihUji():
    print('masukan nilai bagi antar latih dan uji contoh: (80:20, 60:40) :')
    train_size, test_size = map(float, input().split())
    return train_size, test_size

def tampilAkurasi(y_testing, y_prediksi):
    akurasi = accuracy_score(y_testing, y_prediksi)
    print('='*50)
    print('akurasi model adalah', format(akurasi*100),'%')
    print('='*50)

# =========== K-MEANS ===============

def jumlahCluster():
   jumlah = int(input('masukan jumlah cluster: '))
   print('berhasil input jumlah cluster', jumlah)
   return jumlah

def k_nn(df, train_size, test_size, random_state, k):
    print(df)
    df = df.fillna(df.mean())
    x_fitur = df.iloc[:, 5:]     
    y_label = df.iloc[:, 1:2]
    x_training, x_testing, y_training, y_testing = train_test_split(x_fitur , y_label, train_size = train_size, test_size = test_size, random_state = random_state)
    scaller = StandardScaler()
    x_training_sc = scaller.fit_transform(x_training)
    x_testing_sc = scaller.transform(x_testing)
    classifier = KNeighborsClassifier(n_neighbors = k)
    classifier.fit(x_training_sc, y_training)
    y_prediksi = classifier.predict(x_testing_sc)
    return y_testing, y_prediksi



def k_means(df, k, random_state, train_size, test_size):
    df = df.fillna(df.mean())
    y_features = df.iloc[:, 6:]
    x_training, _ = train_test_split(y_features, test_size=test_size, train_size=train_size, random_state=random_state)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x_training)
    # menambahkan kolom untuk hasil cluster
    df['result_cluster'] = kmeans.predict(y_features)
    return df

def naive_bayes(df, train_size, test_size, random_state):
    # mengisi missing value
    df = df.fillna(df.mean())
    # menentukan featues
    x_features = df.iloc[:, 6:]
    # menentukan label
    y_label = df['Customer Type']
    # membagi data training dan testing
    x_training, x_testing, y_training, y_testing = train_test_split(
        x_features, y_label, test_size=test_size, random_state=random_state, train_size=train_size)
    # model naive bayes
    model = GaussianNB()
    # training model menggunakan data training
    model.fit(x_training, y_training)
    # membuat prediksi
    y_predict = model.predict(x_testing)
    return y_testing, y_predict


def menu():
    print('1. KNN')
    print('2. Naive Bayes')
    print('3. K-means')
    print('3. exit')

def run_knn():
        data = None
        train_size = None
        test_size = None
        rand_state = None
        inputK = None
        print('1. Input Data')
        print('2. Input Nilai K')
        print('3. Input pembagian antara data latih dan data uji')
        print('4. Input Random State')
        print('5. Hasil Akurasi')
        choice = int(input('masukan pilihan: '))
        if choice == 1:
            namafile = input('nama file: ')
            data = inputFile(namafile)
        elif choice == 2:
            inputK = inputNilaiK()
        elif choice == 3:
            train_size, test_size = bagiLatihUji()
        elif choice == 4:
             rand_state = inputRandomState()
        elif choice == 5:
            y_testing, y_prediksi = k_nn(data, train_size=train_size, test_size=test_size,random_state=rand_state,k=inputK)
            tampilAkurasi(y_prediksi=y_prediksi, y_testing=y_testing)
            return main()

def run_naive_bayes():
    print('1. Input Data')
    print('2. Input pembagian antara data latih dan data uji')
    print('3. Input Random State')
    print('4. Hasil Akurasi')
    choice = int(input('masukan pilihan: '))
    if choice == 1:
        namafile = input('nama file: ')
        df = inputFile(namafile)
    elif choice == 2:
        train_size, test_size = bagiLatihUji()
    elif choice == 3:
        rand_state = inputRandomState()
    elif choice == 4:
        y_testing, y_predict = naive_bayes(df=df,train_size=train_size,test_size=test_size,random_state=rand_state)
        tampilAkurasi(y_prediksi=y_predict, y_testing=y_testing)
        return main()


# namafile = input('nama file: ')
# df = inputFile(namafile)
# inputK = inputNilaiK()
# train_size, test_size = bagiLatihUji()
# rand_state = inputRandomState()
# df = k_means(df=df,k=inputK,random_state=rand_state, train_size=train_size, test_size=test_size)
# for i in df['result_cluster'].values:
#     if i != 0 :
#         print(i)


def run_k_means():
    print('1. Input Data')
    print('2. Input pembagian antara data latih dan data uji')
    print('3. Input Random State')
    print('4. Input Nilai K')
    print('5. Hasil Klustering')
    choice = int(input('masukan pilihan: '))
    if choice == 1:
        namafile = input('nama file: ')
        data = inputFile(namafile)
    elif choice == 2:
        train_size, test_size = bagiLatihUji()
    elif choice == 3:
        rand_state = inputRandomState()
    elif choice == 4:
        nilaiK = inputNilaiK()
    elif choice == 5:
        clustering = k_means(data, train_size=train_size, test_size=test_size,random_state=rand_state, k=nilaiK)
        print('='*50)
        print('='*24," HASIL CLUSTERING ",'='*24)
        print('='*50)
        print(clustering)
        return main()

def runAlgorithm(algo):
    while True:
        if algo == 1:
            run_knn()
        elif algo == 2:
            run_naive_bayes()
        elif algo == 3:
            run_k_means()

def main():
    menu()
    while True:
        algo = int(input('masukan jenis algoritma: '))
        runAlgorithm(algo)
        print('An exception occurred')
            
    
main()
# df = inputFile('test.csv')
# print(df.fillna(5))
# train_size, test_size = bagiLatihUji()
# random_state = inputRandomState()
# k = inputNilaiK()
# y_testing, y_prediksi = k_nn(df, train_size, test_size, random_state, k)
# tampilAkurasi(y_prediksi=y_prediksi, y_testing=y_testing)