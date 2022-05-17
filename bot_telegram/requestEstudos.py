import requests

#resp = requests.get("https://viacep.com.br/ws/01001000/json/")

#print(resp.json())

#dd = resp.json()

#dt = resp.text

#print(dd)

def get_info_cep(cep):
    url_base = f'https://viacep.com.br/ws/{cep}/json/' 
    r = requests.get(url_base)   
    return r.json()


d = get_info_cep("08615000") #01001000

def retorna_rua(d):
    return d['logradouro']

#print(d)



def get_ticks(moeda = 'BTC',metodo= 'ticker'):
    url_base = f'https://www.mercadobitcoin.net/api/{moeda}/{metodo}/'
    r = requests.get(url_base)
    return r.json()

d1 = get_ticks('ETH')
#print(d1)

def get_movie(nome='matrix'):
    url_base = f'http://www.omdbapi.com/?apikey=8b4fe466&{nome}'
    r = requests.get(url_base)
    return r.json()

print(get_movie())

