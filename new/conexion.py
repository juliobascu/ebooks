from getpass import getpass
from mysql.connector import connect, Error
import login
class Conexion:

    def __init__(self):
        try:
            aux = connect(
                host='localhost',
                user='root',
                password=login.Login.contraseña,
                database='biblioteca'
            )
            self.connection = aux
            #print("conexion exitosa...")
        except Error as e:
            print("Eror ",e)

    def ieb(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)

    def list(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()#me devuelve una lista
        for registro in resultado:#me devuelve una tupla
            print(f"""Id:{registro[0]}  Codigo:{registro[1]}  Nombre:{registro[2]}  Autor:{registro[3]}  Fecha:{registro[4]}  Precio:{registro[5]}  Stock:{registro[6]}
==========================================================================================================================================================
            """)
        self.close()

    def listcarrito(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()#me devuelve una lista
        for registro in resultado:#me devuelve una tupla
            print(f"""Id:{registro[0]}  Codigo:{registro[1]}  Nombre:{registro[2]}  Autor:{registro[3]}  Fecha:{registro[4]}  Precio:{registro[5]}
=======================================================================================================================================================================
""")
        self.close()

    def liststock(self, sql):
        cursor = self.connection.cursor()
        #print(cursor)
        cursor.execute(sql)
        resultado = cursor.fetchall()#me devuelve una lista
        stock=int(resultado[0][0])
        login.Login.stock = stock
        #print(stock)
        self.close()

    def close(self):
        self.connection.close()
        #print("La conexion fue cerrada")

