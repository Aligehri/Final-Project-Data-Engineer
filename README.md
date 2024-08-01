<p align="center" style="font-size: 3em;">
  <strong>Proyecto final del curso Data Engineer</strong>
</p>

# Primer consigna

Script que extraiga datos de una API pública y crear la tabla en Redshift para posterior carga de sus datos.

# Descripción

Este script de Python se conecta a la API de Spotify para extraer y analizar datos sobre la actividad musical del usuario. Las principales funcionalidades incluyen:

*Recopilación de Datos:

1. Obtiene las últimas 50 canciones reproducidas por el usuario.
2. Recupera el top 50 de canciones más escuchadas del usuario.
3. Identifica los 50 artistas más escuchados.

*Carga en Amazon Redshift:

Inserta los datos recopilados en una base de datos Amazon Redshift para su análisis y almacenamiento.

# Requisitos
* Cuenta en spotify

* Credenciales de amazon redshift

# Instrucciones

0. **Clona el repositorio o abre un codespace**
```bash
git clone https://github.com/Aligehri/Final-Proyect-Data-Engineer.git
```
1. **Crea un entorno virtual e instala las dependencias**
```bash
pip install -r requirements.txt
```
2. **Crea y agrega credenciales para usar la api de spotify y conectar con Redshift**

Abre tu cuenta de spotify en el siguiente link:

https://developer.spotify.com/

Ve al dashboard y crea una app. Llena los campos necesarios, debería verse así:

![Ejemplo](https://drive.google.com/file/d/1pH6brsI04qT9qDHVvutiTkagWFCRwrYf/view?usp=sharing)

Después ve a los ajustes de tu app y copia el Client Id y el Client Secret que aprece en información básica.

Copialos y pegalos en un archivo .env en la raíz del proyecto con los siguientes nombres:

```bash

SPOTIPY_CLIENT_ID = ' '
SPOTIPY_CLIENT_SECRET = ' '
SPOTIPY_REDIRECT_URI = ' '

#Información Redshift: 

user_rs = ' '
pass_rs =  ' '
host_rs = ' '
port_rs = '5439'
database_rs = ' '
```

3. **Ejecuta el programa**
```bash
python main.py
```

4. **Accede al link**

Inmediatamente después de ejecutar el programa, aparecerá un link. Debes acceder para ingresar a tu cuenta de Spotify y dar permiso a la app para que acceda a tu información de reproducción.

5. **Pega el link**
Después de autenticarte y dar permiso a la app, serás redirigido a otro link. Debes copiar y pegar el link en la Terminal, aunque la página mande un mensaje de error.