import sqlite3

class conexionDB:
    # conectar con la base de datos 
    def __init__ (self):
        self.con=sqlite3.connect("ProyectoFinal\Base")
        #crea el cursor
        self.cursor=self.con.cursor()
    
    # cierra la base de datos
    def cerrar(self):
        self.con.commit()
        self.con.close()