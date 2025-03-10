mysql>  INSERT INTO etudiant (lastname, firstname, age, email)
-> VALUES ("Dupuis", "Martin", 18, "martin.dupuis@laplateforme.io");
Query OK, 1 row affected (0.02 sec)

mysql> SELECT * FROM etudiant
-> WHERE lastname = 'Dupuis';
+----+----------+-----------+-----+---------------------------------+
| id | lastname | firstname | age | email                           |
+----+----------+-----------+-----+---------------------------------+
|  5 | Dupuis   | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis   | Martin    |  18 | martin.dupuis@laplateforme.io   |
+----+----------+-----------+-----+---------------------------------+
2 rows in set (0.00 sec)