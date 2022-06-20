from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import time
from selenium.common.exceptions import NoSuchElementException

import Banco_Dados

def raspagemDados(navegador,liga,temporada):
    def raspagem_stats(id_jogo, liga, temporada):
        navegador.get('https://www.flashscore.com.br/jogo/'+id_jogo+'/#/resumo-de-jogo/estatisticas-de-jogo/0')
        time.sleep(1)
        jogo = navegador.find_element_by_xpath('/html/body/div[1]/div')
        html_2 = jogo.get_attribute('outerHTML')
        soup2 = BeautifulSoup(html_2, 'html.parser')
        rodada = soup2.find('span', class_='tournamentHeader__country').get_text()
        for i in range(len(rodada)):
            if rodada[i] == '-':
                rodada_camp = rodada[i+1:]
                break
        res = soup2.find_all('div', class_='detailScore__wrapper')
        ress = res[0].get_text()
        for i in range(len(ress)):
            if ress[i] == '-':
                res_casa = int(ress[:i])
                res_fora = int(ress[i + 1:])

        # Rodada
        # O nome de cada time
        times = soup2.find_all('div', class_='participant__participantName participant__overflow')
        # data e hora do jogo
        data_hora = soup2.find_all('div', class_='duelParticipant__startTime')
        # Nome de casa estatistica
        stats_name = soup2.find_all('div', class_='stat__categoryName')
        # Estatisticas do time da casa
        casa_stats = soup2.find_all('div', class_='stat__homeValue')
        # Estatistica do time de fora
        fora_stats = soup2.find_all('div', class_='stat__awayValue')
        # Lista com todos os nomes das estatisticas da partida
        nome_stats = ['Posse de bola', 'Tentativas de gol', 'Finalizações', 'Chutes fora', 'Chutes bloqueados',
                      'Faltas cobradas', 'Escanteios', 'Impedimentos', 'Laterais cobrados', 'Defesas do goleiro',
                      'Faltas', 'Cartões vermelhos',
                      'Cartões amarelos', 'Total de passes', 'Passes completados', 'Desarmes', 'Ataques',
                      'Ataques Perigosos']
        # lista para guardar as estatisticas do time da casa e de fora
        stats_partidas = []
        cont_stats = 0
        # Verificar se na partida estar contida todas as estatisticas, pois o site se não acontecer nenhum evento daquela estatistica, o mesmo não coloca aquela estatisca
        for i in range(18):
            if i == 0:
                if stats_name[cont_stats].get_text() == nome_stats[i]:
                    stats_partidas.append(casa_stats[cont_stats].get_text())
                    stats_partidas.append(fora_stats[cont_stats].get_text())
                    cont_stats += 1
                else:
                    stats_partidas.append('0')
                    stats_partidas.append('0')
            else:
                if stats_name[cont_stats].get_text() == nome_stats[i]:
                    transformar = int(casa_stats[cont_stats].get_text())
                    stats_partidas.append(transformar)
                    transformar = int(fora_stats[cont_stats].get_text())
                    stats_partidas.append(transformar)
                    cont_stats += 1
                else:
                    stats_partidas.append(0)
                    stats_partidas.append(0)

        Banco_Dados.add_jogos(liga, id_jogo, times[0].get_text(), res_casa, times[1].get_text(), res_fora,
                              data_hora[0].get_text(), rodada_camp, str(temporada), stats_partidas[0],
                              stats_partidas[1], stats_partidas[2], stats_partidas[3], stats_partidas[4],
                              stats_partidas[5], stats_partidas[6], stats_partidas[7], stats_partidas[8],
                              stats_partidas[9], stats_partidas[10], stats_partidas[11], stats_partidas[12],
                              stats_partidas[13], stats_partidas[14],
                              stats_partidas[15], stats_partidas[16], stats_partidas[17], stats_partidas[18],
                              stats_partidas[19], stats_partidas[20], stats_partidas[21], stats_partidas[22],
                              stats_partidas[23], stats_partidas[24],
                              stats_partidas[25], stats_partidas[26], stats_partidas[27], stats_partidas[28],
                              stats_partidas[29], stats_partidas[30], stats_partidas[31], stats_partidas[32],
                              stats_partidas[33], stats_partidas[34], stats_partidas[35])

    # Acessando os jogos da Liga escolhida
    cont = 0
    while True:
        try:
            if cont == 0:
                carregar= navegador.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/section/div[2]/div/a')
            elif cont ==4:
                break
            else:
                carregar = navegador.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div/div/a')

            while True:
                try:
                  carregar.click()
                  cont +=1
                except :
                    break
        except NoSuchElementException:
            break
    jogos = navegador.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div/div')
    html_content = jogos.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    cont = 0
    #Pegando o id de cada jogo
    for rodada in soup.find_all('div', attrs={"event__match event__match--static event__match--twoLine"} ):
        #Id de cada partida
        id_jogo=rodada['id']
        id_j = id_jogo[4:]
        #mudando o id na url
        raspagem_stats(id_j,liga,temporada)


    #Como a div da pagina para o ultimo jogo de cada rodada é diferente, temos que criar esse for para raspar os dados da ultima partida
    for rod in soup.find_all('div', attrs={"event__match event__match--static event__match--last event__match--twoLine"}):
        id_jog = rod['id']
        id_jj = id_jog[4:]
        raspagem_stats(id_jj,liga,temporada)
    navegador.quit()
