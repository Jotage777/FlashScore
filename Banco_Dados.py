from contextlib import closing
import sqlite3



def criar_BD() -> None:
    with sqlite3.connect('FlashScore.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')

            cursor.execute('''
                        CREATE TABLE Campeonato(
                            id_campeonato INTEGER primary key AUTOINCREMENT ,
                            name VARCHAR(45) NOT NULL
                            )'''
                           )
            cursor.execute('''
                                    CREATE TABLE Times(
                                        id_time INTEGER primary key AUTOINCREMENT ,
                                        name VARCHAR(45) NOT NULL
                                        )'''
                           )
            cursor.execute('''
                        CREATE TABLE Jogos(id_jogo VARCHAR (20) primary key ,
                                           casa VARCHAR(15) NOT NULL,
                                           resultado_casa INTEGER NOT NULL ,
                                           fora VARCHAR(15) NOT NULL ,
                                           resultado_fora INTEGER NOT NULL ,
                                           date VARCHAR(10) NOT NULL,
                                           rodada VARCHAR (30)NOT NULL,
                                           temporada VARCHAR (30)NOT NULL,
                                           posse_bola_casa VARCHAR (5) NOT NULL,
                                           posse_bola_fora VARCHAR (5) NOT NULL,
                                           tentativas_gol_casa INTEGER NOT NULL,
                                           tentativas_gol_fora INTEGER NOT NULL,
                                           finalizacoes_casa INTEGER NOT NULL,
                                           finalizacoes_fora INTEGER NOT NULL,
                                           chute_fora_casa INTEGER NOT NULL,
                                           chute_fora_fora INTEGER NOT NULL,
                                           chutes_bloqueados_casa INTEGER NOT NULL,
                                           chutes_bloqueados_fora INTEGER NOT NULL,
                                           faltas_cobradas_casa INTEGER NOT NULL,
                                           faltas_cobradas_fora INTEGER NOT NULL,
                                           escanteios_casa INTEGER NOT NULL,
                                           escanteios_fora INTEGER NOT NULL ,
                                           impedimentos_casa INTEGER NOT NULL ,
                                           impedimentos_fora INTEGER NOT NULL ,
                                           laterais_cobrados_casa INTEGER NOT NULL ,
                                           laterais_cobrados_fora INTEGER NOT NULL ,
                                           defesas_goleiro_casa INTEGER NOT NULL ,
                                           defesas_goleiro_fora INTEGER NOT NULL ,
                                           faltas_casa INTEGER NOT NULL,
                                           faltas_fora INTEGER NOT NULL ,
                                           cartoes_vermelhos_casa INTEGER NOT NULL ,                                       
                                           cartoes_vermelhos_fora INTEGER NOT NULL ,
                                           cartoes_amarelos_casa INTEGER NOT NULL ,
                                           cartoes_amarelos_fora INTEGER NOT NULL ,
                                           total_passes_casa INTEGER NOT NULL ,
                                           total_passes_fora INTEGER NOT NULL ,
                                           passes_completos_casa INTEGER NOT NULL ,
                                           passes_completos_fora INTEGER NOT NULL ,
                                           desarmes_casa INTEGER NOT NULL ,
                                           desarmes_fora INTEGER NOT NULL ,
                                           ataques_casa INTEGER NOT NULL ,
                                           ataques_fora INTEGER NOT NULL ,
                                           ataques_perigosos_casa INTEGER NOT NULL ,
                                           ataques_perigosos_fora INTEGER NOT NULL ,
                                           fk_id_campeonato INTEGER NOT NULL,
                                           FOREIGN KEY(fk_id_campeonato) REFERENCES Campeonato (id_campeonato))'''
                           )
            conn.commit()


