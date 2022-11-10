import mysql.connector


try:
    conexion = mysql.connector.connect(user="jbascunan",password="Isabellabascu1409",host="localhost",database="pruebapy",port="3306")

    print("conexion exitosa")

except:
    print("error de conexion")


