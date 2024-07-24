import sqlite3

# CREA LA BASE DE DATOS
miConexion=sqlite3.connect("Carpeta\Nombre_BD")
miCursor=miConexion.cursor()

# CREA LA TABLA ALUMNOS CON LOS CAMPOS CORRESPONDIENTES
miCursor.execute("""CREATE TABLE ALUMNOS (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                DOMICILIO VARCHAR(50),
                DNI INTEGER,
                EDAD INTEGER)""")

# CREA LA TABLA DOCENTES CON LOS CAMPOS CORRESPONDIENTES
miCursor.execute("""CREATE TABLE DOCENTES (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                DOMICILIO VARCHAR(50),
                DNI INTEGER,
                CATEGORIA INTEGER,
                ANTIGUEDAD INTEGER,
                SUELDO INTEGER)""")

# CIERRA LA CONEXION
miConexion.close()