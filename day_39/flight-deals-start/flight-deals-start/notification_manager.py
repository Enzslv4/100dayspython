from twilio.rest import Client
import requests

account_sid = 'AC6d5202cc63d426e612d82efb949a22bd'
auth_token = 'f5afe5a8bdde29913fdc625391bd1782'
client = Client(account_sid, auth_token)


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_sms(t):

        message = client.messages.create(
                from_='+14803861954',
                body=f'{t}',
                to='MY NUMB'      # Actually not working because of obvious reasons
            )
        print(message.status)