#!/usr/bin/python
"""Vitalik 
 SQL example use
"""
# -*- coding: utf-8 -
import sqlite3
import pprint
# import sqlite3test.userfunctions as T

con = sqlite3.connect('mybase.db')
cur = con.cursor()

# cur.execute('''SELECT COUNT(TABLE) from *''')
# print(cur.fetchone())
# chch = ord('/')

# Create table
cur.execute('''DROP TABLE `One` ''')
cur.execute('''DROP TABLE `Two` ''')
cur.execute('''DROP TABLE `Three` ''')
cur.execute('''CREATE TABLE `One` 
            (`ID` INTEGER PRIMARY KEY, `Name` TEXT, `Surname` TEXT,
             `Salary/Year` INTEGER)''')
cur.execute(''' CREATE TABLE `Two`
            (`ID` INTEGER PRIMARY KEY, `Month` TEXT, `Taxes` INTEGER,
             `EmployeeID` INTEGER)''')
cur.execute('''CREATE TABLE `Three`
            (`ID` INTEGER PRIMARY KEY, `InternalNumber` INTEGER,
             `Position` TEXT, `EmployeeID` INTEGER)''')
cur.executescript('''
    INSERT INTO `One` VALUES (1, 'Jhon', 'Terrible', 11000);
    INSERT INTO `One` VALUES(2, 'Maggy', 'Woodstock', 15000);
    INSERT INTO `One` VALUES(3, 'Joel', 'Muegos', 22000);
    INSERT INTO `One` VALUES(4, 'Jeroen', 'van Kapf', 44000);

    INSERT INTO `Two` VALUES(1, '01.01.15', 250, 1);
    INSERT INTO `Two` VALUES(2, '01.02.15', 267, 1);
    INSERT INTO `Two` VALUES(3, '01.01.15', 300, 2);
    INSERT INTO `Two` VALUES(4, '01.02.15', 350, 2);
    INSERT INTO `Two` VALUES(5, '01.01.15', 245, 3);
    INSERT INTO `Two` VALUES(6, '01.02.15', 356, 3);
    INSERT INTO `Two` VALUES(7, '01.01.15', 246, 4);
    INSERT INTO `Two` VALUES(8, '01.02.15', 250, 4);
    INSERT INTO `Two` VALUES(9, '01.03.15', 412, 3);

    INSERT INTO `Three` VALUES(1, 32824, 'Manager', 1);
    INSERT INTO `Three` VALUES(2, 23409, 'Top Manager', 2);
    INSERT INTO `Three` VALUES(3, 23908, 'SEO', 3);
    INSERT INTO `Three` VALUES(4, 128, 'Board Chairman', 4);
''')
con.commit()

# var 1
print ("variant 1")
cur.execute("""SELECT Three.InternalNumber AS 'InternalNumber', 
            (One.Name || ' ' || One.Surname) AS `Name/Surname`,
            Three.Position AS 'Position',
            One.`Salary/Year`/ (
            SELECT COUNT(t.Month) FROM Two t WHERE t.EmployeeID == One.ID)  
            AS `Salary/Month`,
            Two.Taxes AS 'Taxes', Two.Month AS 'Month'  FROM One, Two, Three
            WHERE One.ID == Two.EmployeeID AND One.ID == Three.EmployeeID
            ORDER BY Three.Position
            """)
    # ORDER BY Three.InternalNumber
j = 1
for i in cur.fetchall(): 
    print (j,' ', end='')
    pprint.pprint(i) # print(*i, sep =", ")
    j+=1

# var 2
print ("variant 2")
cur.execute("""SELECT DISTINCT Three.InternalNumber AS 'InternalNumber', 
            (One.Name || ' ' || One.Surname) AS `Name/Surname`,
            Three.Position AS 'Position',
            One.`Salary/Year`/ (
            SELECT COUNT(t.Month) FROM Two t WHERE t.EmployeeID == One.ID)
            AS `Salary/Month`
            FROM One, Two, Three
            WHERE One.ID == Two.EmployeeID AND One.ID == Three.EmployeeID
            ORDER BY Three.Position
            """)
    # ORDER BY Three.InternalNumber Two.Taxes AS 'Taxes', Two.Month AS 'Month' 
j = 1
for i in cur.fetchall(): 
    print (j,' ', end='')
    pprint.pprint(i)
    j+=1
# print (*cur.fetchall()[:])
print()

# Test SQL
# cur.execute("""SELECT Three.InternalNumber AS 'InternalNumber', 
#                 (One.Name||' ' ||One.Surname) AS 'Name/Surname',
#                 Three.Position AS 'Position',
#                  One.`Salary/Year`/ COUNT( DISTINCT Two.Month),
#                   Two.Taxes AS 'Taxes',
#                 COUNT( DISTINCT Two.Month) AS 'Month' FROM One, Two, Three
#                 WHERE  One.ID == Two.EmployeeID AND One.ID == Three.EmployeeID
#                 GROUP BY Two.Month
#                 """)
                
# j = 1
# for i in cur.fetchall():#[:]:
#     print (j,' ',*i); j+=1
# print ()

# Test SQL
# cur.execute("""SELECT Three.InternalNumber , 
#                 ((One.Name|| ' ' ||One.Surname),
#                 Three.Position, 
#                 One.`Salary/Year`/ (SELECT DISTINCT Two.Month FROM Two), 
#                 Two.Taxes
#                 (SELECT DISTINCT Two.Month FROM Two) FROM One, Two, Three
#                 WHERE  One.ID == Two.EmployeeID AND One.ID == Three.EmployeeID
#                 """)

# j = 1
# for i in cur.fetchall()[:]:
#     print (j,' ',i); j+=1

# j = 1
# for i in cur.fetchall():#[:]:
#     print (j,' ',*i); j+=1

# print (*cur.fetchall()[:])
print ()

cur.close()
con.close()

# import sqlite3 as T
# sqlite3.test.userfunctions.test()
#ttt = T.unittest.TextTestRunner()