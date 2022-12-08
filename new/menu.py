from libro import Libro
import os
import login
from getpass import getpass
from conexion import Conexion


class Menu:
    
    def __init__():
        os.system('cls')
        print("""
        ===============MENU==ADMINISTRADOR===============
        | 1.-Listar Libros        2.-Agregar Libro      |
        | 3.-Editar Libro         4.-Borrar Libro       |
        | 0.-Salir                                      |
        =================================================
        
        """)
        

        valor = int(input("Ingresa una opcion...\n"))

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
            stock = int(input("Ingrese el stock del libro "))
            libro=Libro(codigo,nombre,autor,fecha_pub,precio,"",stock)
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
            stock = int(input("Ingrese el stock del libro "))
            libro=Libro(codigo,nombre,autor,fecha_pub,precio,idlibro,stock)
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
            ======================MENU=USUARIO====================================================
            | 1.-Comprar Libros       2.-Ver Carrito de Compras     3.-Borrar Carrito    4.-Salir|
            ======================================================================================
            """)
            op=input("Ingrese una opcion: ")
            if op=="1":
                os.system('cls')
                Libro.list_all()
                idlibro=input("Ingrese el ID del libro que quiere COMPRAR : ")
                Libro.stockview(idlibro)
                stocks=login.Login.stock
                
                if stocks <= 0:
                    print("No queda suficiente stock de ese libro...")
                else:
                    Libro.insertcarro1(idlibro)
                    Libro.insertcarro2(idlibro)               
                    print("Libro agregado correctamente al carrito")
                input("presion ENTER para continuar...")

            elif op == "2":
                os.system("cls")
                Libro.list_carrito()
                input("presione ENTER para continuar...")

            elif op == "3":
                os.system("cls")
                Libro.borrarcarro()
                input("Carrito borrado presione ENTER para continuar...")

            elif op == "4":
                os.system("cls")
                os._exit()


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
            nombreusu=input("Ingrese su nombre de Usuario: ")
            Libro.insertarusuario(nombreusu)
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
