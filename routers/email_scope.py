from fastapi import APIRouter
from lib import send_email 
from schema import Email


emailApp = APIRouter(prefix='/email',
                    tags=['EmailApp'])

#Rutas
@emailApp.get('/')
async def routers():
    return {'detail'    : 'EmailApp',
            'message'   : 'Aplicación para enviar correos electrónicos',
            'EmailApp'  : 'localhost:8000/email/info'}


#Información de la aplicación.
@emailApp.get('/info')
async def email_app_info():
    message = "Esto es una aplicación para enviar correos através de un servicio SMTP"
    return {'detail' : 'Email API',
            'message' : message}


#Enviamos un correo
@emailApp.post('/send', status_code=200)
async def email_send(email : Email):
    #Enviamos el correo electrónico.
    result = {'response' : '¡Mensaje enviado sastifactoriamente!'}
    return result