import inquirer
import random

class Game():

    def __init__(self) -> None:
        self.__palavras = [
            {'tema': 'Carros', 'preco': 50, 'palavras': [
                {'palavra': 'Ferrari',
                 'dicas':
                 ['Carro vermelho mais famoso do mundo',
                  'O seu cirador se chamava Enzo']
                 },
                {'palavra': 'Fusca',
                 'dicas':
                 [
                    'A cor azul é a mais agressiva para esse carro',
                    'Um dos carros mais comuns do Brasil'
                 ]}
            ]},
            {'tema': 'Paises', 'preco': 20, 'palavras': {'palavra': 'Brasil',
                                                         'dicas':
                                                         ['País do futebol',
                                                          'Maior país da América do sul']
                                                         }},
        ]
        
        self.turn = 0

    def __choice_word(self) -> dict:
        """Função para escolher o tema e uma palavra do tema

        Returns:
            dict: Dicionário com a palavra sorteada e as dicas da mesma
        """
        
        # Armazenando todos os temas em uma variável para serem lidos pelo inquirer
        temas = []
        for tema in self.__palavras:
            temas.append(tema['tema'])
            
        questions = [
            inquirer.List(
                "theme",
                message="Qual tema você deseja jogar?",
                choices=[ t for t in temas],
            ),
        ]

        answers = inquirer.prompt(questions)

        palavra_dicas = {}
        
        #escolhe uma palavra do tema sorteado
        for themes in self.__palavras:
            if themes['tema'] == answers['theme']:
                palavra_dicas = random.choice(themes['palavras']) 
                break
                    
        return palavra_dicas
        
      
    def get_kick(self) -> str:
        """
        Função para armazenar qual o palpite do usuário para a palavra

        Returns:
            str: Palpite do usuário
        """
        
        ...  
        
    def play(self):
        palavra_sorteada = self.__choice_word()
        print(palavra_sorteada)


game = Game()
game.play()
