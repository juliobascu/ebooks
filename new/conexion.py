from getpass import getpass
from mysql.connector import connect, Error

class Conexion:

    def __init__(self):
        try:
            aux = connect(
                host='localhost',
                user='root',
                password= "Isabellabascu1409",#getpass("Ingrese password de SQL"),
                database='biblioteca'
            )
            self.connection = aux
            print("conexion exitosa...")
        except Error as e:
            print("Eror ",e)

    def insert(self, sql):
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
        resultado = cursor.fetchall()
        for registro in resultado:
            print(registro)
        self.close()

    
    def getById(self, pk):
        cursor = self.connection.cursor()
        cursor.execute

    def close(self):
        self.connection.close()
        print("La conexion fue cerrada")

