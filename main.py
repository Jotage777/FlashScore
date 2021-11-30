from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import time
import Banco_Dados

def raspagemDados(navegador):
    # Acessando os jogos da premier League
    todos = navegador.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div/div/a').click()
    sleep(5)
    jogos = navegador.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]')
    html_content = jogos.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    casa = soup.find_all('div', class_='event__score event__score--home')
    fora = soup.find_all('div', class_='event__score event__score--away')
    cont=0
    ultimo=0
    #Pegando o id de cada jogo
    for rodada in soup.find_all('div', attrs={"class": "event__match event__match--static event__match--twoLine"}):
        if ultimo==9:
            cont+=1
            ultimo=0

        id_jogo=rodada['id']
        id_j = id_jogo[4:]
        #mudando o id na url
        caminho='https://www.flashscore.com.br/jogo/'+id_j+'/#resumo-de-jogo/estatisticas-de-jogo/0'
        raspagem_stats(caminho, casa[cont].get_text(), fora[cont].get_text(), id_j)
        cont+=1
        ultimo+=1

    cont=9
    #ultimo jogo de cada rodada
    for rod in soup.find_all('div', attrs={"class": "event__match event__match--static event__match--last event__match--twoLine"}):
        id_jog = rod['id']
        id_jj = id_jog[4:]
        caminho1 = 'https://www.flashscore.com.br/jogo/' + id_jj + '/#resumo-de-jogo/estatisticas-de-jogo/0'
        raspagem_stats(caminho1, casa[cont].get_text(), fora[cont].get_text(), id_jj)
        cont+=10





