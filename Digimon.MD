# Membuat database digimon di MySQL

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
