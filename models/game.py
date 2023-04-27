import inquirer
import random
from time import sleep
from models.player import Player
import pandas as pd

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
            {'tema': 'Paises', 'preco': 20, 'palavras': [
                {'palavra': 'BRASIL',
                    'dicas':
                    ['País do futebol',
                    'Maior país da América do sul',
                    'Pratos típicos como feijoada, churrasco e brigadeiro.',
                    'A dança mais famosa do país é o samba',
                    'A região amazônica é um importante patrimônio natural']
                },
                {'palavra': 'ESTADOS UNIDOS',
                 'dicas': [
                    'É considerado o país mais rico do mundo',
                    'País dos super-herois mais famosos',
                    'A culinária local inclui pratos icônicos como hambúrgueres, cachorros-quentes, pizza e donuts.',
                    'É o palco da maior competição de basquete do mundo, a NBA',
                    'A Estátua da Liberdade é um dos monumentos mais icônicos do país e um símbolo da liberdade e da democracia.'
                 ]},
                {'palavra': 'ALEMANHA',
                 'dicas': [
                    'Está localizado no centro do continente Europeu',
                    'Participou ativamente da Primeira e da Segunda guerra mundial',
                    'Seus pratos típicos são salsicha e cerveja',
                    'É o lar de várias empresas conhecidas internacionalmente, incluindo marcas de carros, como Mercedes-Benz e BMW, e empresas de tecnologia, como a SAP',
                    'A pais sede da Bosch.'
                 ]},
            ]
            },
            {'tema': 'Pessoas do Mundo da Tecnologia', 'preco': 20, 'palavras': [
                {'palavra': 'BILL GATES',
                    'dicas':
                    ['Ele já foi premiado com várias honrarias, incluindo a Ordem do Império Britânico e a Medalha Nacional de Tecnologia e Inovação dos Estados Unidos.',
                    'Juntamente com sua esposa, ele fundou uma das maiores organizações de caridade do mundo, que trabalha para combater a pobreza e melhorar a saúde global.',
                    'Largou Harvard para acreditar no sonho da sua própria empresa de softwares, seu primeiro contrato de sucesso foi com a IBM',
                    'Ficou durante anos como a pessoa mais rica do mundo, e continua estando no ranking dos mais ricos do mundo',
                    'A empresa fundada por ele, desenvolveu o sistema operacional mais utilizado hoje em dia']
                },
                {'palavra': 'STEVE JOBS',
                 'dicas': [
                    'Ele é conhecido por seu estilo de liderança único e inovador, que se concentra na criatividade e na simplicidade.',
                    'Ele fundou a Pixar Animation Studios, que produziu alguns dos filmes animados de maior sucesso da história.',
                    'Apesar de ser um grande profissional, ficou muito conhecido por ser muito exigente, causando pôlemicas com seus funcionários',
                    'Ele foi responsável por transformar a Apple em uma das empresas mais valiosas do mundo, com um valor de mercado que ultrapassou US$ 1 trilhão.',
                    'Ele foi o cofundador da Apple, uma das maiores empresas de tecnologia do mundo.'
                 ]},
                {'palavra': 'MARK ZUCKERBERG',
                 'dicas': [
                    'Ele é conhecido por sua visão empreendedora e por transformar a forma como as pessoas se conectam online.',
                    'Ele foi um dos mais jovens bilionários do mundo e atualmente é um dos mais ricos, com uma fortuna pessoal estimada em mais de US$ 100 bilhões.',
                    'Ele é conhecido por sua filantropia e já doou bilhões de dólares para causas de caridade através da Iniciativa Chan Zuckerberg.',
                    'Ainda na faculdade criou uma rede social, que no momento era apenas interna, para interagir entre seus colegas de faculdade',
                    'Ele é o fundador e CEO do Facebook, a maior rede social do mundo.'
                 ]},
            ]
            },
        ]
        
        self.__turn = 0
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
        """
         -> Função que verifica seo palpite dado pelo usuário, é a palavra correta, exibindo dica ou erro

        :palpite: str -> chute do usuário 
        :palavra: str -> palavra sorteada
        :dicas: list -> lista com as dicas da palavra 
        """
        
        if palpite != palavra:
            if self.__turn == 0:
                print(f'\033[31mTudo bem, é meio dificil acertar de primeira, aqui vai uma dica para te ajudar:\n\t{dicas[0]}\033[m')
            elif self.__turn == 1:
                print(f'\033[31mLá vai, a segunda dica é...\n\t{dicas[1]}\033[m')
            elif self.__turn == 2:
                print(f"\033[31mAgora é pra matar, mais uma dica:\t{dicas[2]}\033[m")
            elif self.__turn == 3:
                print(f"\033[31mVixi parece que as coisas estão meio complicadas hoje, para finalizar, lá vai outra dica:\n\t{dicas[3]}\033[m")
            elif self.__turn == 4 :
                print("\033[31mÉ agora ou nunca, ultima chance, ultima dica, se prepare!!\033[m")
                for i in range(3):
                    sleep(1)
                    print(f"\033[33m{i+1}\033[m")
                print(f"\t{dicas[4]}")
            self.__turn += 1
            if self.__turn > 5:
                return 'fim' 
        elif palpite == palavra:
            if self.__turn == 0:
               print("\033[1;32mMas que já!!!, você anda treinando né\ndepois dessa sou obrigado a te dar mais +25 pontos\033[m")
               self.__pontos += 25
            elif self.__turn == 1:
                print("\033[1;32mMuito bom, somente  uma dica, está muito bem de memória em!! \ntoma +20 pontos, você merece\033[m")
                self.__pontos += 20
            elif self.__turn == 2:
               print("\033[1;32mNada mal!! conseguiu mostrar toda sua eficiencia, +15 pontos para recompensar seu esforço\033[m")
               self.__pontos += 15
            elif self.__turn == 3:
               print("\033[1;32m'Foi difícil foi, foi intenso foi...', PARABÉNS!!! foi dificil mas você consegiu, lá vai +10 pontos\033[m")
               self.__pontos += 10
            elif self.__turn == 4:
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
            
            if check_word == 'fim':
                print('--------------PARTIDA FINALIZADA--------------')
                break
        Player.save_player(name=self.__jogador.nome,pontos=self.__pontos,moedas=self.__pontos)


    @staticmethod
    def list_ranking():
        # df = pd.read_excel('C:/Users/CT67CA/Desktop/guessing-game-python/archives/players.xlsx')
        df = pd.read_excel('D:/Projetos/guessing-game-python/archives/players.xlsx')
        top5 = df.loc[:,['nome','pontuacao','mediapontos']]
        top5 = top5.sort_values(by=['pontuacao'], ascending=False, na_position='last',ignore_index=True).head(5)
        
        print(top5)

if __name__ == '__main__':
    # Game.list_ranking()
    ...
