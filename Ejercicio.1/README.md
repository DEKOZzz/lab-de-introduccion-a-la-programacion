1. Creación de la carpeta del proyecto

El primer paso fue crear una carpeta llamada:

ejercicio.1

Esta carpeta funciona como el directorio principal del proyecto, donde se almacenan el entorno virtual y los archivos de Python.

📸 Agregar captura de la carpeta creada aquí

🧱 2. Creación del entorno virtual

Dentro de la carpeta ejercicio.1, se creó el entorno virtual usando el siguiente comando en PowerShell:

python -m venv env

Esto generó una carpeta llamada:

env/

La cual contiene todos los archivos necesarios para el entorno virtual.

📸 Agregar captura del entorno virtual creado aquí

🔐 3. Permitir la ejecución de scripts en PowerShell

Antes de activar el entorno virtual, fue necesario permitir la ejecución de scripts en PowerShell, ya que Windows los bloquea por seguridad.

Se ejecutó el siguiente comando en PowerShell:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Después se confirmó la acción escribiendo:

Y

📸 Agregar captura del cambio de política aquí

▶️ 4. Activación del entorno virtual

Una vez permitido ejecutar scripts, se activó el entorno virtual con el comando:

env\Scripts\activate

Cuando el entorno se activa correctamente, aparece (env) al inicio de la línea en la terminal.

Ejemplo:

(env) PS C:\Users\...\ejercicio.1>

📸 Agregar captura del entorno virtual activo aquí

📦 5. Instalación de librerías

Con el entorno virtual activo, se instaló la librería numpy utilizando pip:

pip install numpy

Esta librería se instaló únicamente dentro del entorno virtual, no de forma global.

📸 Agregar captura de la instalación de numpy aquí

📄 6. Creación del archivo Python

Dentro del proyecto se creó un archivo de Python llamado:

ejercicio.1.py

Este archivo está preparado para contener el código del ejercicio.
En este caso, el archivo no fue ejecutado, únicamente se creó como parte de la estructura del proyecto.

📸 Agregar captura del archivo ejercicio.1.py aquí

📂 7. Buenas prácticas con Git

Para evitar subir el entorno virtual a GitHub, se recomienda crear un archivo .gitignore y agregar la siguiente línea:

env/

Esto evita subir archivos innecesarios al repositorio.

📸 Agregar captura del archivo .gitignore aquí

🚀 Conclusión

En este ejercicio se logró:

Crear un proyecto en Python desde cero

Configurar un entorno virtual correctamente

Activar el entorno en PowerShell

Instalar librerías dentro del entorno virtual

Preparar el proyecto para subirse a GitHub

El uso de entornos virtuales es una práctica fundamental para trabajar de forma ordenada y profesional en Python.