from tkinter import messagebox
from conexion import conexionDB

class Docentes():
    #CONSTRUCTOR QUE INICIALIZA LOS ATRIBUTOS    
    def __init__(self,id=0,nombre="",domicilio="",dni=0,categoria=0,antiguedad=0,sueldo=0):
        self.id=id
        self.nombre=nombre
        self.domicilio=domicilio
        self.dni=dni
        self.categoria=categoria
        self.antiguedad=antiguedad
        self.sueldo=sueldo

    # DEFINICION DE METODOS
    
    #METODO QUE RECIBE LOS DATOS Y LOS INSERTA EN LA TABLA
    def Agregar(self):
        conexDB=conexionDB()
        sql="insert into docentes(Nombre,Domicilio,dni,categoria,antiguedad,sueldo) values ('%s','%s',%s,%s,%s,%s)"
        conexDB.cursor.execute(sql %(self.nombre,self.domicilio,self.dni,self.categoria,self.antiguedad,self.sueldo))
        conexDB.con.commit
        messagebox.showinfo('Agregar','Nuevo docente ingresado!!')
        conexDB.cerrar()

 
    #METODO QUE BUSCA LOS DATOS Y LOS DEVUELVE
    def listaDocentes():
        conexDB=conexionDB()
        sql='select * from Docentes order by id desc'
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos

    #METODO QUE PERMITE MODIFICAR LOS DATOS DE UN DOCENTE
    def Modificar(self):
        conexDB=conexionDB()
        sql="update docentes set Nombre='%s',Domicilio='%s',Dni=%s ,Categoria=%s,Antiguedad=%s,Sueldo=%s where id=%s"
        conexDB.cursor.execute(sql %(self.nombre,self.domicilio,self.dni,self.categoria,self.antiguedad,self.sueldo,self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar','Datos de Docente Modificados!!')
        conexDB.cerrar()

    #METODO QUE PERMITE ELIMINAR UN DOCENTE
    def Eliminar(self):
        conexDB=conexionDB()
        sql="delete from docentes where id=%s"
        try:
            conexDB.cursor.execute(sql %self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar','Docente Eliminado!!')
        except:
            messagebox.showerror('Eliminar','No se ha seleccionado ningun Docente!!')


    #METODO QUE PERMITE REALIZAR UNA BUSQUEDA FINA DE ALUMNOS
    def BuscarDocentes(self):
        conexDB=conexionDB()
        Texto=self.nombre.strip()+"%"
        sql="select * from docentes where Nombre like '%s' order by Nombre " %Texto
        conexDB.cursor.execute(sql)
        datos=conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos       