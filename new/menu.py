from libro import Libro
import os

class Menu:

    def __init__():
        os.system('cls')
        print("Seleccione una opcion ...")
        print("1 para listar los libros.. ")
        print("2 para agregar un libro")
        print("3 para editar un libro")
        print("4 para borrar un libro")
        print("0 para salir del sistema")

        valor = int(input("...\n"))

        if valor == 0:
            print("Adios ...")
            os._exit()
        elif valor == 1:
            os.system('cls')
            print("Listando libros...")
            Libro.list_all()
            
            
        elif valor == 2:
            os.system("cls")
            print("Solicitando datos de libros ...\n")
            codigo = int(input("Ingrese el codigo del libro "))
            nombre = input("Ingrese el nombre del libro ")
            autor = input("Ingrese el autor del libro ")
            fecha_pub = input("Ingrese fecha de publicacion del libro ")
            precio = int(input("Ingrese el precio del libro "))
            libro=Libro(codigo,nombre,autor,fecha_pub,precio,"")
            libro.insertar()
            print("Libro guardado exitosamente! \n")

        elif valor == 3:
            os.system("cls")
            print("Solicitando datos de libros ...\n")
            Libro.list_all()
            idlibro=input("Ingrese el ID del libro que quiere EDITAR : ")
            codigo = int(input("Ingrese el codigo del libro "))
            nombre = input("Ingrese el nombre del libro ")
            autor = input("Ingrese el autor del libro ")
            fecha_pub = input("Ingrese fecha de publicacion del libro ")
            precio = int(input("Ingrese el precio del libro "))
            libro=Libro(codigo,nombre,autor,fecha_pub,precio,idlibro)
            libro.editar()
            print("Libro guardado exitosamente! \n")

        elif valor == 4:
            os.system("cls")
            print("Solicitando datos de libros ...\n")
            Libro.list_all()
            idlibro=input("Ingrese el ID del libro que quiere BORRAR : ")
            Libro.borrar(idlibro)
            print("Libro borrado exitosamente! \n")
        else:
            print("No se reconoce el comando ... :s")
            Menu.__init__()
    
    def post_listar_libros():
        print("Ingrese el id del libro a modificar")
        print("Ingrese 0 para salir de la app")
        value = input("\n")
        if value == 0:
            print("Adios..")
        else:
            print(f'se va a modificar el libro con id {value}...')
            
while True:
    Menu.__init__()
    input("presione ENTER para continuar......")