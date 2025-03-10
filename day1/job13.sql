mysql> SELECT * FROM etudiant
-> WHERE age >= 18 AND age <= 25;

+----+-----------+-----------+-----+---------------------------------+
| id | lastname  | firstname | age | email                           |
+----+-----------+-----------+-----+---------------------------------+
|  1 | Spaghetti | Betty     |  23 | betty.Spaghetti@laplateforme.io |
|  3 | Doe       | John      |  18 | john.doe@laplateforme.io        |
|  5 | Dupuis    | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin    |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+-----------+-----+---------------------------------+
4 rows in set (0.00 sec)