def raspagem_stats(url,home, away, id_jogo):
    nave=webdriver.Chrome()
    nave.get(url)
    sleep(5)

    jogo = nave.find_element_by_xpath('/html/body/div[2]/div')
    html_2 = jogo.get_attribute('outerHTML')
    soup2 = BeautifulSoup(html_2, 'html.parser')
    v=soup2.find_all('a')
    rodada = v[4]

    # Rodada

    times = soup2.find_all('div', class_='participant__participantName participant__overflow')

    data_hora = soup2.find_all('div', class_='duelParticipant__startTime')
    stats_name = soup2.find_all('div', class_='statCategoryName')
    casa_stats = soup2.find_all('div', class_='statHomeValue')
    fora_stats = soup2.find_all('div', class_='statAwayValue')
    print(stats_name[11].get_text())
    #Estatisticas
    if stats_name [11]  ==" Cartões vermelhos":
        if stats_name [12]  =="Cartões amarelos":
            Banco_Dados.add_jogos("Premier League", id_jogo,times[0].get_text(),home,times[1].get_text(),away,data_hora[0].get_text(),rodada.get_text(), casa_stats[0].get_text(),fora_stats[0].get_text(),
                                  int(casa_stats[1].get_text()),int(fora_stats[1].get_text()),int(casa_stats[2].get_text()),int(fora_stats[2].get_text()),int(casa_stats[3].get_text()),int(fora_stats[3].get_text()),int(casa_stats[4].get_text()),int(fora_stats[4].get_text())
            ,int(casa_stats[5].get_text()),int(fora_stats[5].get_text()),int(casa_stats[6].get_text()),int(fora_stats[6].get_text()),int(casa_stats[7].get_text()),int(fora_stats[7].get_text()),int(casa_stats[8].get_text()),int(fora_stats[8].get_text()),int(casa_stats[9].get_text()),int(fora_stats[9].get_text())
            ,int(casa_stats[10].get_text()),int(fora_stats[10].get_text() ),int(casa_stats[11].get_text()),int(fora_stats[11].get_text()),int(casa_stats[12].get_text()),int(fora_stats[12].get_text()),int(casa_stats[13].get_text()),int(fora_stats[13].get_text()),int(casa_stats[14].get_text()),int(fora_stats[14].get_text())
                                  ,int(casa_stats[15].get_text()),int(fora_stats[15].get_text()),int(casa_stats[16].get_text()),int(fora_stats[16].get_text()), int(casa_stats[17].get_text()), int(fora_stats[17].get_text()))
        else:
            Banco_Dados.add_jogos("Premier League", id_jogo, times[0].get_text(), home,
                                 times[1].get_text(), away, data_hora[0].get_text(),rodada.get_text(),
                                  casa_stats[0].get_text(), fora_stats[0].get_text()
                                  , int(casa_stats[1].get_text()), int(fora_stats[1].get_text()), int(casa_stats[2].get_text()), int(fora_stats[2].get_text()),
                                  int(casa_stats[3].get_text()), int(fora_stats[3].get_text()), int(casa_stats[4].get_text()), int(fora_stats[4].get_text())
                                  , int(casa_stats[5].get_text()), int(fora_stats[5].get_text()), int(casa_stats[6].get_text()), int(fora_stats[6].get_text()),
                                  int(casa_stats[7].get_text()), int(fora_stats[7].get_text()), int(casa_stats[8].get_text()), int(fora_stats[8].get_text()),
                                  int(casa_stats[9].get_text()), int(fora_stats[9].get_text())
                                  , int(casa_stats[10].get_text()), int(fora_stats[10].get_text()), 0, 0,
                                  int(casa_stats[11].get_text()), int(fora_stats[11].get_text()), int(casa_stats[12].get_text()), int(fora_stats[12].get_text()),
                                  int(casa_stats[13].get_text()), int(fora_stats[13].get_text())
                                  , int(casa_stats[14].get_text()), int(fora_stats[14].get_text()), int(casa_stats[15].get_text()), int(fora_stats[15].get_text()), int(casa_stats[16].get_text()), int(fora_stats[16].get_text()))
    elif stats_name [11]  =="Cartões amarelos":
        Banco_Dados.add_jogos("Premier League", id_jogo, times[0].get_text(), home,times[1].get_text(),
                              away, data_hora[0].get_text(),rodada.get_text(), casa_stats[0].get_text(), fora_stats[0].get_text()
                              , int(casa_stats[1].get_text()), int(fora_stats[1].get_text()), int(casa_stats[2].get_text()), int(fora_stats[2].get_text()),
                              int(casa_stats[3].get_text()), int(fora_stats[3].get_text()), int(casa_stats[4].get_text()), int(fora_stats[4].get_text())
                              , int(casa_stats[5].get_text()), int(fora_stats[5].get_text()), int(casa_stats[6].get_text()), int(fora_stats[6].get_text()),
                              int(casa_stats[7].get_text()), int(fora_stats[7].get_text()), int(casa_stats[8].get_text()), int(fora_stats[8].get_text()),
                              int(casa_stats[9].get_text()), int(fora_stats[9].get_text())
                              , 0, 0, int(casa_stats[10].get_text()), int(fora_stats[10].get_text()),
                              int(casa_stats[11].get_text()), int(fora_stats[11].get_text()), int(casa_stats[12].get_text()), int(fora_stats[12].get_text()),
                              int(casa_stats[13].get_text()), int(fora_stats[13].get_text())
                              , int(casa_stats[14].get_text()), int(fora_stats[14].get_text()), int(casa_stats[15].get_text()), int(fora_stats[15].get_text()), int(casa_stats[16].get_text()), int(fora_stats[16].get_text()))
    else:
        Banco_Dados.add_jogos("Premier League", id_jogo, times[0].get_text(), int(home), times[1].get_text(),
                              int(away), data_hora[0].get_text(),rodada.get_text(), casa_stats[0].get_text(), fora_stats[0].get_text()
                              , int(casa_stats[1].get_text()), int(fora_stats[1].get_text()), int(casa_stats[2].get_text()), int(fora_stats[2].get_text()),
                              int(casa_stats[3].get_text()), int(fora_stats[3].get_text()), int(casa_stats[4].get_text()), int(fora_stats[4].get_text())
                              , int(casa_stats[5].get_text()), int(fora_stats[5].get_text()), int(casa_stats[6].get_text()), int(fora_stats[6].get_text()),
                              int(casa_stats[7].get_text()), int(fora_stats[7].get_text()), int(casa_stats[8].get_text()), int(fora_stats[8].get_text()),
                              int(casa_stats[9].get_text()), int(fora_stats[9].get_text())
                              , 0,0,0,0 ,
                              int(casa_stats[10].get_text()), int(fora_stats[10].get_text()), int(casa_stats[11].get_text()), int(fora_stats[11].get_text()),
                              int(casa_stats[12].get_text()), int(fora_stats[12].get_text())
                              , int(casa_stats[13].get_text()), int(fora_stats[13].get_text()), int(casa_stats[14].get_text()), int(fora_stats[14].get_text()), int(casa_stats[15].get_text()), int(fora_stats[15].get_text()))




browser = webdriver.Chrome()


# Criando o banco de dados
create_db = not os.path.isfile('FlashScore.db')
if create_db:
  Banco_Dados.criar_BD()


# Acessando o flashScore
browser.get('https://www.flashscore.com.br/futebol/inglaterra/campeonato-ingles/resultados/')
sleep(5)
raspagemDados(browser)




