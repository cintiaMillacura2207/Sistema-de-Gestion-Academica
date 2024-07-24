from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from claseDocentes import Docentes

class guiDocentes(Frame):
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, root=None):
        super().__init__(root)
        self.root=root
        self.pack()  
        global Nombre, Domicilio, Dni, Categoria, Antiguedad, Sueldo
        Nombre=StringVar()
        Domicilio=StringVar()
        Dni=IntVar()
        Categoria=IntVar()
        Antiguedad=IntVar()
        Sueldo=IntVar()
        self.gui() 


    def gui(self):
        self.config(bg="dodger blue")
        #PRINCIPAL FUNCION DE ESTA CLASE CON EL CONTENIDO DE LA GUI REFERIDO A LA INTERFAZ
        self.tituloMarco=Label(self,text="CARGA DE DOCENTES")
        self.tituloMarco.grid(row=0,column=0,columnspan=3,pady=10,padx=10)
        self.tituloMarco.config(bg="lightgray",width=40,font=("Arial",12,"bold"),anchor="center")

        #LABELS INGRESO DE DATOS
        self.lab1=Label(self, text="Nombre: ")
        self.lab1.grid(row=1,column=0, sticky="", pady=3, padx=10)
        self.lab1.config(bg="lightgray",width=15,font=("Arial",12,"bold"),anchor="w")
        self.lab2=Label(self, text="Domicilio: ")
        self.lab2.grid(row=2,column=0,pady=3, padx=10)
        self.lab2.config(bg="lightgray",width=15,font=("Arial",12,"bold"),anchor="w")
        self.lab3=Label(self, text="DNI: ")
        self.lab3.grid(row=3,column=0,pady=3, padx=10)
        self.lab3.config(bg="lightgray",width=15,font=("Arial",12,"bold"),anchor="w")
        self.lab4=Label(self, text="Categoria: ")
        self.lab4.grid(row=4,column=0, pady=3, padx=10)
        self.lab4.config(bg="lightgray",width=15,font=("Arial",12,"bold"),anchor="w")
        self.lab5=Label(self, text="Antiguedad: ")
        self.lab5.grid(row=5,column=0, pady=3, padx=10)
        self.lab5.config(bg="lightgray",width=15,font=("Arial",12,"bold"),anchor="w")
        self.lab6=Label(self, text="Sueldo: ")
        self.lab6.grid(row=6,column=0, pady=3, padx=10)
        self.lab6.config(bg="lightgray",width=15,font=("Arial",12,"bold"),anchor="w")

        #ENTRYS O CUADROS DE TEXTO
        self.txtNom=Entry(self,textvariable=Nombre)
        self.txtNom.grid(row=1,column=1,columnspan=2,sticky="w",pady=3,padx=10)
        self.txtNom.config(bg="white",width=40,font=("Arial",12),state="disabled") 
        self.txtDom=Entry(self,textvariable=Domicilio)
        self.txtDom.grid(row=2,column=1,columnspan=2,sticky="w",pady=3,padx=10)
        self.txtDom.config(bg="white",width=40,font=("Arial",12),state="disabled")
        self.txtDni=Entry(self,textvariable=Dni)
        self.txtDni.grid(row=3,column=1,columnspan=2,sticky="w",pady=3,padx=10)
        self.txtDni.config(bg="white",width=40,font=("Arial",12),state="disabled")
        self.txtCategoria=Entry(self,textvariable=Categoria)
        self.txtCategoria.grid(row=4,column=1,columnspan=2,sticky="w",pady=3,padx=10)
        self.txtCategoria.config(bg="white",width=40,font=("Arial",12),state="disabled")
        self.txtAntiguedad=Entry(self,textvariable=Antiguedad)
        self.txtAntiguedad.grid(row=5,column=1,columnspan=2,sticky="w",pady=3,padx=10)
        self.txtAntiguedad.config(bg="white",width=40,font=("Arial",12),state="disabled")
        self.txtSueldo=Entry(self,textvariable=Sueldo)
        self.txtSueldo.grid(row=6,column=1,columnspan=2,sticky="w",pady=3,padx=10)
        self.txtSueldo.config(bg="white",width=40,font=("Arial",12),state="disabled")

        
        #BUTTONS
        self.botonNue=Button(self,text="Nuevo",command=lambda:self.Nuevo())
        self.botonNue.grid(row=7,column=0,pady=10,padx=10)
        self.botonNue.config(bg="green",fg="white",width=15, font=("Arial",12),cursor='hand2')
        self.botonConf=Button(self,text="Guardar",command=lambda:self.Guardar())
        self.botonConf.grid(row=7,column=1,pady=10,padx=10)
        self.botonConf.config(bg="blue",fg="white",width=15, font=("Arial",12),state="disabled",cursor='hand2')
        self.botonCanc=Button(self,text="Cancelar",command=lambda:self.Cancelar())
        self.botonCanc.grid(row=7,column=2,pady=10,padx=10)
        self.botonCanc.config(bg="red",fg="white",width=15, font=("Arial",12),state="disabled",cursor='hand2')
        self.botonSal=Button(self,text="Salir",command=lambda:self.Salir())
        self.botonSal.grid(row=10,column=0,columnspan=3,pady=10,padx=10)
        self.botonSal.config(bg="purple1",fg="white",width=40, font=("Arial",12,"bold"),cursor='hand2')


        # CREAR/DEFINIR TREEVIEW Y CANTIDAD DE COLUMNAS DE TREEVIEW
        self.Tv=ttk.Treeview(self,columns=('NomApe','Dom','Dni','Categ','Ant','Sue')) 
        self.Tv.grid(row=8,column=0,columnspan=4,sticky='w')
        self.scroll=ttk.Scrollbar(self,orient='vertical',command=self.Tv.yview)
        self.scroll.grid(row=8,column=4,sticky='nse')
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

        #BOTONES DEBAJO DE LA GRILLA
        self.boton_editar=Button(self, text='Editar',command=lambda:self.editar())
        self.boton_editar.config(width=20, font=('Arial',12,'bold'),
                            fg='#FFFFFF',bg='#126B14',
                            cursor='hand2', activebackground='#5EB060')
        self.boton_editar.grid(row=9,column=0, padx=10, pady=5)

        self.boton_eliminar=Button(self, text='Eliminar',command=lambda:self.eliminar())
        self.boton_eliminar.config(width=20, font=('Arial',12,'bold'),
                    fg='#FFFFFF',bg='#CA250C',
                    cursor='hand2', activebackground='#D0422C')
        self.boton_eliminar.grid(row=9,column=1, padx=10, pady=5)

        self.llenar_tv()

    #FINALIZA LO REFERIDO AL DISEÑO DE LA INTERFAZ GRAFICA
    #COMIENZA LO REFERIDO A LA FUNCIONALIDAD

    #FUNCIONES PARA BUTTONS

    def Guardar(self):
        # FUNCION ASOCIADA AL BOTON GUARDAR
        if Nombre.get()=="" or Domicilio.get()=="" or Dni.get()==0 or Categoria.get()==0 or Antiguedad.get()==0 or Sueldo.get()==0:
            messagebox.showerror("ERROR","Alguno de los datos es erroneo")
        else:
            global esNuevo
            if esNuevo==True:
                miDocente=Docentes(0,Nombre.get(),Domicilio.get(),Dni.get(),Categoria.get(),Antiguedad.get(),Sueldo.get())
                miDocente.Agregar()
                self.limpiar()
                self.estadoTextos("disabled")
                self.estadoBotones("disabled","normal","disabled")
                self.llenar_tv()
            else:
                miDocente=Docentes(self.Tv.item(self.Tv.selection())['text'],Nombre.get(),Domicilio.get(),Dni.get(),Categoria.get(),Antiguedad.get(),Sueldo.get())
                miDocente.Modificar()
                self.limpiar()
                self.estadoTextos("disabled")
                self.estadoBotones("disabled","normal","disabled")
                self.llenar_tv()


    def Nuevo(self):
        # FUNCION ASOCIADA AL BOTON NUEVO PARA INGRESAR UN REGISTRO
        global esNuevo 
        esNuevo=True
        self.limpiar()
        self.estadoTextos("normal")
        self.estadoBotones("normal","disabled","normal") 
        self.txtNom.focus()
        messagebox.showwarning("ATENCION","Esta por cargar un nuevo docente")

    def Cancelar(self):
        # FUNCION ASOCIADA AL BOTON CANCELAR
        self.limpiar()
        self.estadoTextos("disabled")
        self.estadoBotones("disabled","normal","disabled")
        messagebox.showwarning("ATENCION","Se cancela la carga")

    def editar(self):
        # FUNCION ASOCIADA AL BOTON EDITAR
        global esNuevo
        esNuevo=False
        try:
            self.limpiar()
            self.estadoTextos("normal")
            self.estadoBotones("normal","disabled","normal")
            Nombre.set(self.Tv.item(self.Tv.selection())['values'][0])
            Domicilio.set(self.Tv.item(self.Tv.selection())['values'][1])
            Dni.set(self.Tv.item(self.Tv.selection())['values'][2])
            Categoria.set(self.Tv.item(self.Tv.selection())['values'][3])
            Antiguedad.set(self.Tv.item(self.Tv.selection())['values'][4])
            Sueldo.set(self.Tv.item(self.Tv.selection())['values'][5])
            self.txtNom.focus()
        except:
            self.estadoTextos("disabled")
            self.estadoBotones("disabled","normal","disabled")
            messagebox.showerror('Editar','No se ha seleccionado ningun docente')

    def eliminar(self):
        # FUNCION ASOCIADA AL BOTON ELIMINAR
        #Se elimina docente usando el metodo de la clase y pasando el ID
        miDocente=Docentes(self.Tv.item(self.Tv.selection())['text'])
        miDocente.Eliminar()
        #Se Configuran los objetos de la GUI para continuar
        self.limpiar()
        self.estadoTextos("disabled")
        self.estadoBotones("disabled","normal","disabled")
        self.llenar_tv()  


    def limpiar(self):
        # FUNCION QUE PERMITE LIMPIAR VARIABLES PARA ENTRYS
        Nombre.set("")
        Domicilio.set("")
        Dni.set(0)
        Categoria.set(0)
        Antiguedad.set(0)
        Sueldo.set(0)

    def estadoTextos(self,estado):
        # FUNCION QUE SETEA LOS ESTADOS DE LOS ENTRYS
        self.txtNom.config(state=estado)
        self.txtDom.config(state=estado)
        self.txtDni.config(state=estado)
        self.txtCategoria.config(state=estado)
        self.txtAntiguedad.config(state=estado)
        self.txtSueldo.config(state=estado)

    def estadoBotones(self,estado1,estado2,estado3):
        # FUNCION QUE SETEA LOS ESTADOS DE LOS BOTONES GUARDAR, NUEVO, CANCELAR
        self.botonConf.config(state=estado1)
        self.botonNue.config(state=estado2)
        self.botonCanc.config(state=estado3)


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


