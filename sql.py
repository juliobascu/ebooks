from mysql.connector import connect,Error
from getpass import getpass

class Database:

    def __init__(self) -> None:
        try:
            self.connection = connect(
                    host="localhost",
                    user="root",
                    database="ebooks",
                    password="Isabellabascu1409"
            )
        except Error as e:
            print(f"Error {e}")


    def select(self):
        cursor = self.connection.cursor()
        sql ="SELECT * FROM libros"
        cursor.execute(sql)
        #fetchall 
        resp = cursor.fetchall()
        for row in resp:
            print("===================================================")
            print(row)
            print("===================================================")
        

    def insert(self):
        cod=int(input("Ingrese codigo del libro: "))
        nom=input("Inserte el nombre del libro: ")
        cost=int(input("Inserte el valor del libro: "))
        cursor = self.connection.cursor()
        sql=f"INSERT INTO libros (codigo,nombre,creditos) VALUES ({cod},'{nom}',{cost});"
        cursor.execute(sql)
        self.connection.commit()

    def getbyid(self,pk):
        cursor=self.connection.cursor()
        cursor.execute()    

    def close(self):
        self.connection.close()
        print("conexion cerrada....")

db = Database()

db.select()
db.insert()
db.select()
db.close()

