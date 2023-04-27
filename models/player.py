import pandas as pd
import os

class Player():
    
    def __init__(self, nome='', pontos=0, partidas=0, moedas=0, media=0) -> None:
        self.__nome = nome
        self.__pontos = pontos
        self.__partidas = partidas
        self.__moedas = moedas
        self.__media = media
        
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def pontos(self):
        return self.__pontos
    
    @property
    def partidas(self):
        return self.__partidas
    
    @property
    def moedas(self):
        return self.__moedas
    
    @property
    def media(self):
        return self.__media
    
    @staticmethod
    def save_player(name:str, pontos:int, moedas:int) -> None:
        """ Função estática que salva/atualiza os dados de um jogador

        Args:
            name (str): Nome do jogador
            pontos (int): Pontuação do jogador
            moedas (int): Quantas moedas o jogador tem
        """
        jogadores = pd.read_excel('D:/Projetos/guessing-game-python/archives/players.xlsx',index_col='id')
        # jogadores = pd.read_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx',index_col='id')
        jogadores = pd.DataFrame(jogadores)
        player_data = jogadores.loc[jogadores['nome'] == name]
        index = player_data.index[0]
        jogadores.at[int(index),'nome']=name
        jogadores.at[int(index),'pontuacao'] += pontos
        jogadores.at[int(index),'moedas'] += moedas
        jogadores.at[int(index),'partidas'] += 1
        jogadores.at[int(index),'mediapontos'] = jogadores.at[int(index),'pontuacao'] / jogadores.at[int(index),'partidas']
        print(player_data)
 
        # os.remove('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')
        # csv_data = jogadores.to_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')
        os.remove('D:/Projetos/guessing-game-python/archives/players.xlsx')
        csv_data = jogadores.to_excel('D:/Projetos/guessing-game-python/archives/players.xlsx')

    
    def new_player(self) -> None:
        """
        Função que cria um novo jogador na base de dados
        """
        jogadores = pd.read_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx',index_col='id')
        jogadores = pd.DataFrame(jogadores)
        dados = [self.__nome, self.__pontos, self.__moedas, self.__partidas, self.__media]
    
        jogadores.loc[len(jogadores.index)] = dados
        
        # os.remove('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')
        # csv_data = jogadores.to_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')
        os.remove('D:/Projetos/guessing-game-python/archives/players.xlsx')
        csv_data = jogadores.to_excel('D:/Projetos/guessing-game-python/archives/players.xlsx')


