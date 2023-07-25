###########################################################################################################################
##PARTE DUDA
# Importação das bibliotecas utilizadas no código.
import pygame
from pygame.locals import *
from sys import exit
from random import randint

#Inicialização das funções da biblioteca pygame.
pygame.init()

#Definição das variáveis utilizadas durante o código
largura = 1080
altura = 720

x_cobra = int(largura/2) 
y_cobra = int(altura/2) 

x_parede1 = int (largura/3)
y_parede1 = int(altura/3) 

velocidade = 10 
x_controle = velocidade 
y_controle = 0 

#Raddint -> irá gerar/sortear valores (posições) dentro de um determinado intervalo, isso fará com que a maçã mude de posição
x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0 

# Definição e formatação da fonte utilizada no jogo.
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

#Criação da superfície do jogo
tela = pygame.display.set_mode((largura, altura))

#Definição do nome que irá aparecer na janela do jogo
pygame.display.set_caption('Jogo da cobrinha')
relogio = pygame.time.Clock() 
#####################################################################################################################
##PARTE NATALIA
#Lista para armazenar todos os valores
lista_cobra = [] 
comprimento_inicial = 5 
morreu = False 

#Criando uma função para aumentar a cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))
#######################################################################################################################################################
####PARTE ARTHUR
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2) 
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False
#################################################################################################################################################################
###parte Letícia
#Criação do loop principal do jogo
while True:
    #Controlando a taxa de frames do jogo
    relogio.tick(30)
    #Preenchendo a superfície/tela com uma cor sólida, para não deixar um "rastro" do retângulo que representa a cobra
    tela.fill((255,255,255))
    
    #Definindo a mensagem que irá aparecer para o jogador para ele saber os seus pontos
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    
    #Loop for -> detecta se algum evento ocorreu. Nesse caso a condição craida é para o jogo fechar
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Definindo teclas do teclado para a mudança de direção
        if event.type == KEYDOWN:
				# condição: se selecionar a tecla A objeto move pra esquerda
            if event.key == K_a:
				#se a direção for positiva a tecla não vai ser bloqueada
                if x_controle == velocidade:
                    pass
				#se a direção for negativa a tecla vai ser bloqueada
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
#igualando a cobra a x e y para fazer ela se mover apenas na horizoontal e na vertical de maneira contínua
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

#Desenhando retângulos para representar a cobra, as maçãs e os obstáculos
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    parede1 = pygame.draw.rect(tela, (0,0,0), (x_parede1, y_parede1, 10,400))
#################################################################################################################################
#Parte da Ana
#Nessa parte, estamos apresentando um condição: Se a cobra colidir com a maçã, a maçã mudará de posição, será acrescido um ponto e o tamanho da cobra também irá aumentar
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        comprimento_inicial = comprimento_inicial + 1

#Armazena os valores atuais 
    lista_cabeca = []
    #Aramzenando valores da posição x
    lista_cabeca.append(x_cobra)
    #Armazenando valores da posição y
    lista_cabeca.append(y_cobra)
    
    #Recebe os valores da lista cabeça
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()                          
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            #Para exibição da mensagem na tela
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if cobra.colliderect(parede1):
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
 
        while morreu:
            tela.fill((255,255,255))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()                          
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo() 
#######################################################################################################################      
##PARTE ARTHUR
            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            #A cada interação com o loop principal, essa função irá atualizar a tela do jogo, para ele não travar após a primeira "rodada" 
            pygame.display.update()            
##########################################################################################################################
##PARTE DUDA
#Para a cobra conseguir não parar quando "bater" no final da tela e sim, "aparecer" do lado oposto em que saiu
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0
#######################################################################################################################
##PARTE NATALIA
#Para a cobra não ficar crescendo infinitamente 
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
##################################################################################################################################
##PARTE ARTHUR
    tela.blit(texto_formatado, (450,40))

    pygame.display.update()