## 3OLIDTS-RodrigoNandayapa-04
## Formulario de registro almacenamiento en TXT sin validacion
import tkinter as tk
from tkinter import messagebox

### Definicion de funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_fun():
    limpiar_campos()

def guardar_valores():
    # Obtener valores desde los entrys
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    # Obtener el genero de los RadioButtons
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    # Generar la cadena de caracteres
    datos = ("Nombres: " + nombres + "\n" +
             "Apellidos: " + apellidos + "\n" +
             "Edad: " + edad + " anios\n" +
             "Estatura: " + estatura + "\n" +
             "Telefonos: " + telefono + "\n" +
             "Genero: " + genero)

    # Guardar los datos en el archivo TXT
    with open("302024Datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")

    # Mostrar mensaje de confirmacion
    messagebox.showinfo("Informacion", "Datos guardados con exito:\n\n" + datos)
    limpiar_campos()

### Creacion de Ventana
ventana = tk.Tk()
ventana.geometry("520x580")
ventana.title("Formulario V0.01")

# Crear variable para el RadioButton
var_genero = tk.IntVar()
var_genero.set(0)

# Creacion de etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text="Nombres :")
tbNombre = tk.Entry(ventana)
lbNombre.pack()
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos :")
tbApellidos = tk.Entry(ventana)
lbApellidos.pack()
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono :")
tbTelefono = tk.Entry(ventana)
lbTelefono.pack()
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad :")
tbEdad = tk.Entry(ventana)
lbEdad.pack()
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura :")
tbEstatura = tk.Entry(ventana)
lbEstatura.pack()
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Genero")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbHombre.pack()
rbMujer.pack()

### Creacion de Botones
btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnBorrar.pack()
btnGuardar.pack()

### Ejecucion de ventana
ventana.mainloop()