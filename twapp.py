from twilio.rest import Client
from tw_creds import sid, token, phones, tw_cell, msg

client = Client(sid,token)
for number in phones:
  message = client.messages.create(to=number,from_=tw_cell,body=msg)

