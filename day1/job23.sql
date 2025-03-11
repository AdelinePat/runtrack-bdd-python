SELECT * FROM etudiant
WHERE age = (SELECT MAX(age) FROM etudiant);

+----+----------+-----------+-----+-----------------------------+
| id | lastname | firstname | age | email                       |
+----+----------+-----------+-----+-----------------------------+
|  2 | Steak    | Chuck     |  45 | chuck.steak@laplateforme.io |
+----+----------+-----------+-----+-----------------------------+
1 row in set (0.00 sec)