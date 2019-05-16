# Memasukan file csv ke database MySQL

import csv
import mysql.connector

mydb = mysql.connector.connect(
    host = 'your database host',        # contoh ini dijalankan dengan menggunakan database pada localhost
    user = 'your database username',
    passwd = 'your database password',
    database = 'your database name'     # dalam contoh ini adalah database digimon
)

cursor = mydb.cursor()

# bila saat menjalankan file berulang kali dan tidak ingin menumpuk data pada database
hapus = cursor.execute('DELETE FROM digimon2')                      # menghapus data di tabel yang sudah ada
mulai = cursor.execute('ALTER TABLE digimon2 AUTO_INCREMENT = 1')   # memulai kembali id dari 1

with open('digimon.csv','r') as csvfile:        # membuka file csv dengan mode read('r')
    csvreader = csv.reader(csvfile)
    next(csvreader)                             # untuk melewati baris header
    for row in csvreader:
        cursor.execute('INSERT INTO digimon2(nama, gambar) VALUES(%s, %s)', row) 
        mydb.commit()

cursor.close()                                  # memutus koneksi dengan database.