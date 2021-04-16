from twilio.rest import Client

TWILIO_SID = "twilio sid"
TWILIO_AUTH = "twilio auth"
TWILIO_VIRTUAL_NUM = "sending number"
TWILI_VERIFIED_NUM = "receiving number"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)