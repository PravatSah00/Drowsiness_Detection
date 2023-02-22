from twilio.rest import Client
import threading

keys = {
    "account_sid" : "AC78655bf7bad911618e8205127e8d888b",
    "auth_token"  : "5aa689050d565e01a31b916571e919fd",
    "twilio_number" : "+15405016107"
}

class SMS:
    def __init__(self) -> None:
        self.client = Client(keys["account_sid"], keys["auth_token"])
        self.cool_down_state = False
        self.sms_text = "This is a warning sms!!!!"
        try:
            with open(r"DataDir/UserData/user_number.ff") as contact:
                self.cotact =  contact.read()
        except:
            self.contact = ""

    def send_sms_from_client(self):
        try:
            message = self.client.messages.create(
                body = self.sms_text,
                from_ = keys["twilio_number"],
                to = "+91" + self.contact
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

