# Configurações iniciais
import pygame
import random

pygame.init()

pygame.display.set_caption("Snake in Python")

#  cria um tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura)) 

#  paramentros do jogo
relogio = pygame.time.Clock()
velocidade_jogo = 15

tamanho_quadrado = 10 

# Cores em RGB
preto = (0,0,0)
branca = (255, 255, 255)
vermelha = (255, 0,0 )
verde = (0, 255, 0)

def gerar_comida():
   pos_comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado) ) * float(tamanho_quadrado)  # equivale o tamanho do quadrado 
   pos_comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado) ) * float(tamanho_quadrado)  
   return pos_comida_x, pos_comida_y

def desenhar_comida(tamanho, pos_comida_x, pos_comida_y):
   pygame.draw.rect(tela, verde, [pos_comida_x, pos_comida_y, tamanho, tamanho])
   
def desenha_cobrinha(tamanho, pixels):
   for pixel in pixels:
      pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenha_pontuacao(pontuacao):
   fonte = pygame.font.SysFont("Helvetica", 20)
   texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
   tela.blit(texto, [1,1])

def seleciona_velocidade(tecla):
   
   if tecla == pygame.K_DOWN:
      velocidade_x = 0
      velocidade_y = tamanho_quadrado
      
   if tecla == pygame.K_UP:
      velocidade_x = 0
      velocidade_y = -tamanho_quadrado
      
   if tecla == pygame.K_RIGHT:
      velocidade_x = tamanho_quadrado
      velocidade_y = 0
      
   if tecla == pygame.K_LEFT:
      velocidade_x = -tamanho_quadrado
      velocidade_y = 0
   
   return velocidade_x, velocidade_y

def roda_jogo():
   fim_jogo = False
   
   x = largura / 2
   y = altura / 2
   
   velocidade_x = 0
   velocidade_y = 0
   
   tamanho_cobra = 1
   pixels = []
   
   pos_comida_x, pos_comida_y = gerar_comida()
   
   while not fim_jogo:
      
      tela.fill(preto)
      
      for evento in pygame.event.get(): # pega os inputs e interações do usuario
         if evento.type == pygame.QUIT:
            fim_jogo = True
         elif evento.type == pygame.KEYDOWN:
            velocidade_x, velocidade_y = seleciona_velocidade(evento.key) 
      
      
      desenhar_comida(tamanho_quadrado, pos_comida_x, pos_comida_y)
      
      # Atualizar a posição da cobra
      if x < 0 or x >= largura or y < 0 or y >= altura:
         fim_jogo = True
      
      x += velocidade_x
      y += velocidade_y
      
      
      pixels.append([x, y])
      if len(pixels) > tamanho_cobra:
         del pixels[0]
      
      # verifica se a cobra bateu nela mesma.
      for pixel in pixels[:-1]:
         if pixel == [x, y]: 
            fim_jogo = True
      
      desenha_cobrinha(tamanho_quadrado, pixels)
      desenha_pontuacao(tamanho_cobra - 1)
   
      
      # atualização da tela
      pygame.display.update()
      
      # Criar uma nova comida
      if x == pos_comida_x and y == pos_comida_y: # significa que a cobra comeu a comida
         tamanho_cobra +=1
         pos_comida_x, pos_comida_y = gerar_comida()
      
      relogio.tick(velocidade_jogo)
      
roda_jogo()