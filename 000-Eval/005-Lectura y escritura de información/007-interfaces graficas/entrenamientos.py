import tkinter as tk

def mostrar():
  serivalor = series_entry.get()
  repevalor = repeticiones_entry.get()
  mostrar = "Las series completadas: " + serivalor + " y Las repeticiones realizadas: " + repevalor 
  resultado.config(text=mostrar)

ventana = tk.Tk()

series_entry = tk.Entry()
series_entry.pack(padx=10,pady=10)

repeticiones_entry = tk.Entry()
repeticiones_entry.pack(padx=10,pady=10)

boton = tk.Button(text="Mostrar!",command=mostrar)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Tus series y repeteciones realizadas son: ")
resultado.pack(padx=10,pady=10)

ventana.mainloop()