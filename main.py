import pandas as pd
from models.player import Player

temas = ['Carros', 'Paises', 'Times do Brasil', 'Personagens de desenhos']

palavras = [
    {'palavra': 'Ferrari', 'dicas': ['Carro vermelho mais famoso do mundo'], 'tema_id': 0},
]

def get_players():
    jogadores = pd.read_excel('archives\players.xlsx',index_col='id')
    return jogadores

def get_player_data() -> Player:
    """Esta função pega qual o nome do jogador e procura o mesmo na base de dados,
    caso encontre, retorna o objeto,
    caso não encontre, cria um novo registro e retorna o objeto

    Returns: Player -> Objeto do jogador
    """
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
                
                jogador = Player(nome=player_data['nome'].values[0],
                                 pontos=player_data['pontuacao'].values[0],
                                 partidas=player_data['partidas'].values[0],
                                 moedas=player_data['moedas'].values[0],
                                 media=player_data['mediapontos'].values[0])
                # jogador.save_player(name=name)
                return jogador
            else:
                print('Criando novo jogador...')
                player_data = Player(nome=name)
                player_data.new_player()
                return player_data

        
player = get_player_data()
