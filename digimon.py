# web scraping untuk mendapatkan data nama dan gambar digimon
from bs4 import BeautifulSoup
import requests 

url = 'https://wikimon.net/Visual_List_of_Digimon'
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, 'html.parser')

digimon = []    # list untuk menampung hasil web scraping

images = soup.find_all('img')
for image in images:
    # buat dictionary dengan key nama dan gambar
    my_dict = {
        'nama': image.get('alt'),
        'gambar': 'https://wikimon.net'+ image.get('src')
    }
    digimon.append(my_dict)     # menambahkan dictionary ke dalam list

# print(digimon)

# menuliskan hasil web scrap ke file csv
import csv
with open('digimon.csv', 'w', newline='', encoding='utf8') as csv_file:
    fieldnames = ['nama', 'gambar']     # membuat nama kolom yang akan diakses oleh key:value pada dictionary
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()                # menuliskan row header
    for i in range(len(digimon)-2):     # 2 baris terakhir pada list digimon tidak berisi nama digimon
        writer.writerow(digimon[i])

# memasukkan data ke mysql
import mysql.connector

mydb = mysql.connector.connect(
    host = 'your database host',
    user = 'your username',
    passwd = 'your password',
    database = 'database name'
)

cursor = mydb.cursor()

for i in range(len(digimon)-2):
    nama = digimon[i]['nama']
    gambar = digimon[i]['gambar']
    cursor.execute('INSERT INTO digimon (nama,gambar) values (%s, %s)',(nama, gambar))
    mydb.commit()