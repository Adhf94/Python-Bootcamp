from twilio.rest import Client
account_sid = 'SID'
auth_token = "AUTH TOKEN"



class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        message = self.client.messages.create(body=message,
                                              from_='whatsapp:+1',
                                              to='whatsapp:+1'
                                              )
        print(message.sid)