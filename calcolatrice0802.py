import tkinter
import math


def button_click(numero:int):
    #catturo il numero eventualmente presente sullo schermo
    numero_presente= schermo.get()
    #pulisco lo schermo
    schermo.delete(0, tkinter.END)
    #aggiorno lo schermo(concateno il numero precedente con il corrente)
    schermo.insert(0, numero_presente + str(numero))

def button_clear():
    """Associata al tasto canc, per pulire lo schermo"""
    schermo.delete(0, tkinter.END) #per pulire da inizio a fine dello schermo

def button_add():
    primo_numero=schermo.get()
    #faccio una variabile globale di primo numero (SCONSIGLIATO)
    #per avere visibile il primo numero all'esterno di button_add
    global primo_numero_globale
    primo_numero_globale= float(primo_numero)
    schermo.delete(0, tkinter.END)
    #setto operazione algebrica
    global operazione
    operazione= "+"


def button_equal():
    secondo_numero= schermo.get()
    schermo.delete(0,tkinter.END)
    # gestione operazione algebrica (+, -, *, /)
    if operazione == "+":
        schermo.insert(0, f"{(primo_numero_globale + float(secondo_numero)):.3f}")
    elif operazione == "-":
        schermo.insert(0, f"{(primo_numero_globale - float(secondo_numero)):.3f}")
    elif operazione == "x":
        schermo.insert(0, f"{(primo_numero_globale * float(secondo_numero)):.3f}")
    elif operazione == "-": # operazione = "/":
        schermo.insert(0, f"{(primo_numero_globale / float(secondo_numero)):.3f}")
    elif operazione == "%":
        schermo.insert(0, f"{primo_numero_globale*(float(secondo_numero)/100):.2f}")
    elif operazione == "sqrt":
        schermo.insert(0, f"{math.pow(primo_numero_globale, 1/float(secondo_numero)):.3f}")
    else:
        schermo.insert(0, f"{math.pow(primo_numero_globale, float(secondo_numero))}")




def button_subtrack():
    primo_numero=schermo.get()
    #faccio una variabile globale di primo numero (SCONSIGLIATO)
    #per avere visibile il primo numero all'esterno di button_add
    global primo_numero_globale
    primo_numero_globale= float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione= "-"


def button_mult():
    primo_numero=schermo.get()
    #faccio una variabile globale di primo numero (SCONSIGLIATO)
    #per avere visibile il primo numero all'esterno di button_add
    global primo_numero_globale
    primo_numero_globale= float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione= "x"

def button_div():
    primo_numero=schermo.get()
    #faccio una variabile globale di primo numero (SCONSIGLIATO)
    #per avere visibile il primo numero all'esterno di button_add
    global primo_numero_globale
    primo_numero_globale= float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione= "/"

def calculate_perc():
    primo_numero = schermo.get()
    global primo_numero_globale
    primo_numero_globale= float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione="%"


def calculate_sqrt():
    primo_numero=schermo.get()
    #faccio una variabile globale di primo numero (SCONSIGLIATO)
    #per avere visibile il primo numero all'esterno di button_add
    global primo_numero_globale
    primo_numero_globale= float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione= "sqrt"

def calculate_pow():
    primo_numero=schermo.get()
    #faccio una variabile globale di primo numero (SCONSIGLIATO)
    #per avere visibile il primo numero all'esterno di button_add
    global primo_numero_globale
    primo_numero_globale= float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione= "^"



#Creazione della finestra
window = tkinter.Tk()
#creazione titolo della finestra
window.title("CalCoolator")

#inserire icona
window.iconbitmap("icons8-calculator-48.ico")

schermo= tkinter.Entry(window, width=18, borderwidth=5, background="black", font=("Helvetica", 20, "bold"), foreground="#CAF0F8", justify="left")
schermo.grid(row=0, column=0, columnspan=3)

#creazione dei bottoni
button1= tkinter.Button(window, text="1", padx=40, pady=10, borderwidth=3, command=lambda:button_click(1))
button2= tkinter.Button(window, text="2", padx=40, pady=10, borderwidth=3, command=lambda:button_click(2))
button3= tkinter.Button(window, text="3", padx=40, pady=10, borderwidth=3, command=lambda:button_click(3))
button4= tkinter.Button(window, text="4", padx=40, pady=10, borderwidth=3, command=lambda:button_click(4))
button5= tkinter.Button(window, text="5", padx=40, pady=10, borderwidth=3, command=lambda:button_click(5))
button6= tkinter.Button(window, text="6", padx=40, pady=10, borderwidth=3, command=lambda:button_click(6))
button7= tkinter.Button(window, text="7", padx=40, pady=10, borderwidth=3, command=lambda:button_click(7))
button8= tkinter.Button(window, text="8", padx=40, pady=10, borderwidth=3, command=lambda:button_click(8))
button9= tkinter.Button(window, text="9", padx=40, pady=10, borderwidth=3, command=lambda:button_click(9))
button0= tkinter.Button(window, text="0", padx=40, pady=10, borderwidth=3, command=lambda:button_click(0))

button_canc= tkinter.Button(window, text="CANC", background="#023E8A", foreground="white", activebackground="#0077B6", padx=74, pady=10, borderwidth=3, command= button_clear)
button_più= tkinter.Button(window, text="+", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=39, pady=10, borderwidth=3, command= button_add)
button_uguale= tkinter.Button(window, text="=", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=86.5, pady=10, borderwidth=3, command= button_equal)
button_meno= tkinter.Button(window, text="-", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=41, pady=10, borderwidth=3, command= button_subtrack)
button_per= tkinter.Button(window, text="x", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=40, pady=10, borderwidth=3, command= button_mult)
button_diviso= tkinter.Button(window, text="/", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=40, pady=10, borderwidth=3, command= button_div)
button_percentuale= tkinter.Button(window, text="%", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=39, pady=10, borderwidth=3, command= calculate_perc)
button_sqrt= tkinter.Button(window, text="x\u207f", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=38, pady=10, borderwidth=3, command= calculate_sqrt)
button_pot= tkinter.Button(window, text="^", background="#0077B6",foreground="white", activebackground="#90E0EF", padx=38, pady=10, borderwidth=3, command= calculate_pow)

button7.grid(row=1,column=0, padx=1, pady=1)
button8.grid(row=1,column=1, padx=1, pady=1)
button9.grid(row=1,column=2, padx=1, pady=1)

button4.grid(row=2,column=0, padx=1, pady=1)
button5.grid(row=2,column=1, padx=1, pady=1)
button6.grid(row=2,column=2, padx=1, pady=1)

button1.grid(row=3,column=0, padx=1, pady=1)
button2.grid(row=3,column=1, padx=1, pady=1)
button3.grid(row=3,column=2, padx=1, pady=1)

button0.grid(row=4,column=0, padx=1, pady=1)
button_canc.grid(row=4, column=1, columnspan=2, padx=1, pady=1)

button_più.grid(row=5, column=0, padx=1, pady=1)
button_uguale.grid(row=5, column=1, columnspan=2, padx=1, pady=1)

button_meno.grid(row=6, column=0, padx=1, pady=1)
button_per.grid(row=6, column=1, padx=1, pady=1)
button_diviso.grid(row=6, column=2, padx=1, pady=1)

button_percentuale.grid(row=7, column=0, padx=1, pady=1)
button_sqrt.grid(row=7, column=1, padx=1, pady=1)
button_pot.grid(row=7, column=2, padx=1, pady=1)

#Chiusura della finestra
window.mainloop()