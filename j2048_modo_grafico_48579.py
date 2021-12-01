# ISEL - LEIM
#
# Jogo 2048 Interface gráfica
#
# Daniela Gonçalves - A48579 11D-A
#
import pygame

from j2048_motor_48579 import novo_jogo
from j2048_motor_48579 import valor
from j2048_motor_48579 import pontuacao
from j2048_motor_48579 import terminou
from j2048_motor_48579 import esquerda
from j2048_motor_48579 import direita
from j2048_motor_48579 import acima
from j2048_motor_48579 import abaixo

pygame.mixer.init()
pygame.mixer.pre_init(44100,16,2,4096) # Iniciação do mixer (frequencia, bits, saidas, buffer)
pygame.init()

# formatar os diferentes tipos de texto

def texto (pos, txt, color, f_size, bg_color):
    font = pygame.font.Font(None, f_size)
    text = font.render(txt,True,color,bg_color)
    screen.blit(text, pos) # blit inserir imagens sobre outras

# load audio para end_theme.mp3
def load_audio (mp3_path,volume,repeat):
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

# Volume
volume_end = 0.8


# Cores e tamanhos:

grey  = (40,40,40)
blue  = (0,180,255)
white = (255,255,255)
red   = (255,0,0)
fill_color = grey
pontuacao_texto = 80
gameover_size   = 30


# Criar uma janela gráfica:

largura = 900
altura  = 720
size    = [largura,altura]               # tamanho da janela
screen  = pygame.display.set_mode(size)  # abrir janela
pygame.display.set_caption("Jogo 2048 - Daniela Gonçalves") # nome da janela
clock = pygame.time.Clock()

#################   LOAD DAS IMAGENS USADAS ############################

background      = pygame.image.load("imgs/grelha_background.bmp")
botao_pontuacao = pygame.image.load("imgs/pontos_background2.bmp")
game_over       = pygame.image.load("imgs/game_over.bmp")

n2              = pygame.image.load("imgs/2.bmp")
n4              = pygame.image.load("imgs/4.bmp")
n8              = pygame.image.load("imgs/8.bmp")
n16             = pygame.image.load("imgs/16.bmp")
n32             = pygame.image.load("imgs/32.bmp")
n64             = pygame.image.load("imgs/64.bmp")
n128            = pygame.image.load("imgs/128.bmp")
n256            = pygame.image.load("imgs/256.bmp")
n512            = pygame.image.load("imgs/512.bmp")
n1024           = pygame.image.load("imgs/1024.bmp")
n2048           = pygame.image.load("imgs/2048.bmp")
n4096           = pygame.image.load("imgs/4096.bmp")

# imprime imagens na grelha comparando o valor de cada numero do tabuleiro de jogo a um dos valores possiveis,quando
# se verificar a condição imprime a imagem no respectivo local incrementando a posição para a posição seguinte no final.

def print_grelha_grafica(jogo):
    yi=91 # coordenada y inicial dos 1's elementos de cada coluna
    for linha in [1,2,3,4]:
        xi=203 # coordenada x inicial dos 1's elementos de cada linha
        for coluna in [1,2,3,4]:
            if valor(jogo, linha, coluna) == 2: 
                screen.blit(n2, [xi,yi])
            if valor(jogo, linha, coluna) == 4: 
                screen.blit(n4, [xi,yi])
            if valor(jogo, linha, coluna) == 8: 
                screen.blit(n8, [xi,yi])
            if valor(jogo, linha, coluna) == 16: 
                screen.blit(n16, [xi,yi])
            if valor(jogo, linha, coluna) == 32: 
                screen.blit(n32, [xi,yi])
            if valor(jogo, linha, coluna) == 64: 
                screen.blit(n64, [xi,yi])
            if valor(jogo, linha, coluna) == 128: 
                screen.blit(n128, [xi,yi])
            if valor(jogo, linha, coluna) == 256: 
                screen.blit(n256, [xi,yi])
            if valor(jogo, linha, coluna) == 512: 
                screen.blit(n512, [xi,yi])
            if valor(jogo, linha, coluna) == 1024: 
                screen.blit(n1024, [xi,yi])
            if valor(jogo, linha, coluna) == 2048: 
                screen.blit(n2048, [xi,yi])
            if valor(jogo, linha, coluna) == 4096: 
                screen.blit(n4096, [xi,yi])
            xi+=121 # incremento horizontal, quadricula + espaçamento
        yi+=121 # incremento vertical, quadricula + espaçamento
        
jogo = novo_jogo()

# gestao do jogo:

done = False
estado_jogo = 'jogo'
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:      
            done = True

        # estado fim:
        if estado_jogo == 'fim':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    estado_jogo = 'jogo'
                    jogo = novo_jogo()                    
        
        # estado jogo:    
        if estado_jogo == 'jogo':
            if event.type == pygame.KEYDOWN:
                
#################### MOVIMENTOS NA GRELHA ################################
                
                if event.key == pygame.K_LEFT:
                    
                    jogo=esquerda(jogo)
                    
                if event.key == pygame.K_RIGHT:
                    
                    jogo=direita(jogo)
                    
                if event.key == pygame.K_UP:
                    
                    jogo=acima(jogo)
                    
                if event.key == pygame.K_DOWN:
                    
                    jogo=abaixo(jogo)
                    

##################### NOVO JOGO ####################################################
                    
                if event.key == pygame.K_n:
                    estado_jogo == 'jogo'
                    jogo = novo_jogo()
                    
##################### SAIR DO JOGO  ###########################################
                    
                if event.key == pygame.K_q:
                    done = True
                    print("Fim")

##################### PRINT DO TABULEIRO ###########################################
                    
            screen.blit(background, [0,0]) 
            print_grelha_grafica(jogo)
            screen.blit(botao_pontuacao, [150,605])
            texto((500,630),str(jogo[3]),grey,pontuacao_texto,None)
            

#################### VERIFICA SE 2048 FOI ATINGIDO #################################

            # 2018/09/23 jbs - isto funciona mas não está muito bem. Devia usar-se get_vitoria
            for linha in [1,2,3,4]:
                for coluna in [1,2,3,4]:
                    if valor(jogo,linha,coluna) == 2048:
                        texto((50,10),"Muitos Parabéns!! Chegou ao elemento 2048!!", blue, 50,None)
            
                        
#################### VERIFICA SE O JOGADOR PERDEU ###################################
            
            if jogo[1] == True:
               
                load_audio("end_theme.mp3",volume_end,-1)
                estado_jogo = 'fim'
                texto((275,50),"Pressione Enter para tentar de novo", red, gameover_size,None)
                screen.blit(game_over, [115,250])
                
                
            
    pygame.display.flip()                   # limpar o estado da janela
    #clock.tick(20)                          # 20 frames por segundo
    clock.tick(10)                          # 2018/09/23 jbs - 10 frames por segundo

#Sair:
pygame.quit()
