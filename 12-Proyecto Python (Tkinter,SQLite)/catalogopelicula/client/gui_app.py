import tkinter as tk
from tkinter import ttk

def barraMenu(root):
    barraMenu = tk.Menu(root)
    root.config(menu = barraMenu, width = 300, height = 300)

    #creamos el inicio en la barra de menu
    mInicio = tk.Menu(barraMenu, tearoff=0)
    barraMenu.add_cascade(label= 'Inicio', menu = mInicio)

    #creamos submenus
    mInicio.add_command(label= 'Crear Registro')
    mInicio.add_command(label= 'Eliminar')
    mInicio.add_command(label= 'Salir',command= root.destroy)

    barraMenu.add_cascade(label= 'Consultas')
    barraMenu.add_cascade(label= 'Configuracion')
    barraMenu.add_cascade(label= 'Ayuda')


class Frame(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root,width = 480, height = 320)
        self.root = root
        self.pack()
        #self.config(bg = 'white')

        self.camposPeliculas()
        self.deshabilitarCampos()
        self.tablaPeliculas()

    def camposPeliculas(self):
        #labels de cada campo
        self.label_Nombre = tk.Label(self, text = 'Nombre: ')
        self.label_Nombre.config(font = ('Calibri', 12, 'bold'))
        self.label_Nombre.grid(row = 0, column = 0)

        self.duracion = tk.Label(self, text = 'Duracion: ')
        self.duracion.config(font = ('Calibri', 12, 'bold'))
        self.duracion.grid(row = 1, column = 0)

        self.genero = tk.Label(self, text = 'Genero: ')
        self.genero.config(font = ('Calibri', 12, 'bold'))
        self.genero.grid(row = 2, column = 0)

        #entrys de cada campo
        #Nombre
        self.nombrePelicula = tk.StringVar()
        self.entryNombre = tk.Entry(self,textvariable=self.nombrePelicula)
        self.entryNombre.config(width = 50,font = ('Calibri', 12) )
        self.entryNombre.grid(row = 0 , column = 1, padx=10, pady=10, columnspan=2)
        #Duracion
        self.duracionPelicula = tk.StringVar()
        self.entryDuracion = tk.Entry(self, textvariable=self.duracionPelicula)
        self.entryDuracion.config(width = 50,font = ('Calibri', 12))
        self.entryDuracion.grid(row = 1 , column = 1, padx=10, pady=10, columnspan=2)
        #Genero
        self.generoPelicula = tk.StringVar()
        self.entryGenero = tk.Entry(self, textvariable=self.generoPelicula)
        self.entryGenero.config(width = 50,font = ('Calibri', 12))
        self.entryGenero.grid(row = 2 , column = 1, padx=10, pady=10, columnspan=2)


        #BOTONES

        #boton para agregar nuevas peliculas
        self.botonAgregar = tk.Button(self, text = 'Agregar', command = self.habilitarCampos)
        self.botonAgregar.config(width=20,font = ('Calibri', 12, 'bold'), fg = '#DAD5D6', bg = '#158645', cursor = 'hand2', activebackground='#35BD6F')
        self.botonAgregar.grid(row = 3,column = 0, padx=10, pady=10)


        #boton para guardar nuevas peliculas
        self.botonGuardar = tk.Button(self, text = 'Guardar', command=self.guardarDatos)
        self.botonGuardar.config(width=20,font = ('Calibri', 12, 'bold'), fg = '#DAD5D6', bg = '#1658A2', cursor = 'hand2', activebackground='#3586DF')
        self.botonGuardar.grid(row = 3,column = 1, padx=10, pady=10)
        

        #boton para cancelar nuevas peliculas
        self.botonCancelar = tk.Button(self, text = 'Cancelar', command=self.deshabilitarCampos)
        self.botonCancelar.config(width=20,font = ('Calibri', 12, 'bold'), fg = '#DAD5D6', bg = '#BD152E', cursor = 'hand2', activebackground='#E15370')
        self.botonCancelar.grid(row = 3,column = 2, padx=10, pady=10)
        

    #Habilitar Campos
    def habilitarCampos(self):
        #Enviamos campos vacios cuando cancelamos por ej...
        self.nombrePelicula.set('')
        self.duracionPelicula.set('')
        self.generoPelicula.set('')

        #seteamos todos los campos como estado normales.
        self.entryNombre.config(state='normal')
        self.entryDuracion.config(state='normal')
        self.entryGenero.config(state='normal')
        
        #seteamos botones como estado normal
        self.botonGuardar.config(state='normal')
        self.botonCancelar.config(state='normal')
    #Deshabilitar campos
    def deshabilitarCampos(self):
        #Enviamos campos vacios cuando cancelamos por ej...
        self.nombrePelicula.set('')
        self.duracionPelicula.set('')
        self.generoPelicula.set('')

        #seteamos todos los campos como deshabilitados.
        self.entryNombre.config(state='disabled')
        self.entryDuracion.config(state='disabled')
        self.entryGenero.config(state='disabled')

        #seteamos botones como deshabilitados
        self.botonGuardar.config(state='disabled')
        self.botonCancelar.config(state='disabled')

    def guardarDatos(self):
        self.deshabilitarCampos()
            

    def tablaPeliculas(self):
        self.tabla = ttk.Treeview(self, column = ('Nombre','Duracion','Genero'))
        self.tabla.grid(row=4,column=0,columnspan=4)

        self.tabla.heading('#0',text = 'ID')
        self.tabla.heading('#1',text = 'Nombre')
        self.tabla.heading('#2',text = 'Duracion')
        self.tabla.heading('#3',text = 'Genero')


        self.tabla.insert('',0,text='1',values = ('Los Vengadores','2.35','Accion'))


        #BOTONES ELIMINAR EDITAR
         #boton para agregar nuevas peliculas
        
        self.botonEditar = tk.Button(self, text = 'Editar')
        self.botonEditar.config(width=20,font = ('Calibri', 12, 'bold'), fg = '#DAD5D6', bg = '#158645', cursor = 'hand2', activebackground='#35BD6F')
        self.botonEditar.grid(row = 5,column = 0, padx=10, pady=10)
        
        self.botonEliminar = tk.Button(self, text = 'Eliminar')
        self.botonEliminar.config(width=20,font = ('Calibri', 12, 'bold'), fg = '#DAD5D6', bg = '#BD152E', cursor = 'hand2', activebackground='#E15370')
        self.botonEliminar.grid(row = 5,column = 1, padx=10, pady=10)