import pandas as pd
from models.player import Player

temas = ['Carros', 'Paises', 'Times do Brasil', 'Personagens de desenhos']

palavras = [
    {'palavra': 'Ferrari', 'dicas': ['Carro vermelho mais famoso do mundo'], 'tema_id': 0},
]

def get_players():
    jogadores = pd.read_excel('archives\players.xlsx',index_col='id')
    return jogadores

def get_player_data():
    name = ''
    while True:
        name = input('Qual seu nome? ').upper()
        if len(name) < 3:
            print('Digite pelo menos seu primeiro nome')
        else:
            players_table = get_players()
            players_name = list(players_table["nome"])
            if name in players_name:
                player_data = players_table.loc[players_table['nome'] == name]
                jogador = Player(nome=player_data['nome'],
                                 pontos=player_data['pontuacao'],
                                 partidas=player_data['partidas'],
                                 moedas=player_data['moedas'],
                                 media=['mediapontos'])
                # jogador.save_player(name=name)
                return jogador
            else:
                print('Criar novo jogador')
                # Criar novo jogador na tabela
                player_data = Player(nome=name)
                player_data.new_player()
            break

        
get_player_data()