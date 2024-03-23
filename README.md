# api-fastapi

************************************************************************************************
## Proceso de Instalación
************************************************************************************************
***1. Debemos tener instalado Python3 y Git.*** 

***2. Descargamos el proyecto de github.***
```
git clone https://github.com/YilverQ/api-fastapi.git
cd api-fastapi
```

***3. Debemos instalar venv para trabajar con entornos virtuales de Python.***
```
sudo apt install python3-venv
```

***4. Creamos un entorno virtual de Python.*** 
```
python3 -m venv venv
```

***5. Activamos el entorno virtual de Python.*** 
```
source venv/bin/activate
```

***6. Instalamos las dependencias de Python***
```
pip install -r requirements.txt
```

***7. Configuramos las variables de entorno.*** 
```
cp .env.copy .env
nano .env
```

***8. Ejecutamos la aplicación.***
> Ejecutar la aplicación en forma de DEPLOY
```
python3 main.py #deploy
```
> Ejecutar la aplicación en forma de DEBUG
```
uvicorn main:app --reload #Debug
```

***9. URL para enviar correo.***
> Utilizar POSTMAN para enviar una petición.
```
http://localhost:8000/email/send
```

***10. Ejemplo para enviar un correo.***
> Enviar por método POST
```
{
    "to" : "user@gmail.com",
    "subject" : "Título del Correo",
    "body" : "Mensaje: Hola Mundo desde FastAPI"
}
```