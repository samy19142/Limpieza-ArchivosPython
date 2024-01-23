import re
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as MessageBox

# Función para limpiar y extraer la información
def procesar_linea(linea):
    # Utiliza expresiones regulares para extraer la información deseada
    match = re.match(r'\s*(\d*\s*[a-zA-Z0-9 -.]{9})\s+(\d+)\s+([\d,.]+)\s+(\w+)\s+(\d{2}:\d{2}:\d{2})\s+(\w)\s+(\d+\s+\d+\s+\d+\s+\d+)\s+([0-9 -]{1,12})\s+(\d+)\s+(\d+/\d+/+\d+)', linea)    
    
    if match:
        # Formato de la información extraída
        resultado = '|'.join(match.groups())
        return resultado
    else:
        return None

def procesar_archivo(archivo_entrada, archivo_salida):
    cabeceras = ['Tipo Operacion', 'Transaccion', 'Valor', 'Cajero', 'Hora', 'Fran', 'No Tarjeta', 'Cta Debito','Autorizacion','Fecha']
    # Procesar el archivo
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada, open(archivo_salida, 'w', encoding='utf-8') as salida:
        salida.write('|'.join(cabeceras) + '\n')
        for linea in entrada:
            # Procesar cada línea del archivo
            resultado_linea = procesar_linea(linea)
            if resultado_linea:
                # Escribir el resultado en el nuevo archivo
                salida.write(resultado_linea + '\n')

    print(f"******Proceso completado. Resultados guardados en '{archivo_salida}'.*******")
    MessageBox.showinfo("Limpieza","Proceso Finalizado!")


def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    archivo_entrada_path = filedialog.askopenfilename(title="Seleccionar archivo de entrada", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    if archivo_entrada_path:
        archivo_salida_path = filedialog.asksaveasfilename(title="Guardar como", defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if archivo_salida_path:
            procesar_archivo(archivo_entrada_path, archivo_salida_path)

if __name__ == "__main__":
    seleccionar_archivo()
