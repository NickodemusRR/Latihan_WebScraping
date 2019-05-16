# Membuat database digimon di MySQL

Database dan tabel digimon dibuat terlebih dahulu menggunakan mysql.

```bash
mysql> create database digimon;
Query OK, 1 row affected (0.01 sec)

mysql> use digimon;
Database changed

mysql> create table digimon(
    -> id int auto_increment,
    -> nama varchar(255),
    -> gambar varchar(255),
    -> primary key(id));
Query OK, 0 rows affected (0.05 sec)

mysql> show tables;
+-------------------+
| Tables_in_digimon |
+-------------------+
| digimon           |
+-------------------+
1 row in set (0.00 sec)

mysql> describe digimon;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int(11)      | NO   | PRI | NULL    | auto_increment |
| nama   | varchar(255) | YES  |     | NULL    |                |
| gambar | varchar(255) | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```

Setelah program _digimon.py_ dijalankan maka data akan masuk ke dalam tabel digimon seperti berikut.
```bash
mysql> SELECT * FROM digimon LIMIT 10;
+----+---------------------+-------------------------------------------------------------------------------------------+
| id | nama                | gambar                                                                                    |
+----+---------------------+-------------------------------------------------------------------------------------------+
|  1 | Aegiochusmon        | https://wikimon.net/images/thumb/b/bd/Aegiochusmon.jpg/120px-Aegiochusmon.jpg             |
|  2 | Aegiochusmon: Blue  | https://wikimon.net/images/thumb/b/bb/Aegiochusmon_blue2.jpg/120px-Aegiochusmon_blue2.jpg |
|  3 | Aegiochusmon: Dark  | https://wikimon.net/images/thumb/7/7a/Aegiochusmon_dark.jpg/120px-Aegiochusmon_dark.jpg   |
|  4 | Aegiochusmon: Green | https://wikimon.net/images/thumb/d/d4/Aegiochusmon_green.jpg/120px-Aegiochusmon_green.jpg |
|  5 | Aegiochusmon: Holy  | https://wikimon.net/images/thumb/0/0b/Aegiochusmon_holly.jpg/120px-Aegiochusmon_holly.jpg |
|  6 | Aegiomon            | https://wikimon.net/images/thumb/9/98/Aegiomon2.jpg/120px-Aegiomon2.jpg                   |
|  7 | Aegisdramon         | https://wikimon.net/images/thumb/8/83/Ageisdramon.jpg/120px-Ageisdramon.jpg               |
|  8 | Aero V-dramon       | https://wikimon.net/images/thumb/5/54/Aerovdramon.jpg/120px-Aerovdramon.jpg               |
|  9 | Agnimon             | https://wikimon.net/images/thumb/d/dc/Agnimon3.jpg/120px-Agnimon3.jpg                     |
| 10 | Agumon              | https://wikimon.net/images/thumb/7/72/Agumon.jpg/120px-Agumon.jpg                         |
+----+---------------------+-------------------------------------------------------------------------------------------+
10 rows in set (0.00 sec)
```