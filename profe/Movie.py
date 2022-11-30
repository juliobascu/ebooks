from Database import Database

class Movie:

    def __init__(self, title):
        self.title = title
    
    def save(self):
        sql = f'INSERT INTO movies (title) VALUES ("{self.title}")'
        db = Database()
        db.insert(sql)

    def list_all():
        db = Database()
        sql = "SELECT * FROM movies;"
        db.list(sql)
    
    def get_movie():
        db = Database()
        db.getById()

