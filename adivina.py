import random
import tkinter as tk
NumAle = random.randint(1,100)
print(NumAle)
vidas = 10

def capturaNum():
    try:
        numeroIngresado = int(cajaNUm.get())
        cajaNUm.delete(0, 'end')  # Limpia la caja de entrada
        return numeroIngresado
    except ValueError:
        mensaje.config(text="⚠️ Ingresa un número válido.")
        return None
    
def check(event=None):
    global vidas
    captura = capturaNum()
    
    
    if captura == NumAle:
        print("Adivinaste el número")
        mensaje.config(text="🎉 ¡Adivinaste el número!", fg="green")
        boton.config(state='disabled')
        botonReset.pack()
        
    elif captura<NumAle:
        mensaje.config(text="🔼 El número es mayor.", fg="red")
    else:
        mensaje.config(text="🔽 El número es menor.", fg="red")
        
    vidas -= 1
    vidasrestantes.config(text=f"Vidas restantes: {vidas}")
    
    if vidas == 0:
        mensaje.config(text=f"😞 ¡Se acabaron las vidas! El número era {NumAle}.")
        boton.config(state='disabled')
        botonReset.pack()
        
def reset ():
    global NumAle, vidas
    NumAle = random.randint(1, 100)  # Generar un nuevo número aleatorio
    vidas = 10  # Reiniciar vidas
    vidasrestantes.config(text=f"Vidas restantes: {vidas}")  # Actualizar vidas
    mensaje.config(text="🕹️ ¡Intenta adivinar el nuevo número!")  # Mensaje inicial
    boton.config(state='normal')  # Habilitar el botón de enviar
    cajaNUm.delete(0, 'end')  # Limpiar la caja de entrada
        
        
    
    
ventana = tk.Tk()
ventana.title("AdivinaElNumero")
ventana.geometry("400x300")

bienvenida = tk.Label(ventana, text="¡Adivina el número secreto entre 1 y 100!",font=("Arial", 12) )
bienvenida.pack(pady=20)
cajaNUm = tk.Entry(ventana,font=("Arial", 14), width=8)
cajaNUm.pack()
boton = tk.Button(ventana, text= " Enviar", command=check)
boton.pack(pady=10)
mensaje= tk.Label(ventana, text="",font=("Arial", 10))
mensaje.pack()
vidasrestantes = tk.Label(ventana,text="")
vidasrestantes.pack(pady= 15)
botonReset = tk.Button(text="Reset", command=reset)
ventana.bind('<Return>', check)







ventana.mainloop()
