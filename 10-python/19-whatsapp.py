# T W I L I O

from twilio.rest import Client

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number   = 'whatsapp:+573103972370'
account_sid          = 'ACbe1b902dbf8f2918c80f6c9d931e2a98'
auth_token           = '32a1bf7bbbcad032f5c309b4ec7517a0'

client = Client(account_sid, auth_token)

def sendmessage(msj):
	client.messages.create(body =msj, 
			       from_=from_whatsapp_number,
			       to   =to_whatsapp_number )

sendmessage('Hola desde Python')
sendmessage('Usando Twilio para WhatsApp')

