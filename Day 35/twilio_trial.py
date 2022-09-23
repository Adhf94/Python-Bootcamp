from twilio.rest import Client

account_sid = "your sid"
auth_token = "your token"
client = Client(account_sid, auth_token)
message = client.messages.create(
                              from_='whatsapp:+',
                              body='Va a llover, busca un paraguas.',
                              to='whatsapp:+'
                          )
print(message.sid)