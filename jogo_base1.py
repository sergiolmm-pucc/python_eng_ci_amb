''''
Na pucc no terminal digitar 
py -3 -m pip install pygame   para instalar o pygame


'''

import pygame

sc_width = 400
sc_height = 300




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,75,100))
        self.rect = self.surf.get_rect()

    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_key[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_key[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        # ajusta posicao na tela do jogadore
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= sc_height:
            self.rect.bottom = sc_height
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= sc_width:
            self.rect.right = sc_width

# criu um jogador (instancia da classe Player)

player = Player()

player_center = ((sc_width - player.rect.width)/2 , 
                 (sc_height - player.rect.height)/2 )
player.rect.move_ip(player_center)

pygame.init()
screen = pygame.display.set_mode((sc_width , sc_height))
done = False
cor_azul = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           done = True 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_SPACE:
                cor_azul = not cor_azul 
    tecla = pygame.key.get_pressed()
    player.update(tecla)
    
    

    screen.fill((255,255,255))

    screen.blit(player.surf, player.rect)
    '''
    surf = pygame.Surface((50,50))

    surf.fill((0,255,128))
    surf_center = ((sc_width-surf.get_width())/2, 
                   (sc_height-surf.get_height())/2)
    screen.blit(surf,surf_center)

    if cor_azul: color = (0,128,255)
    else: color = (255,0,0)
    pygame.draw.rect(screen, (0,128,255), pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen,color,(60,60),15) 
    '''
    pygame.display.flip()
    
