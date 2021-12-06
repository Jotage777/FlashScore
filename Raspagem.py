from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import Banco_Dados

def raspagemDados(navegador,liga):
    # Acessando os jogos da premier League
    # A variável todos realiza um click na pagina para carregar todos os jogos da pagina
    todos = navegador.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div/div/a').click()
    sleep(5)
    #A variável jogos dar acesso ao html aonde os jogos estão

    jogos = navegador.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div')
    html_content = jogos.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    # a Variavel casa o resultado do time da casa
    casa = soup.find_all('div', class_='event__score event__score--home')
    # a Variavel fora o resultado do time de fora
    fora = soup.find_all('div', class_='event__score event__score--away')
    cont=0
    ultimo=0
    #Pegando o id de cada jogo
    for rodada in soup.find_all('div', attrs={"class": "event__match event__match--static event__match--twoLine"}):
        if ultimo==9:
            cont+=1
            ultimo=0
        #Id de cada partida
        id_jogo=rodada['id']
        id_j = id_jogo[4:]
        #mudando o id na url
        caminho='https://www.flashscore.com.br/jogo/'+id_j+'/#resumo-de-jogo/estatisticas-de-jogo/0'
        raspagem_stats(caminho, casa[cont].get_text(), fora[cont].get_text(), id_j,liga)
        cont+=1
        ultimo+=1

    cont=9
    #Como a div da pagina para o ultimo jogo de cada rodada é diferente, temos que criar esse for para raspar os dados da ultima partida
    for rod in soup.find_all('div', attrs={"class": "event__match event__match--static event__match--last event__match--twoLine"}):
        id_jog = rod['id']
        id_jj = id_jog[4:]
        caminho1 = 'https://www.flashscore.com.br/jogo/' + id_jj + '/#resumo-de-jogo/estatisticas-de-jogo/0'
        raspagem_stats(caminho1, casa[cont].get_text(), fora[cont].get_text(), id_jj,liga)
        cont+=10





