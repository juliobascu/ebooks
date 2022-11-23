from mysql.connector import connect,Error
from getpass import getpass

class Database:

    def __init__(self) -> None:
        username = input("Ingrese nombre de usuario: ")
        password = getpass("Ingrese password: ")

        try:
            with connect(
                host="localhost",
                user=username,
                password=password,
            ) as connection:
                print(connection)
        except Error as e:
            print(f"ups ocurrio un error {e}....")

Database()