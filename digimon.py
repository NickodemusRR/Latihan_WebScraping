# web scraping untuk mendapatkan data nama dan gambar digimon
from bs4 import BeautifulSoup
import requests 

url = 'https://wikimon.net/Visual_List_of_Digimon'
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, 'html.parser')

digimon = []

images = soup.find_all('img')
for image in images:
    my_dict = {
        'nama': image.get('alt'),
        'gambar': 'https://wikimon.net/images'+ image.get('src')
    }
    digimon.append(my_dict)

# menuliskan hasil web scrap ke file csv
import csv
with open('digimon.csv', 'w', newline='', encoding='utf8') as csv_file:
    fieldnames = ['nama', 'gambar']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(digimon)-2):
        writer.writerow(digimon[i])

# memasukkan data ke mysql
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'guest',
    passwd = '12345CobaFlask',
    database = 'digimon'
)

cursor = mydb.cursor()

for i in range(len(digimon)-2):
    nama = digimon[i]['nama']
    gambar = digimon[i]['gambar']
    cursor.execute('INSERT INTO digimon (nama,gambar) values (%s, %s)',(nama, gambar))
    mydb.commit()