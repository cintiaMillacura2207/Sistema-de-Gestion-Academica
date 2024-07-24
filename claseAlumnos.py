from tkinter import messagebox
from conexion import conexionDB

class Alumnos():  
     #CONSTRUCTOR QUE INICIALIZA LOS ATRIBUTOS 
    def __init__(self,id=0,nombre="",domicilio="",dni=0,edad=0):
        self.id=id
        self.nombre=nombre
        self.domicilio=domicilio
        self.dni=dni
        self.edad=edad

    #DEFINICION DE METODOS
    
    #METODO QUE RECIBE LOS DATOS Y LOS INSERTA EN LA TABLA
    def Agregar(self):
        conexDB=conexionDB()
        #Se escribe dentro de una variable sql la instruccion con los campos y sus respectivos values
        sql="insert into alumnos(Nombre,Domicilio,Dni,Edad) values ('%s','%s',%s,%s)"
        conexDB.cursor.execute(sql %(self.nombre,self.domicilio,self.dni,self.edad))
        conexDB.con.commit
        messagebox.showinfo('Agregar','Nuevo alumno ingresado!!')
        conexDB.cerrar()

    #METODO QUE BUSCA LOS DATOS Y LOS DEVUELVE
    def listaAlumnos():
        conexDB=conexionDB()
        sql='select * from Alumnos order by id desc'
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos
    
    #METODO QUE PERMITE MODIFICAR LOS DATOS DE UN ALUMNO
    def Modificar(self):
        conexDB=conexionDB()
        sql="update alumnos set Nombre='%s',Domicilio='%s',Dni=%s ,Edad=%s where id=%s"
        conexDB.cursor.execute(sql %(self.nombre,self.domicilio,self.dni,self.edad,self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar','Datos de alumno Modificados!!')
        conexDB.cerrar()

    #METODO QUE PERMITE ELIMINAR UN ALUMNO
    def Eliminar(self):
        conexDB=conexionDB()
        sql="delete from alumnos where id=%s"
        # Manejo de excepciones
        try:
            conexDB.cursor.execute(sql %self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar','Alumno Eliminado!!')
        except:
            messagebox.showerror('Eliminar','No se ha seleccionado ningun Alumno!!')
       

    #METODO QUE PERMITE REALIZAR UNA BUSQUEDA FINA DE ALUMNOS
    def BuscarAlumnos(self):
        conexDB=conexionDB()
        Texto=self.nombre.strip()+"%"
        sql="select * from alumnos where Nombre like '%s' order by Nombre " %Texto
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos
