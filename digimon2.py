# Memasukan file csv ke database MySQL

import csv
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'guest',
    passwd = '12345CobaFlask',
    database = 'digimon'
)

cursor = mydb.cursor()

# menghapus data di tabel yang sudah ada
hapus = cursor.execute('DELETE FROM digimon2')

# memulai kembali id dari 1
mulai = cursor.execute('ALTER TABLE digimon2 AUTO_INCREMENT = 1')

with open('digimon.csv','r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        cursor.execute('INSERT INTO digimon2(nama, gambar) VALUES(%s, %s)', row) 
        mydb.commit()
#close the connection to the database.
cursor.close()