def add_campeonato(campeonato: str) -> int:
    with sqlite3.connect('FlashScore.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_campeonato FROM Campeonato WHERE name = ?''',
                           (campeonato,))
            result = cursor.fetchone()
            if result == None:

                cursor.execute('''INSERT INTO Campeonato (name ) 
                                VALUES(?)''', (campeonato,))

                cursor.execute('''SELECT id_campeonato FROM Campeonato WHERE name = ?''',
                               (campeonato,))
                result = cursor.fetchone()
                conn.commit()
                return result[0]
            else:
                conn.commit()
                return result[0]

def add_times(time: str) -> int:
    with sqlite3.connect('FlashScore.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_time FROM Times WHERE name = ?''',
                           (time,))
            result = cursor.fetchone()
            if result == None:

                cursor.execute('''INSERT INTO Times (name ) 
                                VALUES(?)''', (time,))

                cursor.execute('''SELECT id_time FROM Times WHERE name = ?''',
                               (time,))
                result = cursor.fetchone()
                conn.commit()
                return result[0]
            else:
                conn.commit()
                return result[0]

def add_jogos(campeonato: int,id: str, casa: str, resultado_casa: int, fora: str, resultado_fora: int, data: str, rodada: str, temporada:str, posse_bola_casa: str, posse_bola_fora:str, tentativas_gol_casa: int, tentativas_gol_fora: int,
              finalizacoes_casa:int, finalizacoes_fora:int, chute_fora_casa:int,chute_fora_fora:int,chutes_bloqueados_casa:int,chutes_bloqueados_fora: int,faltas_cobradas_casa: int,
              faltas_cobradas_fora:int,escanteios_casa: int, escateios_fora: int,impedimentos_casa: int, impedimentos_fora: int, laterais_cobrados_casa:int, laterais_cobrados_fora: int,defesas_goleiro_casa:int,
              defesas_goleiros_fora:int,faltas_casa:int,faltas_fora:int,cartoes_vermelhos_casa:int,cartoes_vermelhos_fora:int,cartoes_amarelos_casa:int,cartoes_amarelos_fora:int,total_passes_casa: int,
              total_passes_fora: int, passes_completos_casa: int, passes_completos_fora: int, desarmes_casa:int, desarmes_fora:int, ataques_casa: int, ataques_fora: int, ataques_perigosos_casa: int,
              ataques_perigosos_fora: int) -> int:
    with sqlite3.connect('FlashScore.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_jogo FROM Jogos WHERE id_jogo = ?''',
                           (id,))
            result = cursor.fetchone()
            if result == None:
                fk_id_campeonato = add_campeonato(campeonato)
                add_times(casa)
                add_times(fora)

                cursor.execute('''INSERT INTO Jogos (id_jogo , casa , resultado_casa , fora , resultado_fora , date, rodada ,temporada, posse_bola_casa ,posse_bola_fora ,tentativas_gol_casa ,tentativas_gol_fora ,finalizacoes_casa ,
                                finalizacoes_fora , chute_fora_casa , chute_fora_fora , chutes_bloqueados_casa  ,chutes_bloqueados_fora ,faltas_cobradas_casa ,faltas_cobradas_fora ,escanteios_casa ,escanteios_fora ,impedimentos_casa ,
                                impedimentos_fora ,laterais_cobrados_casa ,laterais_cobrados_fora, defesas_goleiro_casa ,defesas_goleiro_fora,faltas_casa , faltas_fora,cartoes_vermelhos_casa ,cartoes_vermelhos_fora,cartoes_amarelos_casa,
                                cartoes_amarelos_fora ,total_passes_casa ,total_passes_fora , passes_completos_casa, passes_completos_fora, desarmes_casa ,desarmes_fora,ataques_casa ,ataques_fora ,ataques_perigosos_casa,ataques_perigosos_fora,
                                fk_id_campeonato)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                                                   
                                           ''',(id,casa,resultado_casa,fora,resultado_fora,data,rodada,temporada,posse_bola_casa,posse_bola_fora,tentativas_gol_casa,tentativas_gol_fora,finalizacoes_casa,finalizacoes_fora,chute_fora_casa,
                                                chute_fora_fora,chutes_bloqueados_casa,chutes_bloqueados_fora,faltas_cobradas_casa,faltas_cobradas_fora,escanteios_casa,escateios_fora,impedimentos_casa,impedimentos_fora,laterais_cobrados_casa,
                                                laterais_cobrados_fora,defesas_goleiro_casa,defesas_goleiros_fora,faltas_casa,faltas_fora,cartoes_vermelhos_casa,cartoes_vermelhos_fora,cartoes_amarelos_casa,cartoes_amarelos_fora,total_passes_casa,total_passes_fora,
                                                passes_completos_casa,passes_completos_fora,desarmes_casa,desarmes_fora,ataques_casa,ataques_fora,ataques_perigosos_casa,ataques_perigosos_fora, fk_id_campeonato))
                conn.commit()
            else:
                conn.commit()

