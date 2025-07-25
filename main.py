import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont

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
        )
    )
    textbox.delete("1.0", "end")
    with open(filename, "r") as archivo:
        content = archivo.read()
    textbox.insert("1.0", content)
    fileVar.set(filename)
def guardar_archivo(event=None):
    content = textbox.get("1.0", "end-1c")
    filename = filedialog.asksaveasfilename()
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

#Frame
framee = tk.Frame(root)
framee.pack(fill="both", expand=True)
framee.columnconfigure(1, weight=1)
framee.rowconfigure(0, weight=1)

#TextBox
#Dark theme ---> textbox = tk.Text(root, foreground="white", insertbackground="white", background="black")
textbox = tk.Text(framee, font=custom_font, bd=0)
textbox.grid(column=1, row=0, sticky="NSWE")

#Bottombar  
bottom_bar = tk.Frame(root, height=20, bg="gray")
bottom_bar.pack(fill="x")
bottom_bar.pack_propagate(False)
file = tk.Label(bottom_bar,textvariable=fileVar, font=custom_font, bg="gray")
file.grid(column=0, row=0)
line = tk.Label(bottom_bar, font=custom_font, bg="gray", foreground="black")
line.grid(column=1, row=0, padx=20)

currentLine = textbox.index(tk.END)
currentLine = bool(currentLine)
currentLine = round(currentLine)

#Line tracker
lineTracker = tk.Text(framee, width=4, bd=0, font=custom_font, bg="#E6E6E6")
lineTracker.grid(column=0, row=0, sticky="NS")
lineTracker.tag_config("alinear", justify="right")

def get_linePos():
    linePos = int(textbox.index("end-1c").split(".")[0])
    lineTracker.delete("1.0", "end-1c")
    for i in range(linePos):
        x = str(i+1)
        lineTracker.insert("end", x + "\n", "alinear")
    root.after(100, get_linePos)
def get_cursorPos():
    cursorPos = textbox.index(tk.INSERT).split(".")
    currentLine = "Linea " + cursorPos[0]
    line.config(text=currentLine)
    root.after(100, get_cursorPos)
root.after(100, get_linePos)
root.after(100, get_cursorPos)

root.mainloop() 