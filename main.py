# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACca8157bfad48832bce22fe7187b68a4d"
auth_token = "74f75f8debcba75c634e02bb5dcf6ddf"
client = Client(account_sid, auth_token) # Para ingresar se crea un objeto de la clase Client, colocando como atributos el token de autorizacion y el sid

message = client.messages.create( # Y Luego lo llamamos en una variable donde se crea el mensaje
  body="Mensaje de prueba Python", # Body: Contenido del mensaje
  from_="+13614267903", # Telefono virtual desde donde se envia
  to="+584121536554" # Telefono al que llega
)
print(message.sid)
