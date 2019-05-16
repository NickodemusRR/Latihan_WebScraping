from bs4 import BeautifulSoup
import requests
import csv

url = 'https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

table = y.find(class_='wikitable')
rows = table.find_all('tr')

list_title = []     # list untuk menampung judul seri (title)
start_date = []     # list untuk tanggal mulai ditayangkan (first aired)
end_date = []       # list untuk tanggal terakhir ditangkan (last aired)

for row in rows:
    for column in row.find_all('td'):
        for title in column.find_all('i'):      # mengakses judul film yang terdapat pada tag <i>
            list_title.append(title.text)
            # print(title.text)
            
            # mengakses tanggal pada tag <span>
            for start in row.find_all('span', class_='bday dtstart published updated'):
                start_date.append(start.text)
            for end in row.find_all('span', class_='dtend'):
                end_date.append(end.text)

# karena pada dua judul seri terakhir tag <span> tidak memiliki attribute class,
# maka data ditambahkan secara manual
start_date.append('2019-03-02')
end_date.extend(['2018-12-01', 'TBA'])

# memasukan data yang diperoleh ke file csv
import csv

with open('powerRangers.csv', mode='w', newline='') as data:
    data_writer = csv.writer(data)
    for i in range(len(list_title)):
        data_writer.writerow([list_title[i], start_date[i], end_date[i]])