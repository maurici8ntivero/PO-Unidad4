
import tkinter as tk
from tkinter import messagebox
import requests


class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        #datos de la ventana
        self.geometry("500x200")
        self.title("Conversor de moneda")
        
        #Datos del archivo
        url = "https://www.dolarsi.com/api/api.php?type=dolar"
        json_data = requests.get(url).json()
        
        
        dato = (json_data[0]["casa"]["venta"])
        
        array = dato.split(",")
        num = array[0] +"." + array[1]
        
        self.valorDolar = tk.StringVar()
        self.valorDolar.set(num)
        
        
   
                
        self.valor = tk.StringVar()
        self.valorPesos = tk.StringVar()
        self.valor.trace("w", self.calcular)
        #Atributos
        opts = {"pady": 5, "padx": 5}
        
        #dolar Frame
        dolarFrame = tk.Frame(self)
        dolarFrame.pack(side = tk.TOP)
        
        #Conversor Frame
        conversorFrame = tk.Frame(self)
        conversorFrame.pack(side = tk.TOP)
        #Entrys
        
        entry = tk.Entry(dolarFrame, textvariable = self.valor)
        entry.pack(side = tk.LEFT ,**opts)
        
        #Label
        dolar = tk.Label(dolarFrame, text = "Dólar")
        dolar.pack(side = tk.RIGHT, **opts)
        pesos = tk.Label(conversorFrame, text = "Es equivalente a ")
        valorConversion = tk.Label(conversorFrame, textvariable = self.valorPesos)
        
        
        pesos2 = tk.Label(conversorFrame, text = " pesos")
        pesos.pack(side = tk.LEFT, **opts)
        valorConversion.pack(side = tk.LEFT, **opts)
        pesos2.pack(side = tk.RIGHT, **opts)
        
        #Botones
        boton = tk.Button(self, text = "Salir", command = self.salir)
        boton.pack(side = tk.BOTTOM,**opts)
        entry.focus()
        self.mainloop()
        
    def salir(self):
        self.destroy()
    def calcular(self, *args):
        if self.valor.get() != "":
            try:
                self.valorPesos.set(float(self.valor.get()) * float(self.valorDolar.get()))
                
            except ValueError:
                messagebox.showerror(title = "Eror de tipo", message = "Debe ingresar un valor numérico")
                self.valor.set(0)
                self.entry.focus()
        else:
            self.valorPesos.set(0)
            
        return 


