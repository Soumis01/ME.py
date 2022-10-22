from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

print(os.getcwd())

# La orden de que se descargue el video en alta resolucion
def accion():
    enlace=videos.get()     
    video = YouTube(enlace)  
    descarga = video.streams.get_highest_resolution()
    descarga.download()

# Este despliega la ventana de informacion del autor
def popup():
    MessageBox.showinfo("Sobre mí","Enlace a mi perfil de Github: https://github.com/Soumis01\n")

# Creamos y nombramos la ventana 
root = Tk()
root.config(bd=8)
root.title("By Jade Magallnes")

# Ponemos una imagen en un widget
imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

# Hacemos un widget de tipo menu
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Para más información", menu=helpmenu)
helpmenu.add_command(label="Información del autor",command=popup)

# Salir del programa
menubar.add_command(label="Salir", command=root.destroy)

# Instrucciones para el usuario 
instrucciones = Label(root, text="Programa creado en Python para descargar vídeos de Youtube\n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

# Widget tipo boton para activar el programa
boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()