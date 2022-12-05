from libro import Libro
import os
import login
from getpass import getpass
from conexion import Conexion


class Menu:
    
    def __init__():
        os.system('cls')
        print("Seleccione una opcion ...")
        print("1 para listar los libros.. ")
        print("2 para agregar un libro")
        print("3 para editar un libro")
        print("4 para borrar un libro")
        print("5 para agregar STOCK a un libro")
        print("0 para salir del sistema")

        valor = int(input("...\n"))

        if valor == 0:
            print("""
            ██████╗ ██╗   ██╗███████╗    ██████╗ ██╗   ██╗███████╗
            ██╔══██╗╚██╗ ██╔╝██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔════╝
            ██████╔╝ ╚████╔╝ █████╗      ██████╔╝ ╚████╔╝ █████╗  
            ██╔══██╗  ╚██╔╝  ██╔══╝      ██╔══██╗  ╚██╔╝  ██╔══╝  
            ██████╔╝   ██║   ███████╗    ██████╔╝   ██║   ███████╗
            ╚═════╝    ╚═╝   ╚══════╝    ╚═════╝    ╚═╝   ╚══════╝
            """)
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

        elif valor == 5:
            os.system("cls")
            print("Solicitando datos de libros ...\n")
            Libro.list_all()
            idlibro=input("Ingrese el ID del libro que quiere editar STOCK : ")
            stock=input("Ingrese cantidad real de STOCK : ")
            libro=Libro("","","","","",idlibro,stock)
            libro.cantidad(idlibro)
            print("Libro guardado exitosamente! \n")

        else:
            print("No se reconoce el comando ... :s")
            Menu.__init__()

    def musuario():
        while True:
            os.system('cls')
            print("""
            ======================MENU=USUARIO===================
            | 1.-Comprar Libros       2.-Ver Carrito de Compras |
            =====================================================
            """)
            op=input("Ingrese una opcion: ")
            if op=="1":
                os.system('cls')
                Libro.list_all()
                idlibro=input("Ingrese el ID del libro que quiere COMPRAR : ")
                Libro.stockview(idlibro)
                
                
                input("presion ENTER para continuar...")

            elif op == "2":
                pass


    def menu0():
        print("""
         ███████████   ███                                                       ███      █████                          ██████████ █████                       █████             
        ░░███░░░░░███ ░░░                                                       ░░░      ░░███                          ░░███░░░░░█░░███                       ░░███              
         ░███    ░███ ████   ██████  ████████   █████ █████  ██████  ████████   ████   ███████   ██████      ██████      ░███  █ ░  ░███████   ██████   ██████  ░███ █████  █████ 
         ░██████████ ░░███  ███░░███░░███░░███ ░░███ ░░███  ███░░███░░███░░███ ░░███  ███░░███  ███░░███    ░░░░░███     ░██████    ░███░░███ ███░░███ ███░░███ ░███░░███  ███░░  
         ░███░░░░░███ ░███ ░███████  ░███ ░███  ░███  ░███ ░███████  ░███ ░███  ░███ ░███ ░███ ░███ ░███     ███████     ░███░░█    ░███ ░███░███ ░███░███ ░███ ░██████░  ░░█████ 
         ░███    ░███ ░███ ░███░░░   ░███ ░███  ░░███ ███  ░███░░░   ░███ ░███  ░███ ░███ ░███ ░███ ░███    ███░░███     ░███ ░   █ ░███ ░███░███ ░███░███ ░███ ░███░░███  ░░░░███
         ███████████  █████░░██████  ████ █████  ░░█████   ░░██████  ████ █████ █████░░████████░░██████    ░░████████    ██████████ ████████ ░░██████ ░░██████  ████ █████ ██████ 
        ░░░░░░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░░░     ░░░░░░  ░░░░ ░░░░░ ░░░░░  ░░░░░░░░  ░░░░░░      ░░░░░░░░    ░░░░░░░░░░ ░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░ ░░░░░ ░░░░░░  
        
        
        ================MENU=PRINCIPAL==================
        | 1.-Usuario Comprador    2.-Administrador     |
        ================================================
        """)
        op=input("Seleccione una opcion: ")
        if op == "1":
            os.system('cls')
            login.Login.contraseña = "Isabellabascu1409"
            Menu.musuario()
        elif op == "2":
            login.Login.contraseña=getpass("Ingrese contraseña de SQL: ")
            if login.Login.contraseña == "Isabellabascu1409":
                login.Login.menuadmin=True
                while login.Login.menuadmin:
                    Menu.__init__()
                    input("presione ENTER para continuar...")
                

            else:
                print("ERROR de contraseña...")
            
            
        else:
            print("ERROR seleccione 1 o 2 solamente...")

            
while login.Login.menu0:
    os.system("cls")
    Menu.menu0()
    input("presione ENTER para continuar......")
