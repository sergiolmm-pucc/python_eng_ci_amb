import pygame

sc_width = 400
sc_height = 300


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


    screen.fill((255,255,255))

    surf = pygame.Surface((50,50))

    surf.fill((0,255,128))
    surf_center = ((sc_width-surf.get_width())/2, 
                   (sc_height-surf.get_height())/2)
    screen.blit(surf,surf_center)

    if cor_azul: color = (0,128,255)
    else: color = (255,0,0)
    pygame.draw.rect(screen, (0,128,255), pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen,color,(60,60),15) 
    pygame.display.flip()
    
