from tkinter import *
from tkinter import ttk
import tkinter as tk

class Aplicacion():
    __ventana=None
    __iva=None
    __preciobase=None
    __precioconiva=None
    __tasa_iva=None

    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.geometry('650x430')
        self.__ventana.title('Calculadora IVA')
        mainframe = ttk.Frame(self.__ventana, padding="10 10 20 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        style = ttk.Style()
        style.configure('Calcular.TButton', font=('Arial', 12), borderwidth=4, relief="groove", padding=5, background='green', foreground='black')
        style.configure('Salir.TButton', font=('Arial', 12), borderwidth=4, relief="groove", padding=5, background='red', foreground='black')

        n_rows = 6
        n_columns = 2
        for i in range(n_rows):
            mainframe.grid_rowconfigure(i, weight=1)
        for i in range(n_columns):
            mainframe.grid_columnconfigure(i, weight=1)
        self.__ventana.grid_rowconfigure(0, weight=1)
        self.__ventana.grid_columnconfigure(0, weight=1)


        self.__iva = StringVar()
        self.__preciobase = StringVar()
        self.__precioconiva = StringVar()
        self.__tasa_iva = DoubleVar()
        self.valorI = tk.IntVar()

        ttk.Label(mainframe, text="Precio sin IVA").grid(column=0, row=0, sticky=W)
        self.preciobaseEntry = ttk.Entry(mainframe, width=5, textvariable=self.__preciobase,)
        self.preciobaseEntry.grid(column=1, row=0, sticky=(W, E))

        ttk.Radiobutton(mainframe, text='IVA 21%', value=21, variable=self.__tasa_iva, command=self.valorI).grid(row =1, column=0, sticky=W)
        ttk.Radiobutton(mainframe, text='IVA 10.5%', value=10.5, variable=self.__tasa_iva, command=self.valorI).grid(row =2, column=0, sticky=W)

        ttk.Label(mainframe, text="IVA").grid(column=0, row=3, sticky=W)
        self.ivaEntry = ttk.Entry(mainframe, width=5, textvariable=self.__iva,)
        self.ivaEntry.grid(column=1, row=3, sticky=(W, E))

        ttk.Label(mainframe, text="Precio con IVA").grid(column=0, row=4, sticky=W)
        self.precioconivaEntry = ttk.Entry(mainframe, width=5, textvariable=self.__precioconiva,)
        self.precioconivaEntry.grid(column=1, row=4, sticky=(W, E))

        buton_calcular = ttk.Button(mainframe, text="Calcular", style='Calcular.TButton', command=self.calcular_iva).grid(column=0, row=5, sticky=W)
        buton_salir = ttk.Button(mainframe, text='Salir', style='Salir.TButton', command=self.__ventana.destroy).grid(column=1, row=5, sticky=W)
        self.valorI.set(-1)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=50, pady=20)
        self.preciobaseEntry.focus()
        self.__ventana.mainloop()

    def calcular_iva(self):
        precio_base = float(self.preciobaseEntry.get())
        tasa_iva_val = self.__tasa_iva.get()
        iva = precio_base * tasa_iva_val / 100
        precio_con_iva = precio_base + iva
        self.ivaEntry.delete(0, END)
        self.ivaEntry.insert(0, f"{iva:.2f}")
        self.precioconivaEntry.delete(0, END)
        self.precioconivaEntry.insert(0, f"{precio_con_iva:.2f}")

def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()