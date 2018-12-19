import tkinter
from tkinter import ttk
import random
from random import choice
import sys
 
root=tkinter.Tk()
root.title("Generátor náhodných čísel") #pojmenování okna

value1=tkinter.StringVar()
value2=tkinter.StringVar()

entry1=ttk.Entry(root, textvariable=value1) #definice widgetů v okně
entry2=ttk.Entry(root, textvariable=value2)
label1=ttk.Label(root, text="Zadejte počet žáků:")
label2=ttk.Label(root, text="Zadejte počet generovaných čísel:")
label3=ttk.Label(root, text="© Jiří Zinecker")

def generate(): #funkce pro generování seznamu náhodných čísel
    list1=[]
    value1Int=int(value1.get())
    value2Int=int(value2.get())
    
    for i in range(value2Int): 
        list1.append(str(choice([i for i in range(1,value1Int) if i not in [28]]))+",") #generování čísla, kromě čísel ve hranatých závorek

    root2=tkinter.Tk() #2. okno se seznamem generovaných čísel
    root2.title="Vylosovaní"
    label2=ttk.Label(root2, text=list1)
    label3=ttk.Label(root2, text="Vylosovaným gratulujeme!")
    button1=ttk.Button(root2, text="OK", command=lambda: root2.destroy())

    label2.pack()
    label3.pack()
    button1.pack()

quitButton = ttk.Button(root, text="Ukončit", command=sys.exit)
showButton=ttk.Button(root, text="Generuj číslo", command=generate)
 
label1.grid(column=1, row=1, sticky="we") #uspořádání widgetů v okně
label2.grid(column=1, row=2, sticky="we")
label3.grid(column=1, row=3, sticky="w")
entry1.grid(column=2, row=1, sticky="we")
entry2.grid(column=2, row=2, sticky="we")
quitButton.grid(column=1, row=3, sticky="e")
showButton.grid(column=2, row=3, sticky="e")
 
root.mainloop()