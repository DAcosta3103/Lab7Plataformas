import subprocess
import psutil
import time
import matplotlib.pyplot as plt

# Se crea una función para monitorear y registrar el consumo de CPU y memoria
def monitorizar_proceso(pid, intervalo=5):
    with open('log_proceso.txt', 'w') as file: #Se elige formato .txt para el archivo de lol}g
        while True:
            try:
                proceso = psutil.Process(pid)
                cpu = proceso.cpu_percent(interval=intervalo)
                memoria = proceso.memory_info().rss
                file.write(f'{time.time()}, {cpu}, {memoria}\n')
            except psutil.NoSuchProcess:
                break

# Esta función grafica los datos del archivo de log 
def graficar_datos():
    tiempos, cpus, memorias = [], [], []
    with open('log_proceso.txt', 'r') as file:
        for linea in file:
            tiempo, cpu, memoria = map(float, linea.split(','))
            tiempos.append(tiempo)
            cpus.append(cpu)
            memorias.append(memoria)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(tiempos, cpus, label='Uso de CPU (%)')
    plt.xlabel('Tiempo')
    plt.ylabel('CPU (%)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(tiempos, memorias, label='Uso de Memoria (bytes)')
    plt.xlabel('Tiempo')
    plt.ylabel('Memoria (bytes)')
    plt.legend()

    plt.show()

# Acá se ejecuta el proceso y se monitorea el mismo
if __name__ == '__main__':
    ruta_ejecutable = input('Ingrese la ruta del ejecutable: ')
    proceso = subprocess.Popen(ruta_ejecutable)
    monitorizar_proceso(proceso.pid)
    graficar_datos()
