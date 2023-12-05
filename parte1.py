import os
import psutil
import sys

# Primero se crea la función para obtener información del proceso
def obtener_info_proceso(pid):
    print("Obteniendo información para PID:", pid)  # Impresión de depuración para guiar al usuario
    try:
        proceso = psutil.Process(pid)
        info = proceso.as_dict(attrs=['name', 'pid', 'ppid', 'username', 'cpu_percent', 'memory_percent', 'status', 'exe'])
        return info
    except psutil.NoSuchProcess:
        return 'No se encontró el proceso con ID: {}'.format(pid)

# Función principal
def main():
    print("Número de argumentos:", len(sys.argv))  # Impresión de depuración para guiar al usuario
    if len(sys.argv) != 2:
        print("Uso: python script.py <process_id>")
        return
    pid = int(sys.argv[1])
    info_proceso = obtener_info_proceso(pid)
    print(info_proceso)

if __name__ == '__main__':
    main()
