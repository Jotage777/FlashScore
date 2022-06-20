from flask import Flask
from selenium import webdriver
from time import sleep
import time
import os
import Banco_Dados
import Raspagem
from flask import Flask, request
from flask_restful import Resource, Api

print("BETon: Uma plataforma para avaliação de estratégias de apostas no futebol")
print("Raspagem de dados do site FlashScore")
app = Flask(__name__)
api = Api(app)

class Raspagem_dados(Resource):
    def post(self):
        browser = webdriver.Chrome()
        if request.json['liga'] == 'inglaterra':
            browser.get('https://www.flashscore.com.br/futebol/inglaterra/campeonato-ingles-'+request.json['temporada'])
            time.sleep(1)
            Raspagem.raspagemDados(browser, 'Premier League',request.json['temporada'])
        elif request.json['liga'] == 'franca':
            browser.get('https://www.flashscore.com.br/futebol/franca/ligue-1-'+request.json['temporada'])
            time.sleep(1)
            Raspagem.raspagemDados(browser, 'Ligue 1', request.json['temporada'])
        elif request.json['liga'] == 'espanha':
            browser.get('https://www.flashscore.com.br/futebol/espanha/laliga-'+request.json['temporada'])
            time.sleep(1)
            Raspagem.raspagemDados(browser, 'LaLiga', request.json['temporada'])
        elif request.json['liga'] == 'italia':
            browser.get('https://www.flashscore.com.br/futebol/italia/serie-a-'+request.json['temporada'])
            time.sleep(1)
            Raspagem.raspagemDados(browser, 'Serie A', request.json['temporada'])
        elif request.json['liga'] == 'alemanha':
            browser.get('https://www.flashscore.com.br/futebol/alemanha/bundesliga-'+request.json['temporada'])
            time.sleep(1)
            Raspagem.raspagemDados(browser, 'Bundesliga', request.json['temporada'])
        elif request.json['liga'] == 'brasil':
            browser.get('https://www.flashscore.com.br/futebol/brasil/serie-a-'+request.json['temporada'])
            time.sleep(1)
            Raspagem.raspagemDados(browser, 'Campeonato Brasileiro', request.json['temporada'])
        return 200
class Coleta_dados(Resource):
    def get(self,liga,temporada):
        if liga =="inglaterra":
            jogos = Banco_Dados.consultar_jogos_temporada('Premier League',temporada)
        elif liga =="franca":
            jogos = Banco_Dados.consultar_jogos_temporada('Ligue 1',temporada)
        elif liga =="espanha":
            jogos = Banco_Dados.consultar_jogos_temporada('LaLiga',temporada)
        elif liga =="italia":
            jogos = Banco_Dados.consultar_jogos_temporada('Serie A',temporada)
        elif liga =="alemanha":
            jogos = Banco_Dados.consultar_jogos_temporada('Bundesliga',temporada)
        elif liga =="brasil":
            jogos = Banco_Dados.consultar_jogos_temporada('Campeonato Brasileiro',temporada)

        return jogos
api.add_resource(Raspagem_dados,"/adicionar/ligas")
api.add_resource(Coleta_dados,'/coletar/dados/<string:liga>/<string:temporada>')
# Criando o banco de dados
create_db = not os.path.isfile('FlashScore.db')
if create_db:
  Banco_Dados.criar_BD()
if __name__ == "__main__":
    app.run(debug=True)




