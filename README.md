# api-fastapi

************************************************************************************************
****************** PROCESO DE INSTALACIÓN ******************************************************
************************************************************************************************
    1. Debemos tener instalado Python3 y Git. 

    2. Descargamos el proyecto de github.
        git clone https://github.com/YilverQ/api-fastapi.git
        cd api-fastapi

    3. Debemos instalar venv para trabajar con entornos virtuales de Python. 
        sudo apt install python3-venv

    4. Creamos un entorno virtual de Python. 
        python3 -m venv venv

    5. Activamos el entorno virtual de Python. 
        source venv/bin/activate

    6. Instalamos las dependencias de Python
        pip install -r requirements.txt

    7. Configuramos las variables de entorno. 
        cp .env.copy .env
        nano .env

    8. Ejecutamos el archivo main.py que contiene la aplicación.
    	python3 main.py #deploy
        uvicorn main:app --reload #Debug
