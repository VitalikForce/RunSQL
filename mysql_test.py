#!/usr/bin/python
# -*- coding: utf-8 -

import pymysql

def create_db_data():
  cursor.execute(""" CREATE TABLE IF NOT EXISTS `One` (
  `ID` int(11) UNSIGNED NOT NULL PRIMARY KEY,
  `Name` VARCHAR(100),
  `Surname` VARCHAR(100),
  `Salary/Year` int(11) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 """)
  cursor.execute(""" CREATE TABLE IF NOT EXISTS `Two` (
  `ID` int(11) UNSIGNED NOT NULL PRIMARY KEY,
  `Month` VARCHAR(100),
  `Taxes` int(11) DEFAULT NULL,
  `EmployeeID` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 """)
  cursor.execute(""" CREATE TABLE IF NOT EXISTS `Three` (
  `ID` int(11) UNSIGNED NOT NULL PRIMARY KEY,
  `InternalNumber` int(11) UNSIGNED DEFAULT NULL,
  `Position` VARCHAR(100),
  `EmployeeID` int(11) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
# PRIMARY KEY

# cursor.execute(r"CREATE TABLE IF NOT EXISTS One (ID INTEGER PRIMARY KEY, Name TEXT, Surname TEXT, Salary//Year INTEGER)")
# cursor.execute('''CREATE TABLE IF NOT EXISTS Two
#                 (ID INTEGER PRIMARY KEY, Month TEXT, Taxes INTEGER, EmployeeID INTEGER) ''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS Three
#                 (ID INTEGER PRIMARY KEY, InternalNumber INTEGER, Position TEXT, EmployeeID INTEGER) ''')
  cursor.execute(''' 
  INSERT INTO `One`(`ID`, `Name`, `Surname`,`Salary/Year`) 
  VALUES(1, 'Jhon', 'Terrible', 11000) ''')
  cursor.execute(''' 
  INSERT INTO `One`(`ID`, `Name`, `Surname`,`Salary/Year`) 
  VALUES(2, 'Maggy', 'Woodstock', 15000) ''')
  cursor.execute(''' 
  INSERT INTO `One`(`ID`, `Name`, `Surname`,`Salary/Year`) 
  VALUES(3, 'Joel', 'Muegos', 22000); ''')
  cursor.execute(''' 
  INSERT INTO `One`(`ID`, `Name`, `Surname`,`Salary/Year`) 
  VALUES(4, 'Jeroen', 'van Kapf', 44000) ''')
  db.commit()
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(1, '01.01.15', 250, 1) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(2, '01.02.15', 267, 1) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(3, '01.01.15', 300, 2) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(4, '01.02.15', 350, 2) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(5, '01.01.15', 245, 3) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(6, '01.02.15', 356, 3) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(7, '01.01.15', 246, 4) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(8, '01.02.15', 250, 4) ''')
  cursor.execute(''' 
  INSERT INTO `Two`(`ID`, `Month`, `Taxes`, `EmployeeID`) 
  VALUES(9, '01.03.15', 412, 3) ''')
  db.commit()

  cursor.execute(''' 
  INSERT INTO `Three`(`ID`, `InternalNumber`, `Position`, `EmployeeID`) 
  VALUES(1, 32824, 'Manager', 1) ''')
  cursor.execute(''' 
  INSERT INTO `Three`(`ID`, `InternalNumber`, `Position`, `EmployeeID`)  
  VALUES(2, 23409, 'Top Manager', 2) ''')
  cursor.execute(''' 
  INSERT INTO `Three`(`ID`, `InternalNumber`, `Position`, `EmployeeID`) 
  VALUES(3, 23409, 'SEO', 3) ''')
  cursor.execute(''' 
  INSERT INTO `Three`(`ID`, `InternalNumber`, `Position`, `EmployeeID`) 
  VALUES(4, 128, 'Board Chairman', 4) ''')
  db.commit()

doCreateDbData = 0 # 1 - perform create table and data. 0 - do not nother

db = pymysql.connect("127.0.0.1","vit","qaz","")

cursor = db.cursor()
cursor.execute("USE testdb")

if doCreateDbData:
  create_db_data()

cursor.execute("SELECT `ID`, CONCAT (`Name`, ' ' ,`Surname`) AS `Name/Surname`,`Salary/Year` FROM `One` ")

# data = cursor.fetchone()
# print ("Database version : %s " % data)
# alist = cursor.fetchmany()
j = 1
for i in cursor.fetchall():#[:]:
    print (j,' ',*i); j+=1

db.close()
