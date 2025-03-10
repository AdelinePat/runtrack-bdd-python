mysql> SELECT * FROM etudiant
-> WHERE age = (SELECT MIN(age) FROM etudiant);
+----+----------+-----------+-----+-------------------------------+
| id | lastname | firstname | age | email                         |
+----+----------+-----------+-----+-------------------------------+
|  4 | Barnes   | Binkie    |  16 | binkie.barnes@laplateforme.io |
+----+----------+-----------+-----+-------------------------------+
1 row in set (0.02 sec)