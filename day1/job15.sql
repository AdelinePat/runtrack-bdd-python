mysql> SELECT * FROM etudiant
-> ORDER BY lastname;

+----+-----------+-----------+-----+---------------------------------+
| id | lastname  | firstname | age | email                           |
+----+-----------+-----------+-----+---------------------------------+
|  4 | Barnes    | Binkie    |  16 | binkie.barnes@laplateforme.io   |
|  3 | Doe       | John      |  18 | john.doe@laplateforme.io        |
|  5 | Dupuis    | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin    |  18 | martin.dupuis@laplateforme.io   |
|  1 | Spaghetti | Betty     |  23 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck     |  45 | chuck.steak@laplateforme.io     |
+----+-----------+-----------+-----+---------------------------------+
6 rows in set (0.02 sec)