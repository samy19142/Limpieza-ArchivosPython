import re
import tkinter as tk
from tkinter import filedialog

def procesar_archivo(archivo_entrada_path, carpeta_salida_path):
    # Expresión regular para identificar líneas con datos relevantes
    pattern = re.compile(r'\s+([A-Z]{2})\s+(\S+)\s+(.+?)\s+(\w+)\s+(\d+)\s+(\d+)\s+([0-9,.]+)\s+(\d+:\d+:\d+)')

    # Lista de cabeceras
    cabeceras = ['Tipo', 'Cuenta', 'Nombre Cuenta', 'Tipo OP', 'Docto', 'Autoriz', 'Valor', 'Hora']

    # Generar la ruta completa del archivo de salida
    archivo_salida_path = f"{carpeta_salida_path}/resultados_con_cabecera.txt"

    # Procesar el archivo línea por línea y guardar los resultados en formato CSV con cabeceras
    with open(archivo_entrada_path, 'r') as archivo_entrada, open(archivo_salida_path, 'w') as archivo_salida:
        # Agregar cabeceras al archivo de salida
        archivo_salida.write('|'.join(cabeceras) + '\n')

        for linea in archivo_entrada:
            match = pattern.search(linea)
            if match:
                resultado_deseado = '|'.join(match.groups())
                archivo_salida.write(resultado_deseado + '\n')

    print("Proceso completado. Archivo de salida creado:", archivo_salida_path)

def seleccionar_archivo_o_carpeta():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    archivo_entrada_path = filedialog.askopenfilename(title="Seleccionar archivo de entrada", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    if archivo_entrada_path:
        carpeta_salida_path = filedialog.askdirectory(title="Seleccionar carpeta de salida")
        if carpeta_salida_path:
            procesar_archivo(archivo_entrada_path, carpeta_salida_path)

if __name__ == "__main__":
    seleccionar_archivo_o_carpeta()
