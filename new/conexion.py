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
            print("conexion exitosa...")
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
        resultado = cursor.fetchall()
        for registro in resultado:
            print(registro)
        self.close()

    def close(self):
        self.connection.close()
        print("La conexion fue cerrada")

