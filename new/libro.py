from conexion import Conexion

class Libro:

    def __init__(self, codigo,nombre,autor,fecha_pub,precio,idlibro,stock):
        self.idlibro=idlibro
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.fecha_pub = fecha_pub
        self.precio = precio
        self.stock=stock
    
    def insertar(self):
        sql = f'INSERT INTO libros (codigo,nombre,autor,fecha_pub,precio,stock) VALUES ({self.codigo},"{self.nombre}","{self.autor}","{self.fecha_pub}",{self.precio},{self.stock})'
        db = Conexion()
        db.ieb(sql)

    def insertarusuario(nomusuario):
        sql = f'INSERT INTO usuarios (nombre) VALUES ("{nomusuario}")'
        db = Conexion()
        db.ieb(sql)

    def insertcarro1(idlibro):
        sql = f'INSERT INTO carrito (codigo, nombre, autor, fecha_pub, precio) SELECT codigo, nombre, autor, fecha_pub, precio FROM libros WHERE id = {idlibro};'
        db = Conexion()
        db.ieb(sql)

    def insertcarro2(idlibro):
        sql = f'UPDATE libros SET stock = stock - 1 WHERE id = {idlibro};'
        db = Conexion()
        db.ieb(sql)

    def editar(self):
        sql = f'UPDATE `biblioteca`.`libros`SET`id` = {self.idlibro},`codigo` = {self.codigo},`nombre` = "{self.nombre}",`autor` = "{self.autor}",`fecha_pub` = "{self.fecha_pub}",`precio` = {self.precio},`stock` = {self.stock} WHERE `id` = {self.idlibro};'
        db = Conexion()
        db.ieb(sql)

    def borrar(idlibro):
        sql = f'DELETE FROM `biblioteca`.`libros`WHERE `id` = {idlibro};'
        db = Conexion()
        db.ieb(sql)

    def borrarcarro():
        sql = f'DELETE FROM carrito'
        db = Conexion()
        db.ieb(sql)

    def list_all():
        db = Conexion()
        sql = "SELECT * FROM libros;"
        db.list(sql)

    def list_carrito():
        db = Conexion()
        sql = "SELECT * FROM carrito;"
        db.listcarrito(sql)

    def list_id():
        db = Conexion()
        sql = "SELECT idUsuarios FROM usuarios;"
        db.listid(sql)
    
    def cantidad(self,idlibro):
        sql = f'UPDATE `biblioteca`.`libros` SET `stock` = "{self.stock}" WHERE ( `id` = {idlibro} ) ;'
        db = Conexion()
        db.ieb(sql)

    def stockview(idlibro):
        sql = f'SELECT stock FROM biblioteca.libros WHERE id = {idlibro};'
        db = Conexion()
        db.liststock(sql)
    
    