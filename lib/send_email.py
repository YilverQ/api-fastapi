#Importamos las librerías necesarios. 
#No son necesarios instalarlos. Ya vienen instalados en Python.
import smtplib
from email.message import EmailMessage

#Importamos las librerias para obtener las variables de entorno.
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to, subject, body):
	"""·····························"""
	""" Datos para enviar el correo """
	"""·····························"""
	#Tema o asunto del correo. 
	email_subject = subject
	
	#Correo electrónico del 'servidor'. 
	sender_email_address = os.getenv("SENDER_EMAIL_ADDRESS")

	#Correo electrónico del 'recibiente'.
	receiver_email_address = to

	#Servidor de correo electrónico. GMAIL.
	email_smtp = os.getenv("EMAIL_SMTP")

	#Contraseña del correo. 
	email_password = os.getenv("EMAIL_PASSWORD")


	"""·······························"""
	""" Mensaje para enviar por email """
	"""·······························"""
	#Cremos un objeto de tipo Email.
	message = EmailMessage()

	#Configuramos la cabecera. 
	message['Subject'] = email_subject
	message['From'] = sender_email_address
	message['To'] = receiver_email_address

	#Agregamos la información del correo.
	message.set_content(body)


	"""·······························"""
	"""    Configuración del envío    """
	"""·······························"""
	#Puerto de correo SMTP
	port_email_smtp = os.getenv("PORT_EMAIL_STMP")

	#Servidor de Correo SMTP y Puerto
	server = smtplib.SMTP(email_smtp, port_email_smtp)

	#Identificar cliente al servidor SMTP. 
	server.ehlo()

	#Conexión segura SMTP.
	server.starttls()

	#Realizamos un login a nuestro correo electrónico.
	server.login(sender_email_address, email_password)

	#Enviamos el correo electrónico. 
	server.send_message(message)

	#Cerramos la conexión con el servidor. 
	server.quit()