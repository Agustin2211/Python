import sqlite3

conn = sqlite3.connect('test.db') #CONECTARME CON LA BASE DE DATOS


conn.execute('''CREATE TABLE PERSONAS
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            SURNAME TEXT NOT NULL);''')

conn.execute("INSERT INTO PERSONAS(ID,NAME,SURNAME) VALUES (1,'AGUSTIN','PAS')")
conn.execute("INSERT INTO PERSONAS(ID,NAME,SURNAME) VALUES (2,'CARLOS','RAUL')")
conn.execute("INSERT INTO PERSONAS(ID,NAME,SURNAME) VALUES (3,'ELZA','PATO')")
conn.execute("INSERT INTO PERSONAS(ID,NAME,SURNAME) VALUES (4,'ESTEBAN','QUITO')")
conn.execute("INSERT INTO PERSONAS(ID,NAME,SURNAME) VALUES (5,'MAXI','TAXI')")

conn.execute('''CREATE TABLE PUESTOS
            (ID INT PRIMARY KEY NOT NULL,
            PUESTO TEXT NOT NULL);''')

conn.commit()

datos = conn.execute("SELECT * FROM PERSONAS")
for i in datos:
    print(i)

datos = conn.execute("SELECT NAME FROM PERSONAS")
for i in datos:
    print(i)

conn.execute("DELETE FROM USERS WHERE ID = 4")

conn.execute("UPDATE PERSONAS SET NAME = 'AGUSTIN' WHERE ID = 3")

conn.close()