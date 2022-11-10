from BD.conexion import DAO
import funciones


def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar Libros")
            print("2.- Registrar Libro")
            print("3.- Actualizar Libro")
            print("4.- Eliminar Libro")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            libros = dao.listarLibros()
            if len(libros) > 0:
                funciones.listarLibros(libros)
            else:
                print("No se encontraron libros...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarLibro(curso)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            libros = dao.listarLibros()
            if len(libros) > 0:
                curso = funciones.pedirDatosActualizacion(libros)
                if curso:
                    dao.actualizarLibro(curso)
                else:
                    print("Código de libro a actualizar no encontrado...\n")
            else:
                print("No se encontraron libros...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            libros = dao.listarLibros()
            if len(libros) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(libros)
                if not(codigoEliminar == ""):
                    dao.eliminarLibro(codigoEliminar)
                else:
                    print("Código de libro no encontrado...\n")
            else:
                print("No se encontraron libros...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


menuPrincipal()
