from conexion import Conexion

class Libro:

    def __init__(self, codigo,nombre,autor,fecha_pub,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.fecha_pub = fecha_pub
        self.precio = precio
    
    def insertar(self):
        sql = f'INSERT INTO libros (codigo,nombre,autor,fecha_pub,precio) VALUES ({self.codigo},{self.nombre},{self.autor},{self.fecha_pub},{self.precio})'
        db = Conexion()
        db.insert(sql)

    def list_all():
        db = Conexion()
        sql = "SELECT * FROM libros;"
        db.list(sql)
    
    def get_libro():
        db = Conexion()
        db.getById()

