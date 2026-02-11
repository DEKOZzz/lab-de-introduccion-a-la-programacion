1. Creación de la carpeta del proyecto

El primer paso fue crear una carpeta llamada:

ejercicio.1

Esta carpeta funciona como el directorio principal del proyecto, donde se almacenan el entorno virtual y los archivos de Python.

📸 <img width="309" height="294" alt="pt 1" src="https://github.com/user-attachments/assets/ea4d6db5-b960-48a1-b685-462df85a155a" />


🧱 2. Creación del entorno virtual

Dentro de la carpeta ejercicio.1, se creó el entorno virtual usando el siguiente comando en PowerShell:

python -m venv env

Esto generó una carpeta llamada:

env/

La cual contiene todos los archivos necesarios para el entorno virtual.

📸 <img width="537" height="281" alt="pt 2" src="https://github.com/user-attachments/assets/7f6ddaa3-f6cf-45ae-98eb-c5da46144271" />



🔐 3. Permitir la ejecución de scripts en PowerShell

Antes de activar el entorno virtual, fue necesario permitir la ejecución de scripts en PowerShell, ya que Windows los bloquea por seguridad.

Se ejecutó el siguiente comando en PowerShell:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Después se confirmó la acción escribiendo:

Y


▶️ 4. Activación del entorno virtual

Una vez permitido ejecutar scripts, se activó el entorno virtual con el comando:

env\Scripts\activate

Cuando el entorno se activa correctamente, aparece (env) al inicio de la línea en la terminal.

Ejemplo:

(env) PS C:\Users\...\ejercicio.1>

📸<img width="546" height="229" alt="pt 3" src="https://github.com/user-attachments/assets/334f0e2c-22a3-4466-a8e9-9132af3d9e16" />


📦 5. Instalación de librerías

Con el entorno virtual activo, se instaló la librería numpy utilizando pip:

pip install numpy

Esta librería se instaló únicamente dentro del entorno virtual, no de forma global.

📸
<img width="540" height="207" alt="pt 4" src="https://github.com/user-attachments/assets/1235ad13-4cfb-474f-b620-963fb4bd8b80" />

📄 6. Creación del archivo Python

Dentro del proyecto se creó un archivo de Python llamado:

ejercicio.1.py

Este archivo está preparado para contener el código del ejercicio.
En este caso, el archivo no fue ejecutado, únicamente se creó como parte de la estructura del proyecto.

📸 <img width="858" height="251" alt="pt 5" src="https://github.com/user-attachments/assets/6499ac0a-8e5a-4f29-adb1-f4c86ea551ab" />


📂 7. Buenas prácticas con Git

Para evitar subir el entorno virtual a GitHub, se recomienda crear un archivo .gitignore y agregar la siguiente línea:

env/

Esto evita subir archivos innecesarios al repositorio.


🚀 Conclusión

En este ejercicio se logró:

Crear un proyecto en Python desde cero

Configurar un entorno virtual correctamente

Activar el entorno en PowerShell

Instalar librerías dentro del entorno virtual

Preparar el proyecto para subirse a GitHub


El uso de entornos virtuales es una práctica fundamental para trabajar de forma ordenada y profesional en Python.
