import requests
import time 

token = '5194591261:AAH6yDrLzQfbvioAdI0l2kUjZjhLt-PTOn0'
url_base = "http://api.telegram.org/bot{token}"


while True:

    r = requests.get(url_base + "/getUpdates")
    resposta_dict = r.json()

    print(resposta_dict)
    
    time.sleep(5)


    import requests
import time
import json


class TelegramBot:
    def __init__(self):
        token = '5194591261:AAH6yDrLzQfbvioAdI0l2kUjZjhLt-PTOn0'
        self.url_base = f'http://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            updates = self.obter_updates()
            dados = updates

            print(dados)

            print("--------------------------")
            #time.sleep(10)

    def obter_updates(self):
        link_api = self.url_base + "/getUpdates"
        r = requests.post(link_api)
        return r.json()

t = TelegramBot()
t.Iniciar()
    