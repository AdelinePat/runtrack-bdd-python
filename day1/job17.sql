mysql> UPDATE etudiant
-> SET age = 20 WHERE id = 1;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> TABLE etudiant;
+----+-----------+-----------+-----+---------------------------------+
| id | lastname  | firstname | age | email                           |
+----+-----------+-----------+-----+---------------------------------+
|  1 | Spaghetti | Betty     |  20 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck     |  45 | chuck.steak@laplateforme.io     |
|  3 | Doe       | John      |  18 | john.doe@laplateforme.io        |
|  4 | Barnes    | Binkie    |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin    |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+-----------+-----+---------------------------------+
6 rows in set (0.00 sec)