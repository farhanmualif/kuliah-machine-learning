import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from termcolor import cprint


def inputFile(NamaFile):
    try:
        df = pd.read_csv(NamaFile)
        cprint('Berhasil input file','green')
        return df
    except:
        cprint('File Tidak ada','red')

def inputNilaiK():
    nilai = int(input('masukan nilai K: '))
    cprint('berhasil memasukan nilai K','green')
    return nilai

def inputRandomState():
    nilai = int(input('input random state: '))
    cprint('berhasil memasukan nilai Random','green')
    return nilai

def bagiLatihUji():
    print('masukan nilai bagi antar latih dan uji contoh: (80:20, 60:40) :')
    train_size, test_size = map(float, input().split(':'))
    train_size = (train_size/100)
    test_size = (test_size/100)

    train_test = train_size+test_size

    if train_test > 1.0 :
      cprint('hasil pembagi harus kurang dari 1','red')
      exit()

    cprint('berhasil membagi data','green')
    return train_size, test_size

def tampilAkurasi(y_testing, y_prediksi):
    akurasi = accuracy_score(y_testing, y_prediksi)
    print('='*50)
    print('akurasi model adalah', format(akurasi*100),'%')
    print('='*50)

def jumlahCluster():
   jumlah = int(input('masukan jumlah cluster: '))
   cprint('berhasil memasukan jumlah cluster','green')
   print('berhasil input jumlah cluster', jumlah)
   return jumlah


def k_nn(df, train_size, test_size, random_state, k):
    df = df.fillna(df.mean())
    # tentukan label dan fitur
    x_fitur = df.iloc[:, 5:]     
    y_label = df.iloc[:, 1:2]
    # bagi data latih dan uji
    x_training, x_testing, y_training, y_testing = train_test_split(x_fitur , y_label, train_size = train_size, test_size = test_size, random_state = random_state)
    # fit model
    scaller = StandardScaler()
    x_training_sc = scaller.fit_transform(x_training)
    x_testing_sc = scaller.transform(x_testing)
    classifier = KNeighborsClassifier(n_neighbors = k)
    # fit models
    classifier.fit(x_training_sc, y_training)
    y_prediksi = classifier.predict(x_testing_sc)
    return y_testing, y_prediksi


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


def k_means(df, k, random_state, train_size, test_size):
    df = df.fillna(df.mean())
    y_features = df.iloc[:, 6:]
    x_training, _ = train_test_split(y_features, test_size=test_size, train_size=train_size, random_state=random_state)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x_training)
    # menambahkan kolom untuk hasil cluster
    df['result_cluster'] = kmeans.predict(y_features)
    return df


def menu():
    print('1. KNN')
    print('2. Naive Bayes')
    print('3. K-means')
    print('4. exit')

def main():
    menu()
    while True:
            try:
              algo = int(input('masukan jenis algoritma: '))
              os.system('cls')
              if algo == 1:
                    while True:
                        print('1. Input Data')
                        print('2. Input Nilai K')
                        print('3. Input pembagian antara data latih dan data uji')
                        print('4. Input Random State')
                        print('5. Hasil Akurasi')
                        choice = int(input('masukan pilihan: '))
                        if choice == 1:
                            namafile = input('nama file: ')
                            os.system('cls')
                            data = inputFile(namafile)
                        elif choice == 2:
                            os.system('cls')
                            inputK = inputNilaiK()
                        elif choice == 3:
                            os.system('cls')
                            train_size, test_size = bagiLatihUji()
                        elif choice == 4:
                            os.system('cls')
                            rand_state = inputRandomState()
                        elif choice == 5:
                            y_testing, y_prediksi = k_nn(data, train_size=train_size, test_size=test_size,random_state=rand_state,k=inputK)
                            os.system('cls')
                            tampilAkurasi(y_prediksi=y_prediksi, y_testing=y_testing)
                            return main() 
              elif algo == 2:
                while True:
                      print('1. Input Data')
                      print('2. Input pembagian antara data latih dan data uji')
                      print('3. Input Random State')
                      print('4. Hasil Akurasi')
                      choice = int(input('masukan pilihan: '))
                      if choice == 1:
                          namafile = input('nama file: ')
                          os.system('cls')
                          df = inputFile(namafile)
                      elif choice == 2:
                          os.system('cls')
                          train_size, test_size = bagiLatihUji()
                      elif choice == 3:
                          os.system('cls')
                          rand_state = inputRandomState()
                      elif choice == 4:
                          y_testing, y_predict = naive_bayes(df=df,train_size=train_size,test_size=test_size,random_state=rand_state)
                          os.system('cls')
                          tampilAkurasi(y_prediksi=y_predict, y_testing=y_testing)
                          return main()
              elif algo == 3:
                  while True:
                      print('1. Input Data')
                      print('2. Input pembagian antara data latih dan data uji')
                      print('3. Input Random State')
                      print('4. Input Nilai K')
                      print('5. Hasil Klustering')
                      choice = int(input('masukan pilihan: '))
                      if choice == 1:
                          namafile = input('nama file: ')
                          os.system('cls')
                          data = inputFile(namafile)
                      elif choice == 2:
                          os.system('cls')
                          train_size, test_size = bagiLatihUji()
                      elif choice == 3:
                          os.system('cls')
                          rand_state = inputRandomState()
                      elif choice == 4:
                          os.system('cls')
                          nilaiK = inputNilaiK()
                      elif choice == 5:
                          clustering = k_means(data, train_size=train_size, test_size=test_size,random_state=rand_state, k=nilaiK)
                          os.system('cls')
                          print('='*50)
                          print('='*15," HASIL CLUSTERING ",'='*15)
                          print('='*50)
                          print(clustering)
                        #   cek = clustering['result_cluster'].values
                        #   for i in cek:
                        #       if i == 1:
                        #           print(i)
              elif algo == 4:
                print('Terimakasih sudah mengunjungi😄')
                break
            except:
                cprint('Terjadi kesalahan😠', 'red')
                break
main()