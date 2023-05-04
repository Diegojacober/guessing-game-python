from models.Person import Person
import pandas as pd
import os

class Player(Person):
    
    def __init__(self, nome:str ='', pontos: float = 0, partidas: int = 0, moedas: float = 0, media: float = 0, idade: int = 18) -> None:
        super().__init__(nome, idade)
        self.__pontos = pontos
        self.__partidas = partidas
        self.__moedas = moedas
        self.__media = media
        

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


    @classmethod
    def create_player(cls,nome: str, idade:int):
        return cls(nome, 0, 0, 0, 0, idade)

    
    @staticmethod
    def save_player(name:str, pontos:int, moedas:int, idade: int, nome_antigo = '') -> None:
        """ Função estática que salva/atualiza os dados de um jogador

        Args:
            name (str): Nome do jogador
            pontos (int): Pontuação do jogador
            moedas (int): Quantas moedas o jogador tem
        """
       
        jogadores = pd.read_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx',index_col='id')
        jogadores = pd.DataFrame(jogadores)
        if nome_antigo == '':
            player_data = jogadores.loc[jogadores['nome'] == name.upper()]
            index = player_data.index[0]
            jogadores.at[int(index),'nome']= name
            jogadores.at[int(index),'idade']= idade
            jogadores.at[int(index),'pontuacao'] += pontos
            jogadores.at[int(index),'moedas'] += moedas
            jogadores.at[int(index),'partidas'] += 1
            jogadores.at[int(index),'mediapontos'] = jogadores.at[int(index),'pontuacao'] / jogadores.at[int(index),'partidas']
        else:
            player_data = jogadores.loc[jogadores['nome'] == nome_antigo.upper()]
            index = player_data.index[0]
            jogadores.at[int(index),'nome']= name
            jogadores.at[int(index),'idade']= idade
            jogadores.at[int(index),'pontuacao'] += pontos
            jogadores.at[int(index),'moedas'] += moedas
            jogadores.at[int(index),'partidas'] += 1
            jogadores.at[int(index),'mediapontos'] = jogadores.at[int(index),'pontuacao'] / jogadores.at[int(index),'partidas']
 
    
        os.remove('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')
        excel_data = jogadores.to_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')

    def modify_name(self, new_name,nome_antigo):
        if new_name == self._name:
            print('Nome atualizado com sucesso!!!')
        else:
            Person.name = new_name
            self.save_player(name=Person.name, pontos=self.__pontos,idade=self._years, moedas=self.__moedas,nome_antigo=nome_antigo)
            print("Nome atualizado com sucesso!!!")

    def new_player(self) -> None:
        """
        Função que cria um novo jogador na base de dados
        """
        jogadores = pd.read_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx',index_col='id')
        jogadores = pd.DataFrame(jogadores)
        dados = [self._name, self.__pontos, self.__moedas, self.__partidas, self.__media, self._years]
    
        jogadores.loc[len(jogadores.index)] = dados

        os.remove('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')
        excel_data = jogadores.to_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')


