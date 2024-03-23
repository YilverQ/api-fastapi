from fastapi import FastAPI
from routers import emailApp

#Instanciamos FastAPI
app = FastAPI()

#Incluimos todas las rutas.
app.include_router(emailApp)

#Rutas
@app.get('/')
async def routers():
    return {'detail'    : 'Home page',
            'message'   : 'Hello world from FastApi',
            'EmailApp'  : 'localhost:8000/email',
            'API doc'   : 'localhost:8000/docs',
            'redoc'     : 'localhost:8000/redoc',
            'JsonAPI'   : 'localhost:8000/openapi.json'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
