from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def raspagemDados(navegador):
    # Acessando os jogos da premier League
    jogos = navegador.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div')
    html_content = jogos.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    casa = soup.find_all('div', class_='event__score event__score--home')
    fora = soup.find_all('div', class_='event__score event__score--away')
    cont=0
    ultimo=0
    selc=0
    #Pegando o id de cada jogo
    for rodada in soup.find_all('div', attrs={"class": "event__match event__match--static event__match--twoLine"}):
        if ultimo==9:
            cont+=1
            ultimo=0

        id_jogo=rodada['id']
        id_j = id_jogo[4:]
        #mudando o id na url
        caminho='https://www.flashscore.com.br/jogo/'+id_j+'/#resumo-de-jogo/estatisticas-de-jogo/0'
        raspagem_stats(caminho, casa[cont].get_text(), fora[cont].get_text())
        cont+=1
        ultimo+=1
        print(ultimo)
    cont=9
    #ultimo jogo de cada rodada
    for rod in soup.find_all('div', attrs={"class": "event__match event__match--static event__match--last event__match--twoLine"}):
        id_jog = rod['id']
        id_jj = id_jog[4:]
        caminho1 = 'https://www.flashscore.com.br/jogo/' + id_jj + '/#resumo-de-jogo/estatisticas-de-jogo/0'
        raspagem_stats(caminho1, casa[cont].get_text(), fora[cont].get_text())
        cont+=10




def raspagem_stats(url,home, away):
    nave=webdriver.Chrome()
    nave.get(url)
    sleep(1)

    jogo = nave.find_element_by_xpath('/html/body/div[2]/div')
    html_2 = jogo.get_attribute('outerHTML')
    soup2 = BeautifulSoup(html_2, 'html.parser')
    v=soup2.find_all('a')
    rodada = v[4]
    print(rodada.get_text())
    times = soup2.find_all('div', class_='participant__participantName participant__overflow')
    print(times[0].get_text()," ", home, " x ",away, " ",times[1].get_text())
    stats_name = soup2.find_all('div', class_='statCategoryName')
    casa_stats = soup2.find_all('div', class_='statHomeValue')
    fora_stats = soup2.find_all('div', class_='statAwayValue')


    tamanho = len(stats_name)
    cont2=0
    for i in range(tamanho):
        print(stats_name[cont2].get_text(), " ", casa_stats[cont2].get_text(), " x ", fora_stats[cont2].get_text())
        cont2+=1
    print("-------------------------------------------------------------------------------------------------------------")



browser = webdriver.Chrome()


# Acessando o flashScore
browser.get('https://www.flashscore.com.br/futebol/inglaterra/campeonato-ingles/resultados/')
sleep(1)
raspagemDados(browser)





