import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont
import os

#Window config
root = tk.Tk(className="tkint")
root.title("Editor de texto")
root.geometry("800x700")
fileVar = tk.StringVar()
fileVar.set("Untitled")

custom_font = tkfont.Font(family="Fixedsys Excelsior 3.01", size=12)

#Functions
def nuevo_archivo(event=None):
    textbox.delete("1.0", "end")
    fileVar.set("Untitled")
def abrir_archivo(event=None):
    filename = filedialog.askopenfilename(
        filetypes=(
            ("Archivos de texto", "*.txt"),
            ("Archivos de Python", "*.py"),
            ("Todos lo archivos", "*.*")
        ),
        initialdir="~/Dev/Pruebas/"
    )
    textbox.delete("1.0", "end")
    with open(filename, "r") as archivo:
        content = archivo.read()
    textbox.insert("1.0", content)
    fileVar.set(filename)
def guardar_archivo(event=None):
    content = textbox.get("1.0", "end-1c")
    filename = filedialog.asksaveasfilename(
        initialdir="~/Dev/Pruebas/"
    )
    with open(filename, "w") as archivo:
        archivo.write(content)
def salir(event=None):
    root.destroy()

#Binds
root.bind_all("<Control-o>", nuevo_archivo)
root.bind_all("<Control-p>", abrir_archivo)
root.bind_all("<Control-s>", guardar_archivo)
root.bind_all("<Control-x>", salir)

#Menubar
barra_menu = tk.Menu()
menu_archivo = tk.Menu(barra_menu, tearoff=False)
menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+O", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", accelerator="Ctrl+P", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", accelerator="Ctrl+S", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", accelerator="Ctrl+X", command=salir)
barra_menu.add_cascade(menu=menu_archivo, label="Archivo")
root.config(menu=barra_menu)

#TextBox
#Dark theme ---> textbox = tk.Text(root, foreground="white", insertbackground="white", background="black")
textbox = tk.Text(root, font=custom_font)
textbox.pack(fill="both", expand=True)

#Bottombar  
bottom_bar = tk.Frame(root, height=20, bg="gray")
bottom_bar.pack(fill="x")
bottom_bar.pack_propagate(False)
file = tk.Label(bottom_bar,textvariable=fileVar, font=custom_font, bg="gray")
file.grid(column=0, row=0)

root.mainloop() 