
from tkinter import *

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

# dibujar una linea recta
#linea_1 = c.create_line(BASE/2, ALTURA/2, BASE,0, fill="red", width=2)
#linea_2 = c.create_line(BASE, ALTURA, BASE/2, ALTURA/2, fill="yellow", width=2)
#linea_3 = c.create_line(0,ALTURA,BASE/2,ALTURA/2, fill="blue", width=2)
#linea_4 = c.create_line(0,0,BASE/2,ALTURA/2, fill="green", width=2)

# dibujar texto
#texto_1 = c.create_text(BASE/4, ALTURA/2, anchor="center", tex="SISTEMAS!", font=("Arial", 20, "bold"), fill="blue", activefill="yellow")

#texto_2 = c.create_text(3*BASE/4, ALTURA/2, anchor="center", tex="COLEGIO", font=("Arial", 20, "bold"), fill="blue", activefill="yellow")

#texto_3 = c.create_text(2*BASE/4, ALTURA/1.3, anchor="center", tex="GUANENTA", font=("Arial", 20, "bold"), fill="blue", activefill="yellow")

#texto_4 = c.create_text(2*BASE/4, ALTURA/4.7, anchor="center", tex="ESPECIALIDAD", font=("Arial", 20, "bold"), fill="blue", activefill="yellow")

# DIBUJAR RECTANGULO 
rect_1 = c.create_rectangle(BASE/2,ALTURA/2, BASE, ALTURA, fill= "pink", outline ="blue")
rect_2 = c.create_rectangle(0,0,BASE/2, ALTURA/2, fill = "orange", outline="white")


# DIBUJAR CIRCULOS 
circ_1 = c.create_oval(BASE/2,0,BASE,ALTURA/2, fill="blue")
circ_2 = c.create_oval(0,ALTURA/2,BASE/4,ALTURA, fill="yellow")
circ_3 = c.create_oval(BASE/4,ALTURA/2,BASE/2,ALTURA, fill = "red")

# DIBUJAR POLIGONOS 
polig_1 = c.create_polygon(3*BASE/4,ALTURA/2,BASE,ALTURA,BASE/2,ALTURA, fill ="red")
polig_2 = c.create_polygon(BASE/4,0,BASE/2,ALTURA/4,BASE/4,ALTURA/2,0,ALTURA/4, fill="white")
outline="black"

#----------------------_
# FRAME DE CONTROLES 
# -----------------------

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, heigh=230)
frame_controles.place(x=10, y=260)


# DESPLEGAR VENTANA 

ventana_principal.mainloop()
