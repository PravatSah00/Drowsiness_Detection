import playsound
import threading

class Alarm:
    def __init__(self):
        self.playing = False
        self.thread = None

    def play_sound(self):
        playsound.playsound(r"DataDir//Alarm//alarm.mp3")
        self.playing = False
    
    def play(self):
        if self.playing == False:
            self.playing = True
            self.thread = threading.Thread(target = self.play_sound)
            self.thread.start()