def raspagem_stats(url,home, away, id_jogo,liga):
    nave=webdriver.Chrome()
    nave.get(url)
    sleep(5)

    jogo = nave.find_element_by_xpath('/html/body/div[2]/div')
    html_2 = jogo.get_attribute('outerHTML')
    soup2 = BeautifulSoup(html_2, 'html.parser')
    v=soup2.find_all('a')
    rodada = v[4]

    # Rodada
    # O nome de cada time
    times = soup2.find_all('div', class_='participant__participantName participant__overflow')
    #data e hora do jogo
    data_hora = soup2.find_all('div', class_='duelParticipant__startTime')
    #Nome de casa estatistica
    stats_name = soup2.find_all('div', class_='statCategoryName')
    # Estatisticas do time da casa
    casa_stats = soup2.find_all('div', class_='statHomeValue')
    #Estatistica do time de fora
    fora_stats = soup2.find_all('div', class_='statAwayValue')


    #Em alguns jogos não contem cartões e com isso o html não gera estatisticas dos mesmo e com isso os dados dos cartões tem que ser inseridos manualmente
    #Aqui verificamos se nessa posição das estatiscas estar localizado os cartões vermelhos
    if stats_name [11].get_text()  =="Cartões vermelhos":
        # Se existe algum cartão vermlho na partida, vericamos se nessa partida tambem houve cartões amarelos
        if stats_name [12].get_text()  =="Cartões amarelos":
            Banco_Dados.add_jogos(liga, id_jogo,times[0].get_text(),home,times[1].get_text(),away,data_hora[0].get_text(),rodada.get_text(), casa_stats[0].get_text(),fora_stats[0].get_text(),
                                  int(casa_stats[1].get_text()),int(fora_stats[1].get_text()),int(casa_stats[2].get_text()),int(fora_stats[2].get_text()),int(casa_stats[3].get_text()),int(fora_stats[3].get_text()),
                                  int(casa_stats[4].get_text()),int(fora_stats[4].get_text()),int(casa_stats[5].get_text()),int(fora_stats[5].get_text()),int(casa_stats[6].get_text()),int(fora_stats[6].get_text()),
                                  int(casa_stats[7].get_text()),int(fora_stats[7].get_text()),int(casa_stats[8].get_text()),int(fora_stats[8].get_text()),int(casa_stats[9].get_text()),int(fora_stats[9].get_text())
                                  ,int(casa_stats[10].get_text()),int(fora_stats[10].get_text() ),int(casa_stats[11].get_text()),int(fora_stats[11].get_text()),int(casa_stats[12].get_text()),int(fora_stats[12].get_text()),
                                  int(casa_stats[13].get_text()),int(fora_stats[13].get_text()),int(casa_stats[14].get_text()),int(fora_stats[14].get_text())
                                  ,int(casa_stats[15].get_text()),int(fora_stats[15].get_text()),int(casa_stats[16].get_text()),int(fora_stats[16].get_text()),int(casa_stats[17].get_text()),int(fora_stats[17].get_text()))
        # Se não houver adicionamos os cartões amarelos de modo manual
        else:

            Banco_Dados.add_jogos(liga, id_jogo, times[0].get_text(), home,
                                 times[1].get_text(), away, data_hora[0].get_text(),rodada.get_text(),
                                  casa_stats[0].get_text(), fora_stats[0].get_text()
                                  , int(casa_stats[1].get_text()), int(fora_stats[1].get_text()), int(casa_stats[2].get_text()), int(fora_stats[2].get_text()),
                                  int(casa_stats[3].get_text()), int(fora_stats[3].get_text()), int(casa_stats[4].get_text()), int(fora_stats[4].get_text())
                                  , int(casa_stats[5].get_text()), int(fora_stats[5].get_text()), int(casa_stats[6].get_text()), int(fora_stats[6].get_text()),
                                  int(casa_stats[7].get_text()), int(fora_stats[7].get_text()), int(casa_stats[8].get_text()), int(fora_stats[8].get_text()),
                                  int(casa_stats[9].get_text()), int(fora_stats[9].get_text()), int(casa_stats[10].get_text()), int(fora_stats[10].get_text()), 0, 0,
                                  int(casa_stats[11].get_text()), int(fora_stats[11].get_text()), int(casa_stats[12].get_text()), int(fora_stats[12].get_text()),
                                  int(casa_stats[13].get_text()), int(fora_stats[13].get_text()), int(casa_stats[14].get_text()), int(fora_stats[14].get_text()),
                                  int(casa_stats[15].get_text()), int(fora_stats[15].get_text()),int(casa_stats[16].get_text()),int(fora_stats[16].get_text()))
    # Se não existir cartão vermelho na partida mas houver amarelos, inserimos os cartçoes vermelhos de modo manual
    elif stats_name [11].get_text() =="Cartões amarelos":

        Banco_Dados.add_jogos(liga, id_jogo, times[0].get_text(), home,times[1].get_text(),
                              away, data_hora[0].get_text(),rodada.get_text(), casa_stats[0].get_text(), fora_stats[0].get_text()
                              , int(casa_stats[1].get_text()), int(fora_stats[1].get_text()), int(casa_stats[2].get_text()), int(fora_stats[2].get_text()),
                              int(casa_stats[3].get_text()), int(fora_stats[3].get_text()), int(casa_stats[4].get_text()), int(fora_stats[4].get_text())
                              , int(casa_stats[5].get_text()), int(fora_stats[5].get_text()), int(casa_stats[6].get_text()), int(fora_stats[6].get_text()),
                              int(casa_stats[7].get_text()), int(fora_stats[7].get_text()), int(casa_stats[8].get_text()), int(fora_stats[8].get_text()),
                              int(casa_stats[9].get_text()), int(fora_stats[9].get_text()), int(casa_stats[10].get_text()), int(fora_stats[10].get_text()),0,0,
                              int(casa_stats[11].get_text()), int(fora_stats[11].get_text()), int(casa_stats[12].get_text()), int(fora_stats[12].get_text()),
                              int(casa_stats[13].get_text()), int(fora_stats[13].get_text()), int(casa_stats[14].get_text()), int(fora_stats[14].get_text()),
                              int(casa_stats[15].get_text()), int(fora_stats[15].get_text()),int(casa_stats[16].get_text()),int(fora_stats[16].get_text()))
    # E no ultimo caso se não existir cartões na partida, inserimos os amarelos e vermelhos de modo manual
    else:
        Banco_Dados.add_jogos(liga, id_jogo, times[0].get_text(), int(home), times[1].get_text(),
                              int(away), data_hora[0].get_text(),rodada.get_text(), casa_stats[0].get_text(), fora_stats[0].get_text()
                              , int(casa_stats[1].get_text()), int(fora_stats[1].get_text()), int(casa_stats[2].get_text()), int(fora_stats[2].get_text()),
                              int(casa_stats[3].get_text()), int(fora_stats[3].get_text()), int(casa_stats[4].get_text()), int(fora_stats[4].get_text())
                              , int(casa_stats[5].get_text()), int(fora_stats[5].get_text()), int(casa_stats[6].get_text()), int(fora_stats[6].get_text()),
                              int(casa_stats[7].get_text()), int(fora_stats[7].get_text()), int(casa_stats[8].get_text()), int(fora_stats[8].get_text()),
                              int(casa_stats[9].get_text()), int(fora_stats[9].get_text()), 0,0,0,0 ,int(casa_stats[10].get_text()), int(fora_stats[10].get_text()),
                              int(casa_stats[11].get_text()), int(fora_stats[11].get_text()),int(casa_stats[12].get_text()), int(fora_stats[12].get_text())
                              ,int(casa_stats[13].get_text()), int(fora_stats[13].get_text()), int(casa_stats[14].get_text()),
                              int(fora_stats[14].get_text()),int(casa_stats[15].get_text()),int(fora_stats[15].get_text()))

