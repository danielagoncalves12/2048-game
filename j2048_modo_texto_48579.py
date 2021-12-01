from j2048_motor_48579 import novo_jogo
from j2048_motor_48579 import valor
from j2048_motor_48579 import terminou
from j2048_motor_48579 import pontuacao
from j2048_motor_48579 import esquerda
from j2048_motor_48579 import direita
from j2048_motor_48579 import acima
from j2048_motor_48579 import abaixo
from j2048_motor_48579 import reverte_linhas
from j2048_motor_48579 import trocar_linhas_com_colunas

from j2048_gestor_48579 import le_identificacao
from j2048_gestor_48579 import inicializa_semente
from j2048_gestor_48579 import regista_grelha_inicial
from j2048_gestor_48579 import regista_jogada
from j2048_gestor_48579 import regista_pontos
from j2048_gestor_48579 import escreve_registo


def welcome():
    print('''jogo 2048
use as letras wasd para jogar
use a tecla n para iniciar um novo jogo
use a tecla q para terminar
a seguir a cada letra tem que carregar em enter/return
boa sorte!
''')

def alinha5(uma_string):
    while len(uma_string) < 5:
        uma_string = ' ' +uma_string
    return uma_string

def print_jogo(jogo):
    pontos = pontuacao(jogo)
    print('pontos = ' + str(pontos))

    for indice_linha in range(4):
        linha_string = ''
        for indice_coluna in range(4):
            linha_string = linha_string + alinha5(str(valor(jogo,
                                                    indice_linha+1,
                                                    indice_coluna+1))) + ' '
        print(linha_string)

welcome()
le_identificacao()
inicializa_semente(None)
jogo = novo_jogo()

regista_grelha_inicial(valor(jogo, 1, 1), valor(jogo, 1, 2), valor(jogo, 1, 3), valor(jogo, 1, 4),
                       valor(jogo, 2, 1), valor(jogo, 2, 2), valor(jogo, 2, 3), valor(jogo, 2, 4),
                       valor(jogo, 3, 1), valor(jogo, 3, 2), valor(jogo, 3, 3), valor(jogo, 3, 4),
                       valor(jogo, 4, 1), valor(jogo, 4, 2), valor(jogo, 4, 3), valor(jogo, 4, 4))
                       

print_jogo(jogo)

tecla = None

while (tecla != 'q') and (not terminou(jogo)):
    tecla = input()
    if tecla == 'n':
        regista_pontos(pontuacao(jogo))
        mensagem_cloud = escreve_registo()
        print(mensagem_cloud)
        le_identificacao()
        inicializa_semente(None)
        jogo = novo_jogo()
        regista_grelha_inicial(valor(jogo, 1, 1), valor(jogo, 1, 2), valor(jogo, 1, 3), valor(jogo, 1, 4),
                       valor(jogo, 2, 1), valor(jogo, 2, 2), valor(jogo, 2, 3), valor(jogo, 2, 4),
                       valor(jogo, 3, 1), valor(jogo, 3, 2), valor(jogo, 3, 3), valor(jogo, 3, 4),
                       valor(jogo, 4, 1), valor(jogo, 4, 2), valor(jogo, 4, 3), valor(jogo, 4, 4))

                               
    elif tecla == 'a':
        jogo = esquerda(jogo)
        regista_jogada(tecla)
        
    elif tecla == 'd':
        jogo = direita(jogo)
        regista_jogada(tecla)
        
    elif tecla == 'w':
        jogo = acima(jogo)
        regista_jogada(tecla)
        
    elif tecla == 's':
        jogo = abaixo(jogo)
        regista_jogada(tecla)
        
    print_jogo(jogo)
    
regista_pontos(pontuacao(jogo))
mensagem_cloud = escreve_registo()
