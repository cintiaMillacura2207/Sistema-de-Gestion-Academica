from tkinter import*
from tkinter import messagebox, ttk  
from claseDocentes import Docentes

class guiDocentesCons(Frame):
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, root=None):
        super().__init__(root)
        self.root=root
        self.pack()  
        global Nombre
        Nombre=StringVar()
        self.gui() 

    def gui(self):
        #PRINCIPAL FUNCION DE ESTA CLASE CON EL CONTENIDO DE LA GUI REFERIDO A LA INTERFAZ
        self.config(bg="dodger blue", width="950", height="500")
        self.tituloMarco=Label(self,text="CONSULTA DE DOCENTES")
        self.tituloMarco.grid(row=0,column=0,columnspan=3,pady=10,padx=10)
        self.tituloMarco.config(bg="lightgray",width=40,font=("Arial",12,"bold"),anchor="center")

        #LABEL INGRESO DE DATOS
        self.lab1=Label(self, text="Ingrese Nombre a buscar: ")
        self.lab1.grid(row=1,column=0, sticky="", pady=3, padx=10)
        self.lab1.config(bg="lightgray",width=20,font=("Arial",12,"bold"),anchor="w")

        #ENTRY O CUADROS DE TEXTO
        self.txtNom=Entry(self,textvariable=Nombre)
        self.txtNom.grid(row=1,column=1,columnspan=2,sticky="w",pady=3,padx=10)
        self.txtNom.config(bg="white",width=40,font=("Arial",12),state="normal") 

        #BUTTONS
        self.botonBus=Button(self,text="Buscar",command=lambda:self.Buscar())
        self.botonBus.grid(row=2,column=0,pady=10,padx=10)
        self.botonBus.config(bg="DodgerBlue2",fg="white",width=20, font=("Arial",12),cursor='hand2')
        self.botonSal=Button(self,text="Salir",command=lambda:self.Salir())
        self.botonSal.grid(row=2,column=1,columnspan=2,pady=10,padx=10)
        self.botonSal.config(bg="purple1",fg="white",width=40, font=("Arial",12),cursor='hand2')

        # CREAR/DEFINIR TREEVIEW Y CANTIDAD DE COLUMNAS DE TREEVIEW
        self.Tv=ttk.Treeview(self,columns=('NomApe','Dom','Dni','Categ','Ant','Sue'))
        self.Tv.grid(row=3,column=0,columnspan=3,sticky='w')
        self.scroll=ttk.Scrollbar(self,orient='vertical',command=self.Tv.yview)
        self.scroll.grid(row=3,column=2,sticky='nse')
        self.Tv.configure(yscrollcommand=self.scroll.set)

        # DEFINIR NOMBRES DE COLUMNA
        self.Tv.heading('#0',text='ID')
        self.Tv.column('#0',width=50)
        self.Tv.heading('#1',text='Nombre y Apellido')
        self.Tv.column('#1',width=150)
        self.Tv.heading('#2',text='Domicilio')
        self.Tv.column('#2',width=150)
        self.Tv.heading('#3',text='Dni')
        self.Tv.column('#3',width=150)
        self.Tv.heading('#4',text='Categoria')
        self.Tv.column('#4',width=70)
        self.Tv.heading('#5',text='Antiguedad')
        self.Tv.column('#5',width=70)
        self.Tv.heading('#6',text='Sueldo')
        self.Tv.column('#6',width=100)
        self.llenar_tv()
        self.txtNom.focus()


        #FUNCIONES PARA BUTTONS
    def Buscar(self):
        self.vaciar_tv()
        miDocente=Docentes(nombre=Nombre.get())
        datos=miDocente.BuscarDocentes()
        for d in  datos:
            self.Tv.insert('',0,text=d[0],values=(d[1],d[2],d[3],d[4],d[5],d[6]))

    def vaciar_tv(self):
        # FUNCION QUE LIMPIA LA GRILLA ANTES DE PONERLE LOS DATOS
        filas=self.Tv.get_children()   
        for f in filas:
            self.Tv.delete(f)


    def llenar_tv(self):
        # FUNCION QUE PONE LOS DATOS DE LA TABLA ALUMNOS EN LA GRILLA
        self.vaciar_tv() #SE VACIA EL TREEVIEW
        datos=Docentes.listaDocentes()
        for d in datos:
            self.Tv.insert('',0,text=d[0],values=(d[1],d[2],d[3],d[4],d[5],d[6]))

    def Salir(self):
        #FUNCION ASOCIADA AL BOTON SALIR
        respuesta=messagebox.askquestion("Salir","Confirma que desea salir del programa?")
        if respuesta=="yes":
            self.root.destroy() 

