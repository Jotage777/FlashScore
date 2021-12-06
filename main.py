from selenium import webdriver
from time import sleep
import os
import Banco_Dados
import Raspagem

print("BETon: Uma plataforma para avaliação de estratégias de apostas no futebol")
print("Raspagem de dados do site FlashScore")


def menu():
    while True :
        print("Menu")
        print("Digite 1 para realizar a raspagem de dados da Premier League")
        print("Digite 2 para realizar a raspagem de dados da Ligue 1")
        print("Digite 3 para realizar a raspagem de dados da LaLiga")
        print("Digite 4 para realizar a raspagem de dados da Budesliga")
        print("Digite 5 para realizar a raspagem de dados da Serie A")
        print("Digite 6 para sair do menu")
        escolha=int(input('Escolha uma das opções acima:'))
        if escolha == 1 or escolha==2 or escolha==3 or escolha==4 or escolha==5:
            browser = webdriver.Chrome()
            if escolha==1:
                browser.get('https://www.flashscore.com.br/futebol/inglaterra/campeonato-ingles/resultados/')
                sleep(5)
                Raspagem.raspagemDados(browser,'Premier League')
            elif escolha==2:
                browser.get('https://www.flashscore.com.br/futebol/franca/ligue-1/resultados/')
                sleep(5)
                Raspagem.raspagemDados(browser,'Ligue 1')
            elif escolha ==3:
                browser.get('https://www.flashscore.com.br/futebol/espanha/laliga/resultados/')
                sleep(5)
                Raspagem.raspagemDados(browser,'LaLiga')
            elif escolha ==4:
                browser.get('https://www.flashscore.com.br/futebol/alemanha/bundesliga/resultados/')
                sleep(5)
                Raspagem.raspagemDados(browser,'Budesliga')
            elif escolha ==5:
                browser.get('https://www.flashscore.com.br/futebol/italia/serie-a/resultados/')
                sleep(5)
                Raspagem.raspagemDados(browser,'Serie A')
        else:
            print("Escolha indisponivel, tente novamnete")




# Criando o banco de dados
create_db = not os.path.isfile('FlashScore.db')
if create_db:
  Banco_Dados.criar_BD()

#Chamando o menu
menu()





