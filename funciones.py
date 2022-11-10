def listarLibros(libros):
    print("\nLibros: \n")
    contador = 1
    for cur in libros:
        datos = "{0}. Código: {1} | Nombre: {2} ({3} Precio:)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese código: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Código incorrecto: Debe tener 6 dígitos.")

    nombre = input("Ingrese nombre: ")

    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese precio: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("el precio debe ser mayor a 0.")
        else:
            print("precio incorrecto: Debe ser un número.")

    libro = (codigo, nombre, creditos)
    return libro

def pedirDatosActualizacion(libros):
    listarLibros(libros)
    existeCodigo = False
    codigoEditar = input("Ingrese el código del libro a editar: ")
    for cur in libros:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre a modificar: ")

        creditosCorrecto = False
        while(not creditosCorrecto):
            creditos = input("Ingrese precio a modificar: ")
            if creditos.isnumeric():
                if (int(creditos) > 0):
                    creditosCorrecto = True
                    creditos = int(creditos)
                else:
                    print("Los precios deben ser mayor a 0.")
            else:
                print("Precio incorrecto: Debe ser un número.")

        libro = (codigoEditar, nombre, creditos)
    else:
        libro = None

    return libro


def pedirDatosEliminacion(libros):
    listarLibros(libros)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del libro a eliminar: ")
    for cur in libros:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar
