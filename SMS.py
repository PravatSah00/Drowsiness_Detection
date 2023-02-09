from twilio.rest import Client
import threading

keys = {
    "account_sid" : "AC78655bf7bad911618e8205127e8d888b",
    "auth_token"  : "e14e58020a5900a8adf28f834a5cbe58",
    "twilio_number" : "+15405016107"
}

class SMS:
    def __init__(self) -> None:
        self.client = Client(keys["account_sid"], keys["auth_token"])
        self.cool_down_state = False
        self.sms_text = "This is a warning sms!!!!"

    def send_sms_from_client(self):
        try:
            message = self.client.messages.create(
                body = self.sms_text,
                from_ = keys["twilio_number"],
                to = "+917384797488"
            )
        except:
            print("ERROR !!!! Massage could not sent.")
    
    def send(self):
        if self.cool_down_state == False:
            self.cool_down_state = True
            self.thread = threading.Thread(target = self.send_sms_from_client)
            self.thread.start()
        
    def cooldown(self):
        self.cool_down_state = False