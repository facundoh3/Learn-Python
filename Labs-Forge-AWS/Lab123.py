# Puede utilizar Linux para realizar muchas tareas administrativas desde el terminal o desde la línea de comandos de Bash. Python proporciona varios módulos que también puede utilizar para ejecutar comandos en la línea de comandos. En este laboratorio, utilizará os.system() y subprocess.run() para ejecutar comandos de Bash desde Python.
#
# En este laboratorio, deberá realizar lo siguiente:

# utilizar os.system() para ejecutar un comando de Bash
# utilizar subprocess.run() para ejecutar comandos de Bash
import os
import subprocess


subprocess.run(stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None,
               timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

# Uso de subprocess.run con un argumento
os.system("ls")
# Uso de subprocess.run con dos argumentos
subprocess.run(["ls", "-l"])

# Uso de subprocess.run con tres argumentos
subprocess.run(["ls", "-l", "README.md"])

# Recuperación de información del sistema
command = "uname"
commandArgument = "-a"
print(
    f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Recuperación de información sobre el espacio en disco
command = "ps"
commandArgument = "-x"
print(
    f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])