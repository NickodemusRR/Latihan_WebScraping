# Menampilkan judul-judul film Power Rangers dari website Wikipedia
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

table = y.find(class_='wikitable')
title = table.find_all('i')
title_list = []
for i in title:
    print(i.text)               # menampilkan judul-judul seri Power Ranger
    title_list.append(i.text)   # memasukkan judul ke dalam list