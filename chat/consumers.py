from channels.generic.websocket import WebsocketConsumer 
import threading 
from datetime import datetime 

class EchoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data='you are connected by websockets')
        def send_time(self):
            while True:
                self.send(text_data=str(datetime.now().Strftime("%H:%M:%S")))
                time.sleep(1)
        threading.Thread(target=send_time,args=(self)).start()
    def disconnect(self,close_code):
        pass 
    
    def receive(self,text_data):
        pass 
    