Proyecto: Mascota Virtual en Python

Este es un sencillo juego de simulación de mascota virtual desarrollado en Python. La aplicación utiliza la biblioteca tkinter para la interfaz gráfica de usuario (GUI) y demuestra conceptos clave de la Programación Orientada a Objetos (OOP) y el manejo de archivos para persistencia de datos.

Características Principales

Interfaz Gráfica (GUI): Creada con tkinter, la biblioteca estándar de Python.

Programación Orientada a Objetos: La mascota es un objeto instanciado de una clase Mascota, que encapsula sus propios datos (atributos) y comportamientos (métodos).

Persistencia de Datos: El estado de la mascota (nombre, hambre, felicidad) se guarda automáticamente en un archivo (datos_mascota.txt) al salir y se recarga al iniciar.

Mecánica de Juego Simple: El estado de la mascota decae pasivamente con el tiempo, requiriendo la interacción del usuario.

Configuración del Entorno (Setup)

Este proyecto está diseñado para ejecutarse en un entorno virtual aislado (venv) para seguir las mejores prácticas de desarrollo en Python.

1. Requisitos Previos

Tener Python 3 instalado.

2. Clonar y Preparar el Entorno

Clonar el repositorio (o descargar los archivos) en una carpeta local.

Abrir una terminal (PowerShell o CMD) y navegar a la carpeta raíz del proyecto (donde se encuentra este README.md).

# Ejemplo de cómo navegar a la carpeta
cd "C:\Ruta\A\Tu\Proyecto\Python-Tutorial"


Crear el Entorno Virtual:
Este comando crea una carpeta llamada venv que contendrá una instalación de Python aislada para este proyecto.

python -m venv venv


Activar el Entorno Virtual:
Debe activar el entorno para "entrar" en él.

En Windows (PowerShell):

.\venv\Scripts\Activate


(Si encuentras un error de "scripts deshabilitados", ejecuta primero: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process y vuelve a intentarlo)

En Windows (CMD):

.\venv\Scripts\activate.bat


En macOS / Linux:

source venv/bin/activate


Tu terminal debería ahora mostrar (venv) al inicio de la línea.

3. Dependencias

Este proyecto no requiere dependencias externas (usa tkinter, que viene incluido con Python).

Si en el futuro se añadieran librerías, se instalarían aquí usando pip install -r requirements.txt.

Cómo Ejecutar el Juego

Con el entorno virtual activado, simplemente ejecuta el script principal de Python:

python python.py


La primera vez que se ejecute, te pedirá un nombre para tu nueva mascota.

Las veces siguientes, cargará automáticamente el progreso de la mascota que guardaste.

Cómo Jugar

El objetivo es mantener a tu mascota feliz y alimentada.

Estadísticas:

Hambre: ¡Mientras más bajo, mejor! 0 = Lleno, 100 = Hambriento.

Felicidad: ¡Mientras más alto, mejor! 100 = Feliz, 0 = Triste.

Paso del Tiempo:
Automáticamente, cada 3 segundos, la Hambre subirá +2 y la Felicidad bajará -1. ¡No descuides a tu mascota!

Advertencia Visual:
Si el Hambre sube a más de 80 o la Felicidad baja a menos de 20, las estadísticas se pondrán de color ROJO para alertarte.

Acciones (Botones):

Alimentar: Reduce el Hambre (-15) y aumenta un poco la Felicidad (+5).

Jugar: Aumenta mucho la Felicidad (+15) pero da un poco de Hambre (+10).

Guardar:
El juego se guarda automáticamente al presionar el botón "Guardar y Salir" o al cerrar la ventana.