import pandas as pd
from models.player import Player
from models.game import Game
import inquirer

def get_players() -> pd.DataFrame:
    """esta função procura o arquivo excel com todos os jogadores

    Returns: pd.DataFrame
    """
    jogadores = pd.read_excel('archives\players.xlsx',index_col='id')
    return jogadores

def get_player_data() -> Player:
    """Esta função pega qual o nome do jogador e procura o mesmo na base de dados,
    caso encontre, retorna o objeto,
    caso não encontre, cria um novo registro e retorna o objeto

    Returns: Player -> Objeto do jogador
    """
    name = ''
    years = 0
    while True:
        name = input('Qual seu nome? ').upper()
        if len(name) < 3:
            print('Digite pelo menos seu primeiro nome')
        break
    while True:
        years = input('Digite sua idade: ')[0:2]
        try: 
            years = int(years)
        except:
            print("Digite apenas numeros")
            continue
        break

        
    players_table = get_players()
    players_name = list(players_table["nome"])
    if name in players_name:
        player_data = players_table.loc[players_table['nome'] == name]
        
        jogador = Player(nome=player_data['nome'].values[0],
                            pontos=player_data['pontuacao'].values[0],
                            partidas=player_data['partidas'].values[0],
                            moedas=player_data['moedas'].values[0],
                            media=player_data['mediapontos'].values[0],
                            idade=player_data['idade'].values[0])
        return jogador
    else:
        print('Criando novo jogador...')
        player_data = Player.create_player(nome=name,idade=years)
        player_data.new_player()
        return player_data

def menu(game: Game):
    """Função responsável por fazer o gerenciamento do menu do jogo

    Args:
        game (Game): Jogo ativo
    """
    options = [('Jogar','J'), ('Ver Ranking','R'), ('Atualizar meu nome', 'A')]
    questions = [
            inquirer.List(
                "option",
                message="Qual tema você deseja jogar?",
                choices=[ o for o in options],
            ),
        ]

    answers = inquirer.prompt(questions)

    if answers['option'] == 'J':
        game.play()
    elif answers['option'] == 'R':
        Game.list_ranking()
    elif answers['option'] == 'A':
        game.update_name()

    


#Pegar o nome do usuário e registrar na tabela
player = get_player_data()
game = Game(player)
while True:
    menu(game)