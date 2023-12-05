# Laboratorio 7 Plataformas Abiertas

# Primera parte

## Descripción del Script

El script de Python en esta parte del proyecto está diseñado para obtener información relevante de un proceso en ejecución, dado su ID. Proporciona detalles como el nombre del proceso, ID, ID del proceso padre, usuario propietario, uso de CPU, consumo de memoria, estado y ruta del ejecutable.

## Requisitos

- Python 3.x
- Módulo `psutil`.

## Instalación

Para instalar el módulo necesario, se debe ejecutar:

```bash
pip install psutil.
```
## Uso

Para usar el script: se usa el siguiente comando:

python script.py <process_id>

# Segunda parte

Este script en Python está diseñado para monitorear un proceso específico y reiniciarlo automáticamente si se cierra. Es útil para mantener procesos críticos en ejecución sin intervención manual.

## Funcionalidades

- **Monitoreo Continuo**: El script verifica el estado de un proceso cada 5 segundos.
- **Reinicio Automático**: Si el proceso monitoreado se cierra, el script lo reinicia automáticamente.

## Requisitos

Para ejecutar este script, necesitarás Python instalado en tu sistema. Este script ha sido probado con Python 3.8, pero debería ser compatible con versiones más recientes.

## Instalación

No se requiere instalación adicional de módulos, ya que el script utiliza módulos estándar de Python (`os`, `subprocess`, `time`, `sys`).

## Uso

Para usar el script, sigue estos pasos:

1. Descarga el script `monitor_process.py` en tu máquina.
2. Abre una terminal o línea de comandos.
3. Ejecuta el script con el nombre del proceso y el comando para ejecutarlo como argumentos.

   ```bash
   python monitor_process.py <nombre_del_proceso> <comando_para_ejecutar>
    ```

## Uso

Un ejemplo de cómo usar el script es el siguiente: 

python monitor_process.py mi_proceso "python mi_script.py"

# Tercera parte

ste script en Python permite monitorear el consumo de CPU y memoria de un proceso y luego graficar estos datos. Es útil para entender el rendimiento de un programa en términos de recursos del sistema.

## Funcionalidades

- Ejecuta un proceso a partir de un ejecutable proporcionado.
- Monitorea y registra el consumo de CPU y memoria del proceso en un archivo `.txt`.
- Grafica los datos de consumo de CPU y memoria una vez que el proceso ha finalizado.

## Requisitos

Para utilizar este script, necesitarás:
- Python 3.x
- Bibliotecas `psutil` y `matplotlib`. Puedes instalarlas con el siguiente comando:

- pip install psutil matplotlib

## Uso

1. Clona este repositorio o descarga el script `monitor_proceso.py`.
2. Ejecuta el script desde la línea de comandos:
-python monitor_proceso.py
3. Ingresa la ruta del ejecutable que deseas monitorear cuando se te solicite.
4. El script creará un archivo `log_proceso.txt` que contiene los registros del consumo de CPU y memoria.
5. Una vez finalizado el proceso, se generará una gráfica con estos datos.

## Ejemplo de Salida

El archivo `log_proceso.txt` tendrá un formato similar al siguiente:

timestamp, CPU (%), Memoria (bytes)
1633035600, 25.4, 8458240
1633035605, 27.1, 8499200

Y se generará una gráfica mostrando estos datos a lo largo del tiempo.
   




