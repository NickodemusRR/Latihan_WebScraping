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

### Contoh Penggunaan
* _rangers_title.py_ => menampilkan judul-judul seri Power Rangers.
* _pokemon.py_ => menampilkan id dan nama pokemon lalu memasukkannya ke dalam file csv.
