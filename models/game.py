import inquirer
import random
from time import sleep
from models.player import Player

class Game():

    def __init__(self, jogador: Player) -> None:
        self.__palavras = [
            {'tema': 'Carros', 'preco': 50, 'palavras': [
                {'palavra': 'LAMBORGHINI AVENTADOR',
                 'dicas':
                 ['É um carro esportivo de luxo italiano.',
                  'Possui um motor V12 de alta performance.',
                  'Alcança uma velocidade máxima de mais de 350 km/h.',
                  'Possui portas do tipo "tesoura" que se abrem para cima.',
                  'É conhecido pelo seu design aerodinâmico e linhas agressivas.']
                 },
                {'palavra': 'MUSTANG',
                 'dicas':
                 [
                    'É um carro esportivo americano icônico.',
                    'Possui uma carroceria cupê ou conversível.',
                    'É conhecido por seu motor potente e ronco característico.',
                    'Tem uma história rica e uma legião de fãs dedicados.',
                    'Foi lançado pela primeira vez em 1964 e ainda é produzido atualmente.'
                 ]}
            ]},
            {'tema': 'Paises', 'preco': 20, 'palavras': {'palavra': 'Brasil',
                                                         'dicas':
                                                         ['País do futebol',
                                                          'Maior país da América do sul']
                                                         }},
        ]
        
        self.__turn = 1
        self.__pontos = 0
        self.__jogador = jogador

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
        
      
    def __get_kick(self) -> str:
        """
        Função para armazenar qual o palpite do usuário para a palavra

        Returns:
            str: Palpite do usuário
        """
        palpite = ''
        while True:
            palpite = input('Qual seu palpite? ').upper()
            if palpite == '' or palpite == ' ':
                print('\033[31m Digite alguma coisa, por favor\033[m')
                continue
            break
        return palpite
    
    def __check_word(self,palpite: str, palavra: str, dicas: list):
        
        if palpite != palavra:
            
            if self.__turn == 1:
                print(f'\033[31mTudo bem, é meio dificil acertar de primeira, aqui vai uma dica para te ajudar:\n\t{dicas[0]}\033[m')
            elif self.__turn == 2:
                print(f'\033[31mLá vai, a segunda dica é...\n\t{dicas[1]}\033[m')
            elif self.__turn == 3:
                print(f"\033[31mAgora é pra matar, mais uma dica:\t{dicas[2]}\033[m")
            elif self.__turn == 4:
                print(f"\033[31mVixi parece que as coisas estão meio complicadas hoje, para finalizar, lá vai outra dica:\n\t{dicas[3]}\033[m")
            elif self.__turn == 5 :
                print("\033[31mÉ agora ou nunca, ultima chance, ultima dica, se prepare!!\033[m")
                for i in range(3):
                    sleep(1)
                    print(f"\033[33m{i+1}\033[m")
                print(f"\t{dicas[4]}")
            self.__turn += 1
        elif palpite == palavra:
            if self.__turn == 1:
               print("\033[1;32mMas que já!!!, você anda treinando né\ndepois dessa sou obrigado a te dar mais +25 pontos\033[m")
               self.__pontos += 25
            elif self.__turn == 2:
                print("\033[1;32mMuito bom, somente  uma dica, está muito bem de memória em!! \ntoma +20 pontos, você merece\033[m")
                self.__pontos += 20
            elif self.__turn == 3:
               print("\033[1;32mNada mal!! conseguiu mostrar toda sua eficiencia, +15 pontos para recompensar seu esforço\033[m")
               self.__pontos += 15
            elif self.__turn == 4:
               print("\033[1;32m'Foi difícil foi, foi intenso foi...', PAREBÉNS!!! foi dificil mas você consegiu, lá vai +10 pontos\033[m")
               self.__pontos += 10
            elif self.__turn == 5:
                print("\033[1;32mPooorrrr poucooooo, raspou mas passou, o que importa é passar. Se fosse um boletim, você receberia um 5, então toma +5 pontos\033[m")
                self.__pontos += 5
                
            #salvar dados do jogador
            return 'fim'
        else:
            print(f"\033[31m Que pena... Não foi dessa vez, tente novamente!!\033[m")
            return 'fim'
        
    def play(self):
        palavra_sorteada = self.__choice_word()
        print(palavra_sorteada)
        
        while True:
            palpite = self.__get_kick()
            check_word = self.__check_word(palpite=palpite,palavra=palavra_sorteada['palavra'],dicas=palavra_sorteada['dicas'])
            
            if check_word == 'fim' or self.__turn == 6:
                print('--------------PARTIDA FINALIZADA--------------')
                break
        self.__jogador.save_player(name=self.__jogador.nome,pontos=self.__pontos,moedas=self.__pontos)


if __name__ == '__main__':
    game = Game()
    while True:
        game.play()
    
