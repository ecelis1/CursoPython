import tkinter as tk
from client.gui_app import Frame,barraMenu
def main():
    root = tk.Tk()

    root.title('Catalogo de Peliculas')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(0,0)
    
    barraMenu(root)

    #frame, es un contenedor, es un contenedor de los elementos que le vamos a agregar a nuestra ventana.

    #creamos el objeto y se va a empaquetar a la ventana root que es mi ventana principal
    app = Frame(root = root)
    
    app.mainloop()

if __name__ == '__main__':
    main()