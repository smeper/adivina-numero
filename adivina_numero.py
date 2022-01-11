from tkinter import *;
from tkinter import messagebox;
import random

global intentos
intentos = 0

def fin():
    exit = messagebox.askquestion("Salir", "¿Salir de la App?")

    if exit == "yes":
        window.destroy()

def generar_numero_aleatorio():
    return random.randint(1, 101)

numero_adivinar = generar_numero_aleatorio()

def jugar():

    try:
        produccion.set(str(int(produccion.get()) + 1))
        numero_introducido_jugador = int(txt_numero.get())
        if numero_introducido_jugador == numero_adivinar :
            messagebox.showinfo("Win", "Has adivinado el numero")
            fin()
        else:
            if numero_introducido_jugador > numero_adivinar:
                messagebox.showinfo("Ayuda", "El numero es menor")
            elif numero_introducido_jugador < numero_adivinar:
                messagebox.showinfo("Ayuda", "El numero es mayor")
    except TypeError:
        messagebox.showwarning("Error", "Solo admite numero entero reintroduce un numero")


#crear la ventana
window = Tk()
window.title("Adivina el numero. ")
window.configure(width=320, height=250, background="#ffa5a9")
window.resizable(width=False, height=False)

#paneles de texto
label_vidas = Label(window, text="Numero de Vidas", width=15, background="#ffa5a9")
label_vidas.grid(column=0, row=0)

label_numero = Label(window, text="Numero del 1 al 100:", width=15, background="#ffa5a9")
label_numero.grid(column=0, row=1)

produccion = StringVar(window, "0")
txt_intentos = Entry(window, width=30, textvariable=produccion)
txt_intentos.grid(column=1, row=0)

txt_numero = Entry(window, width=30)
txt_numero.grid(column=1, row=1);

#botones de juego
btn_adivinar = Button(window, text="Adivinar", command=jugar, width=15)
btn_adivinar.grid(column=1, row=2, padx=5, pady=5)

btn_salir = Button(window, text="Salir", command=fin, width=15)
btn_salir.grid(column=0, row=2, padx=5, pady=5)

window.mainloop()

