from Movie import Movie
import os

class Menu:

    def __init__():

        print("Seleccione una opcion ...")
        print("1 para listar las peliculas.. ")
        print("2 para agregar pelicula")
        print("0 para salir del sistema")

        valor = int(input("...\n"))

        if valor == 0:
            print("Adios ...")
        elif valor == 1:
            os.system('clear')
            print("Listando peliculas")
            Movie.list_all()
            Menu.post_listar_peliculas()
            
        elif valor == 2:
            print("Solicitando datos de pelicula ...\n")
            title = input("Ingrese titulo de la pelicula ")
            movie = Movie(title)
            movie.save()
            print("Pelicula guardada exitosamente! \n")
        else:
            print("No se reconoce el comando ... :s")
            Menu.__init()
    
    def post_listar_peliculas():
        print("Ingrese el id de la pelicula a modificar")
        print("Ingrese 0 para salir de la app")
        value = input("\n")
        if value == 0:
            print("Adios..")
        else:
            print(f'se va a modificar la pelicula con id {value}...')
            

Menu.__init__()

