import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcos
apellido: Provenzano
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        nombre_usuario=prompt(title="dato", prompt="Ingrese un nombre")

        #mensaje= "el nombre es " + nombre_usuario

        # mensaje= "el nombre es {0}".format(nombre_usuario)
    
        mensaje= f"el nombre es {nombre_usuario}"
    
        # print(mensaje)
        
        alert(title="dato", message=mensaje)
        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()