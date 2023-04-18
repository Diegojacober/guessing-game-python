import pandas as pd
import os

class Player():
    
    def __init__(self, nome='', pontos=0, partidas=0, moedas=0, media=0) -> None:
        self.__nome = nome
        self.__pontos = pontos
        self.__partidas = partidas
        self.__moedas = moedas
        self.__media = media
        
        
    def __str__(self):
        return f"Nome do jogador: {self.__nome}, pontos: {self.__pontos}"
    
    def save_player(self, name:str):
        jogadores = pd.read_excel('C:/Users/57761933898/Desktop/diego/guessing-game-python/archives/players.xlsx',index_col='id')
        jogadores = pd.DataFrame(jogadores)
        player_data = jogadores.loc[jogadores['nome'] == name]
        print(player_data)
        index = player_data.index[0]
        jogadores.at[int(index),'nome']='TESTE'
 
        os.remove("C:/Users/57761933898/Desktop/diego/guessing-game-python/archives/players.xlsx")
        csv_data = jogadores.to_excel('C:/Users/57761933898/Desktop/diego/guessing-game-python/archives/players.xlsx')
        
    
    def new_player(self):
        jogadores = pd.read_excel('C:/Users/57761933898/Desktop/diego/guessing-game-python/archives/players.xlsx',index_col='id')
        jogadores = pd.DataFrame(jogadores)
        dados = [self.__nome, self.__pontos, self.__moedas, self.__partidas, self.__media]
    
        jogadores.loc[len(jogadores.index)] = dados
        
        os.remove("C:/Users/57761933898/Desktop/diego/guessing-game-python/archives/players.xlsx")
        csv_data = jogadores.to_excel('C:/Users/57761933898/Desktop/diego/guessing-game-python/archives/players.xlsx')