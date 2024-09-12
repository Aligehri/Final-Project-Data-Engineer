<p align='center'>
    <img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=0:ff0000,100:6400ff&text=Proyecto%20final%20Data%20Engineer&fontSize=59&fontAlign=50&fontAlignY=41&fontColor=00000000&stroke=00caa9&strokeWidth=2"/>
</p>

# Consigna

Script que extraiga datos de una API pública y crear la tabla en Redshift para posterior carga de sus datos en una base de datos de Amazon Redshift. Corre en un container de Docker y esta embebido en un DAG de Airflow dentro del container. Airflow está configurado para mandar alertas por correo.


# Descripción

Este script de Python se conecta a la API de Spotify para extraer datos de la playlist Epic & Melodic y cargarlos en Amazon Redshift mediante un contenedor de docker que ejecuta el programa en un Dag de Airflow.

# Requisitos

* Credenciales en Spotify Developers

* Credenciales de Amazon Redshift

* Cuenta de correo electrónico

# Instrucciones

0. **Clona el repositorio o abre un codespace**
```bash
git clone https://github.com/Aligehri/Final-Proyect-Data-Engineer.git
```
1. **Crea las carpetas necesarias**
```bash
   sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
```
2. **Crea y agrega credenciales para usar la api de Spotify**

Abre tu cuenta de spotify en el siguiente link:

https://developer.spotify.com/

Ve al dashboard y crea una app. Llena los campos necesarios, debería verse así:

![Ejemplo](/Images/ejemplo.png)

Después ve a los ajustes de tu app y copia el Client Id y el Client Secret que aprece en información básica.

Copialos y pegalos en el archivo Taskfile.yml con los siguientes nombres:

```bash

SPOTIPY_CLIENT_ID = ' '
SPOTIPY_CLIENT_SECRET = ' '

```
3. **Llena tus datos en el archivo Taskfile.yml**
```bash
        #Redshift Credentials:

        user_rs = ''
        pass_rs =  ''
        host_rs = ''
        port_rs = 5439
        database_rs = ''
        schema = ''
        
        #Email Info:
        EMAIL=
        EMAIL_PASSWORD=
        SMTP_HOST=smtp.gmail.com
        SMTP_STARTTLS=True
        SMTP_SSL=False
        SMTP_USER=
        SMTP_PASSWORD=
        SMTP_PORT=587
        SMTP_MAIL_FROM=

        #Spotify Credentials:
        SPOTIPY_CLIENT_ID = ''
        SPOTIPY_CLIENT_SECRET = ''
```
En el archivo ya está la plantilla con los datos que necesita.

4. **Ejecuta el siguiente código y espera a que finalice**
```bash
./bin/task start_project
```
5. **Abre la interfaz Airflow en el purto 8080**

6. **Agrega la conexión a Redshift en la interfaz de Airflowcon los mismos datos que agregaste en el archivo .env**

7. **Ejecuta el Dag en la interfaz de Airflow**


# Opcional

Puedes ejecutar el programa sin Docker y Airflow usando el archivo main.py en la carpeta dags, pero primero tienes que crear el entorno virtual e instalar los requeriments. 

```bash
cd dags
python main.py
```
<p align='center'>
    <img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=0:ff0000,100:6400ff&section=footer"/>
</p>
