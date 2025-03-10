mysql> SELECT * FROM etudiant
-> WHERE firstname LIKE 'b%';

+----+-----------+-----------+-----+---------------------------------+
| id | lastname  | firstname | age | email                           |
+----+-----------+-----------+-----+---------------------------------+
|  1 | Spaghetti | Betty     |  23 | betty.Spaghetti@laplateforme.io |
|  4 | Barnes    | Binkie    |  16 | binkie.barnes@laplateforme.io   |
+----+-----------+-----------+-----+---------------------------------+
2 rows in set (0.02 sec)