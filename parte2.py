import os
import subprocess
import time
import sys

# Se crea la función para verificar si el proceso está en ejecución
def is_process_running(process_name):
    try:
        # Lista todos los procesos en ejecución
        process_list = os.popen('ps aux').read()
        return process_name in process_list
    except:
        return False

# Acá empieza la función principal
def main(process_name, command):
    while True:
        # Este ciclo se hace para verifica periodicamente si el proceso está en ejecución
        if not is_process_running(process_name):
            print(f'El proceso {process_name} no se está ejecutando. Reiniciando...')
            subprocess.Popen(command.split())
        else:
            print(f'El proceso {process_name} está en ejecución.')
        
        # Se settea el tiempo a 5 de verificación a cada 5 segundos
        time.sleep(5)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Uso: python "script.py" <nombre_del_proceso> <comando_para_ejecutar>')
        sys.exit(1)
    
    process_name = sys.argv[1]
    command = sys.argv[2]
    main(process_name, command)
