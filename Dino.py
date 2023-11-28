import pygame # Importa a biblioteca py games
from pygame.locals import *
from sys import exit
import os # Importa biblioteca os
from random import randrange

diretorio_principal = os.path.dirname(__file__) # Encontra o caminho onde o arquivo está
diretorio_imagens = os.path.join(diretorio_principal, 'imagens') # Encontra a pasta das imagens
diretorio_sons = os.path.join(diretorio_principal, 'sons') # encontra a pasta de sons

LARGURA = 640 # Valor da Largura e altura
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Dino Game Mario Edition') # nome do jogo

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'spritesheet.png')).convert_alpha() # convert_alpha = método de conservar transparencia da imagem 
# Inserir as sprites
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = [] # Cria Lista
        for i in range(3): # Cria um loop que aumenta a escala do sprite
            img = sprite_sheet.subsurface((i*32,0), (32,32)) # Intercala os sprites
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)
        
        # Cria a animação de camninhar/correr do dinossauro
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)]

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32,0), (32,32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.x = LARGURA - randrange(30, 300, 90)
        self.altura_nuvem()

    def altura_nuvem(self):
        self.rect.y = randrange(50, 200, 50)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA 
            self.altura_nuvem()
        self.rect.x -= 10

todas_as_sprites = pygame.sprite.Group() # Grupo de sprites
dino = Dino()
todas_as_sprites.add(dino)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30) # Define os frames
    tela.fill(BRANCO) # Pinta a tela de Branco
    for event in pygame.event.get(): # Define eventos
        if event.type == QUIT:
            pygame.quit()
            exit()

    todas_as_sprites.draw(tela) # Insere as sprites
    todas_as_sprites.update()

    pygame.display.flip() # atualiza a tela
