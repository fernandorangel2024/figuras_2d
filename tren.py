from tkinter import*

BASE = 460
ALTURA = 460

Ventana_principal = Tk ()
Ventana_principal.title("trencito")
Ventana_principal.resizable(False,False)
Ventana_principal.geometry("460x450")
Ventana_principal.config(bg="white")

frame_graficacion= Frame(Ventana_principal)
frame_graficacion.config(bg="white", width=480, height=480)
frame_graficacion.place(x=5, y=5)

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="white")
c.place(x=0, y=0)
#RECTANGULOS
rect_1 = c.create_rectangle(BASE/2,0,BASE/2+170,ALTURA/2-205, fill="dim gray", outline="black")
rect_2 = c.create_rectangle(BASE/2,0+65,BASE/2+170,ALTURA/2-50, fill="dim gray", outline="black")
rect_11 = c.create_rectangle(BASE/2+30,0+90,BASE/2+140,ALTURA/2-80, fill="light blue", outline="light blue")
rect_3 = c.create_rectangle(BASE/2-30,0+25,BASE/2+200,ALTURA/2-165, fill="dim gray", outline="black")
#CIRCULOS
circ_4 = c.create_oval(0,ALTURA/2-40,BASE/2-10,ALTURA-80, fill="dim gray", outline="black")
rect_6 = c.create_rectangle(BASE/2-150,ALTURA/2-40,BASE/2-120,ALTURA-80, fill="dim gray", outline="black")
rect_7 = c.create_rectangle(0+120,0+130,BASE/2-60,ALTURA/2, fill="dim gray", outline="black")
#RECTNGULOS PRINCIPALES
rect_8 = c.create_rectangle(0+100,0+100,BASE/2-40 ,ALTURA/2-100, fill="dim gray", outline="black")
rect_4 = c.create_rectangle(0 +100,ALTURA/2-50,BASE/2+200,ALTURA/2+160, fill="dim gray", outline="black")
#CIRCULOS PRINCIPALES
circ_1 = c.create_oval(BASE/2-130,ALTURA/2+120,BASE/2-20,ALTURA, fill="dim gray", outline="black")
circ_2 = c.create_oval(BASE/2-5,ALTURA/2+120,BASE-125,ALTURA, fill="dim gray", outline="black")
circ_3 = c.create_oval(BASE/2+120,ALTURA/2+120,BASE,ALTURA, fill="dim gray", outline="black")
# RECTANGULOS
rect_5 = c.create_rectangle(0+30,ALTURA/2-60,BASE/2-150,ALTURA-60, fill="dim gray", outline="black")
rect_9 = c.create_rectangle(BASE/2-55,ALTURA/2+160,BASE/2+30,ALTURA-40, fill="gray", outline="black")
rect_10 = c.create_rectangle(BASE/2+70,ALTURA/2+160,BASE/2+155,ALTURA-40, fill="gray", outline="black")
Text_1 = c.create_text(BASE/2+40, ALTURA/2+40, anchor="center", text="davidcito", font=("Arial", 20,"bold"),fill="black")
#-------
# cara del homosexual
#------
circ_5 = c.create_oval(BASE/2+35,0+85,BASE-95,ALTURA/2-70, fill="yellow", outline="black")
circ_6 = c.create_oval(BASE/2+90,0+100,BASE/2+115,0+125, fill="white", outline="white")
circ_7 = c.create_oval(BASE/2+55,0+100,BASE/2+80,0+125, fill="white", outline="white")
circ_6 = c.create_oval(BASE/2+95,0+105,BASE/2+110,0+120, fill="black", outline="dim gray")
circ_7= c.create_oval(BASE/2+60,0+105,BASE/2+75,0+120, fill="black", outline="dim gray")
circ_8 = c.create_oval(BASE/2+75,125+0,BASE/2+100,0+160, fill="red", outline="red")
Ventana_principal.mainloop()