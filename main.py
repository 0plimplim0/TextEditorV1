import tkinter as tk
from tkinter import filedialog
import os

#Window config
root = tk.Tk(className="tkint")
root.title("Editor de texto")
root.geometry("800x700")

#Functions
def nuevo_archivo(event=None):
    print("Nuevo archivo")
def abrir_archivo(event=None):
    filename = filedialog.askopenfilename(
        filetypes=(
            ("Archivos de texto", "*.txt"),
            ("Archivos de Python", "*.py"),
            ("Todos lo archivos", "*.*")
        ),
        initialdir="~/Dev/Pruebas/"
    )
    print(filename)
    with open(filename, "r") as archivo:
        content = archivo.read()
    textbox.insert("1.0", content)
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
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#Dark theme ---> textbox = tk.Text(root, height=height, width=width, foreground="white", insertbackground="white", background="black")
textbox = tk.Text(root, height=height, width=width)
textbox.pack()

root.mainloop()