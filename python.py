import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

SAVE_FILE = "datos_mascota.txt"

class Mascota:
    
    def __init__(self, nombre, hambre=50, felicidad=50):
        self.nombre = nombre
        self.hambre = hambre
        self.felicidad = felicidad
        print(f"¡Ha nacido {self.nombre}!") 

    def alimentar(self):
        self.hambre = max(0, self.hambre - 15)
        self.felicidad = min(100, self.felicidad + 5)
        print("Mascota alimentada.") 
        return "...¡Qué rico!"

    def jugar(self):
        self.felicidad = min(100, self.felicidad + 15)
        self.hambre = min(100, self.hambre + 10) 
        print("Mascota ha jugado.")
        return "...¡Qué divertido!"

    def guardar(self):
        try:
            with open(SAVE_FILE, "w") as f:
                f.write(f"{self.nombre}\n")
                f.write(f"{self.hambre}\n")
                f.write(f"{self.felicidad}\n")
            print(f"¡Progreso de {self.nombre} guardado!")
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

def cargar_mascota():
    if not os.path.exists(SAVE_FILE):
        return None 
    try:
        with open(SAVE_FILE, "r") as f:
            nombre = f.readline().strip()
            hambre = int(f.readline().strip())
            felicidad = int(f.readline().strip())
            
            print(f"¡Bienvenido de nuevo, {nombre}!")
            return Mascota(nombre, hambre, felicidad)
    except Exception as e:
        print(f"Error al cargar el archivo, empezando de cero. ({e})")
        return None

class MascotaApp:
    
    def __init__(self, root, mascota):
        self.root = root
        self.mascota = mascota
        self.root.title(f"Mascota Virtual: {self.mascota.nombre}")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        self.lbl_nombre = tk.Label(root, text=self.mascota.nombre, font=("Helvetica", 16, "bold"))
        self.lbl_nombre.pack(pady=10)


        self.lbl_estado = tk.Label(root, text="", font=("Helvetica", 12))
        self.lbl_estado.pack(pady=5)
        self.lbl_mensaje_accion = tk.Label(root, text="¡Hola!", font=("Helvetica", 10, "italic"))
        self.lbl_mensaje_accion.pack(pady=5)

       
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        self.btn_alimentar = tk.Button(frame_botones, text="Alimentar", command=self.accion_alimentar)
        self.btn_alimentar.pack(side=tk.LEFT, padx=5)

        self.btn_jugar = tk.Button(frame_botones, text="Jugar", command=self.accion_jugar)
        self.btn_jugar.pack(side=tk.LEFT, padx=5)

        
        self.btn_salir = tk.Button(root, text="Guardar y Salir", command=self.guardar_y_salir)
        self.btn_salir.pack(pady=10)

        
        self.actualizar_labels_estado() 
        self.paso_del_tiempo()

        self.root.protocol("WM_DELETE_WINDOW", self.guardar_y_salir)

    def actualizar_labels_estado(self):
        estado_texto = f"Hambre: {self.mascota.hambre}/100\nFelicidad: {self.mascota.felicidad}/100"
        self.lbl_estado.config(text=estado_texto)
        
        if self.mascota.hambre > 80 or self.mascota.felicidad < 20:
            self.lbl_estado.config(fg="red")
        else:
            self.lbl_estado.config(fg="black")

    def accion_alimentar(self):
        mensaje = self.mascota.alimentar()
        self.lbl_mensaje_accion.config(text=mensaje)
        self.actualizar_labels_estado()

    def accion_jugar(self):
        mensaje = self.mascota.jugar()
        self.lbl_mensaje_accion.config(text=mensaje)
        self.actualizar_labels_estado()

    def guardar_y_salir(self):
        if self.mascota.guardar():
            messagebox.showinfo("Guardado", f"¡Progreso de {self.mascota.nombre} guardado! ¡Adiós!")
        else:
            messagebox.showerror("Error", "No se pudo guardar el progreso.")
        
        self.root.destroy() 

    def paso_del_tiempo(self):
        self.mascota.hambre = min(100, self.mascota.hambre + 2)
        self.mascota.felicidad = max(0, self.mascota.felicidad - 1)
        self.actualizar_labels_estado()
        
        self.root.after(3000, self.paso_del_tiempo)

def main():
    
    mi_mascota = cargar_mascota()

    
    root_temp = tk.Tk()
    root_temp.withdraw()

  
    if mi_mascota is None:
        nombre_mascota = simpledialog.askstring("Nueva Mascota", "Dale un nombre a tu nueva mascota:")
        if not nombre_mascota:
            nombre_mascota = "Amigo"
            

        mi_mascota = Mascota(nombre_mascota)


    root = tk.Toplevel(root_temp)
    app = MascotaApp(root, mi_mascota)
    root.mainloop() 

if __name__ == "__main__":
    main()


