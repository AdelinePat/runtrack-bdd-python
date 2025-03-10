mysql> SELECT * FROM etudiant
-> WHERE firstname = 'Gertrude' AND lastname = 'Dupuis';

+----+----------+-----------+-----+---------------------------------+
| id | lastname | firstname | age | email                           |
+----+----------+-----------+-----+---------------------------------+
|  5 | Dupuis   | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
+----+----------+-----------+-----+---------------------------------+
1 row in set (0.00 sec)