from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import Banco_Dados

def raspagemDados(navegador,liga):
    # Acessando os jogos da Liga escolhida
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
    stats_partidas=[]
    cont_stats=0
    #Verificar se na partida estar contida todas as estatisticas, pois o site se não acontecer nenhum evento daquela estatistica, o mesmo não coloca aquela estatisca
    for i in range(18):
        if i == 0:
            if stats_name[cont_stats].get_text()=='Posse de bola':
                stats_partidas.append(casa_stats[cont_stats].get_text())
                stats_partidas.append(fora_stats[cont_stats].get_text())
                cont_stats+=1
            else:
                stats_partidas.append('0')
                stats_partidas.append('0')
        elif i == 1:
            if stats_name[cont_stats].get_text()=='Tentativas de gol':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats+=1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 2:
            if stats_name[cont_stats].get_text() == 'Finalizações':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 3:
            if stats_name[cont_stats].get_text() == 'Chutes fora':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 4:
            if stats_name[cont_stats].get_text() == 'Chutes bloqueados':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 5:
            if stats_name[cont_stats].get_text() == 'Faltas cobradas':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 6:
            if stats_name[cont_stats].get_text() == 'Escanteios':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 7:
            if stats_name[cont_stats].get_text() == 'Impedimentos':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 8:
            if stats_name[cont_stats].get_text() == 'Laterais cobrados':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 9:
            if stats_name[cont_stats].get_text() == 'Defesas do goleiro':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 10:
            if stats_name[cont_stats].get_text() == 'Faltas':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 11:
            if stats_name[cont_stats].get_text() == 'Cartões vermelhos':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 12:
            if stats_name[cont_stats].get_text() == 'Cartões amarelos':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 13:
            if stats_name[cont_stats].get_text() == 'Total de passes':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 14:
            if stats_name[cont_stats].get_text() == 'Passes completados':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 15:
            if stats_name[cont_stats].get_text() == 'Desarmes':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 16:
            if stats_name[cont_stats].get_text() == 'Ataques':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)
        elif i == 17:
            if stats_name[cont_stats].get_text() == 'Ataques Perigosos':
                transformar = int(casa_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                transformar = int(fora_stats[cont_stats].get_text())
                stats_partidas.append(transformar)
                cont_stats += 1
            else:
                stats_partidas.append(0)
                stats_partidas.append(0)

    Banco_Dados.add_jogos(liga, id_jogo,times[0].get_text(),home,times[1].get_text(),away,data_hora[0].get_text(),rodada.get_text(),stats_partidas[0],stats_partidas[1],stats_partidas[2],stats_partidas[3],stats_partidas[4],
                          stats_partidas[5],stats_partidas[6],stats_partidas[7],stats_partidas[8],stats_partidas[9],stats_partidas[10],stats_partidas[11],stats_partidas[12],stats_partidas[13],stats_partidas[14],
                          stats_partidas[15],stats_partidas[16],stats_partidas[17],stats_partidas[18],stats_partidas[19],stats_partidas[20],stats_partidas[21],stats_partidas[22],stats_partidas[23],stats_partidas[24],
                          stats_partidas[25],stats_partidas[26],stats_partidas[27],stats_partidas[28],stats_partidas[29],stats_partidas[30],stats_partidas[31],stats_partidas[32],stats_partidas[33],stats_partidas[34],stats_partidas[35])
