import pandas as pd
from sklearn.cluster import KMeans

def inputFile(NamaFile):
   try:
     df = pd.read_csv(NamaFile)
     print('berhasil input file', NamaFile)
     return df
   except:
     print('File Tidak ada')

def jumlahCluster(jumlah):
   print('berhasil input jumlah cluster', jumlah)
   return jumlah

def tampilHasil(df, k):
   feature = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
   kmeans = KMeans(n_clusters=k)
   kmeans.fit(feature)
   df['result_cluster'] = kmeans.labels_
   print(df)

def menu():
   print('1. Input File')
   print('2. Input jumlah cluster')
   print('3. Tampil Hasil')
   print('4. Keluar')

def main():
   while True:
      try:
         menu()
         pilih = int(input('Pilih : '))
         if pilih == 1:
            file = input('Masukkan Nama File : ')
            df = inputFile(file)
         elif pilih == 2:
            angka = int(input('Masukkan jumlah cluster : '))
            k = jumlahCluster(angka)
         elif pilih == 3:
            tampilHasil(df, k)
         elif pilih == 4:
            exit()
      except:
        print('An exception occurred')
        break

main()