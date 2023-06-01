from tkinter import *
import random
#---------------------
# VARIABLES GLOBALES
#--------------------

BASE = 460
ALTURA = 220

#--------------------
# VENTANA PRINCIPAL
#--------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#----------------------
# Frame de graficacion
#----------------------

frame_graficacion = Frame(ventana_principal)    
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# creacion canvas 

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

# Generar 100 circulos de 20 de radio y color y posicion aleatoria sin salirse del canvas
for i in range(10000):
    #generar color aleatorio
    color = "#"
    for i in range(6):
        color = color + random.choice("0123456789ABCDEF")
    #generar color aleatorio 
    x = random.randint(0,  BASE-20)
    y = random.randint(0, ALTURA-20)

    # dibujamos el circulo
    circulo = c.create_oval(x,y,x+20,y+20,fill = color)


#--------------------
# frame controles
#--------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

linea_central_horizontal = c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="green")
linea_central_vertical = c.create_line(BASE/2,0,BASE/2,ALTURA, fill= "green")

ventana_principal.mainloop()