def consultar_jogos_temporada(liga,temporada) -> int:
    with sqlite3.connect('FlashScore.db') as conn:
        with closing(conn.cursor()) as cursor:
            fk_id_campeonato = add_campeonato(liga)
            cursor.execute('''SELECT * FROM Jogos WHERE temporada=? AND fk_id_campeonato=? ''', (temporada,fk_id_campeonato,))
            result = cursor.fetchall()
            todos_jogos={}
            for i in range(len(result)):
                jogo={}
                jogo['casa']=result[i][1]
                jogo['resultado_casa']= result[i][2]
                jogo['fora'] = result[i][3]
                jogo['resultado_fora'] = result[i][4]
                jogo['data'] = result[i][5]
                jogo['rodada'] = result[i][6]
                jogo['temporada'] = result[i][7]
                jogo['posse_bola_casa'] = result[i][8]
                jogo['posse_bola_fora'] = result[i][9]
                jogo['tentativas_gol_casa'] = result[i][10]
                jogo['tentativas_gol_fora'] = result[i][11]
                jogo['finalizacoes_casa'] = result[i][12]
                jogo['finalizacoes_fora'] = result[i][13]
                jogo['chutes_fora_casa'] = result[i][14]
                jogo['chutes_fora_fora'] = result[i][15]
                jogo['chutes_bloqueados_casa'] = result[i][16]
                jogo['chutes_bloqueados_fora'] = result[i][17]
                jogo['faltas_cobradas_casa'] = result[i][18]
                jogo['faltas_cobradas_fora'] = result[i][19]
                jogo['escanteios_casa'] = result[i][20]
                jogo['escanteios_fora'] = result[i][21]
                jogo['impedimentos_casa'] = result[i][22]
                jogo['impedimentos_fora'] = result[i][23]
                jogo['laterais_cobrados_casa'] = result[i][24]
                jogo['laterais_cobrados_fora'] = result[i][25]
                jogo['defesas_goleiro_casa'] = result[i][26]
                jogo['defesas_goleiro_fora'] = result[i][27]
                jogo['faltas_casa'] = result[i][28]
                jogo['faltas_fora'] = result[i][29]
                jogo['cartoes_vermelhos_casa'] = result[i][30]
                jogo['cartoes_vermelhos_fora'] = result[i][31]
                jogo['cartoes_amarelos_casa'] = result[i][32]
                jogo['cartoes_amarelos_fora'] = result[i][33]
                jogo['total_passes_casa'] = result[i][34]
                jogo['total_passes_fora'] = result[i][35]
                jogo['passes_completos_casa'] = result[i][36]
                jogo['passes_completos_fora'] = result[i][37]
                jogo['dessarmes_casa'] = result[i][38]
                jogo['dessarmes_fora'] = result[i][39]
                jogo['ataques_casa'] = result[i][40]
                jogo['ataques_fora'] = result[i][41]
                jogo['ataques_perigosos_casa'] = result[i][42]
                jogo['ataques_perigosos_fora'] = result[i][43]
                todos_jogos[str(result[i][0])] = jogo


            return todos_jogos
