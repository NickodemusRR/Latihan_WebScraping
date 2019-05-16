# Web Scraping

Repository ini berisi beberapa contoh penggunaan package __BeautifulSoup__ pada __python__ untuk melakukan web scraping.

Berikut adalah definisi web scraping menurut Wikipedia
https://en.wikipedia.org/wiki/Web_scraping

Terlebih dahulu silakan install package BeautifulSoup
```bash
pip install beautifulsoup4
```
atau untuk python dengan distribusi dari anaconda
```
conda install beautifulsoup4
```

Import BeautifulSoup pada program python.
```python
from bs4 import BeautifulSoup
```

## Update 2
Menambahkan file
1. *rangers_series.py*
2. *digimon.py*
3. *digimon_csv_sql.py*
Berisi contoh cara memasukkan hasil web scraping ke dalam file csv dan database mysql.

## Situs yang digunakan
Situs-situs yang digunakan untuk latihan webscraping ini adalah:
1. https://wikimon.net/Visual_List_of_Digimon --> digimon
2. https://pokemondb.net/pokedex/national --> pokemon
3. https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes --> power rangers

### Contoh Penggunaan Web Scraping
* *digimon.py* => mengambil nama dan link gambar digimon lalu memasukkanya ke dalam file csv dan database mysql
* *digimon_csv_sql.py* => memasukan data ke database mysql dari file csv
* *pokemon.py* => mengambil id dan nama pokemon lalu memasukkannya ke dalam file csv
* *rangers_title.py* => mengambil judul-judul seri Power Rangers
* *rangers_series*  => mengambil judul seri beserta tanggal tayang Power Ranges lalu memasukkannya ke dalam file csv