# Mencari data nama dan id pokemon dari website 'https://pokemondb.net/pokedex/national'
from bs4 import BeautifulSoup
import requests

url = 'https://pokemondb.net/pokedex/national'
web = requests.get(url)
soup = BeautifulSoup(web.content, 'html.parser')

# mencari span dengan class "infocard-lg-data text-muted" yang berisi nama dan id pokemon 
span = soup.find_all('span', class_="infocard-lg-data text-muted")
my_list = []

# mengakses nama dan id pokemon lalu membuat dictionary yang dimasukkan ke dalam list
for i in span:
    id = i.find('small').text
    nama = i.find('a').text
    my_list.append({'id': id, 'nama':nama})

print(my_list)

# list pokemon diubah menjadi file csv
import csv
with open('pokemon.csv', 'w', newline='', encoding='utf8') as csv_file:
    fieldnames = ['id', 'nama']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(my_list)):
        writer.writerow(my_list[i])