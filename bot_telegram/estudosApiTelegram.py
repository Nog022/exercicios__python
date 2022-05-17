import requests
import time
import json


class TelegramBot:
    def __init__(self):
        token = '5217051724:AAF_8WZe4bjIEtX0NEbg-ZzoCA7nU43LocY'
        self.url_base = f'http://api.telegram.org/bot{token}'

    def Iniciar(self):
        update_id = None
        
        cont = 5
        while True:
            updates = self.obter_updates()
    
            dados = updates["result"]
            print(dados)

            #update_id = dados[0]['update_id']
            #print("Update ID = {}" .format(update_id))

            mensagem = dados[-1]["message"]["text"]
            chat_id_ = dados[-1]["message"]["from"]["id"]
            nome = dados[-1]["message"]["from"]["first_name"]

            print("Chat ID = {}" .format(chat_id_))
            print("Mensagem = {}" .format(mensagem))

            texto = f'Olá {nome} meu nome é Robô Telegram.'

            self.responder(texto, chat_id_)

            print('----------------------')
            time.sleep(5)
            cont -= 1

    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        return requests.get(link_requisicao)

    def obter_updates(self):
        link_api = self.url_base+"/getUpdates" #getMe
        r = requests.get(link_api)

        return r.json()

t = TelegramBot()
t.Iniciar()




