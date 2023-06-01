from tkinter import *
import random

#--------------------
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
# FRAME DE GRAFICACION 
#----------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# CREACION CANVAS

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

# MOLINO 
#base_1 = c.create_rectangle(BASE/2-150,ALTURA-30, BASE/2+150,ALTURA,fil=color)
#triangulo = c.create_polygon(BASE/2,ALTURA/2, BASE/2+20, ALTURA-30, BASE/2-20,ALTURA-30, fill=color)
#aspa_1 = c.create_arc(BASE/2-50, ALTURA/2-50,BASE/2+50,ALTURA/2+50,star =45,extent=60, fill="#ffffffff")
#aspa_2 = c.create_arc(BASE/2-50, ALTURA/2-50,BASE/2+50,ALTURA/2+50,star =165,extent=60, fill="#00ffff")
#aspa_3 = c.create_arc(BASE/2-50, ALTURA/2-50,BASE/2+50,ALTURA/2+50,star =285,extent=60, fill="#ffff00")

# GENERAR 100 CIRCULOS DE 20 DE RADIO, Y COLOR Y POSICION ALEATORIO, SIN SALIRSE DEL CANVAS
for i in range(30):
    #generar color aleatorio
    color = "#"
    for i in range(6):
        color = color + random.choice("0123456789ABCDEF")
    # generar calor de x e y aleatorio 
    radio = random.randint(5,25)
    x = random.randint(0, BASE-2*radio)
    y = random.randint(0,ALTURA-2*radio)

    # DIBUJAMOS EL CIRCULO
    circulo = c.create_oval(x,y,x+2*radio,y+2*radio, fill=color )

# agregar una imagen al canvas
img_nave =PhotoImage(file="img/nave2.png")
nave = c.create_image(BASE/2,ALTURA/2,image=img_nave)

#------------------------
# FRAME DE CONTROLES 
# -----------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)


# DESPLEGAR VENTANA 

ventana_principal.mainloop()