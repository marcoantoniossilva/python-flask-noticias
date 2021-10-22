import urllib.request, json, time
import pandas as pd

from servico import IS_ALIVE, JOGATINA, SISTEMAS_OPERACIONAIS

# Constantes de rotas do serviço de notícias
URL_SERVICO = "http://127.0.0.1:5000/"
IS_ALIVE = URL_SERVICO + "isAlive/"
JOGATINA = URL_SERVICO + "jogatina/"
SISTEMAS_OPERACIONAIS = URL_SERVICO + "sistemas/"

def acessar(url):
    print("Acessando a url: ",url)
    resposta = urllib.request.urlopen(url)
    return resposta.read().decode("utf-8")
    
def is_alive():
    return acessar(IS_ALIVE) == "yes"

def imprimir_noticias(noticias):
    print(pd.DataFrame(noticias).T)

def get_jogatina():
    return json.loads(acessar(JOGATINA))

def get_sistemas():
    return json.loads(acessar(SISTEMAS_OPERACIONAIS))

# Verifica se o serviço está no ar (is_alive)
if __name__ == '__main__':
    while True:
        if is_alive():
            print("O serviço está respondendo, acessando notícias...")
            print("Notícias sobre jogos:")
            imprimir_noticias(get_jogatina())
            print("Notícias sobre sistemas operacionais:")
            imprimir_noticias(get_sistemas())
        else:
            print("O serviço não está ativo!")
        time.sleep(5)