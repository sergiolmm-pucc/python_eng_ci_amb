
import pygame


pygame.init()
screen = pygame.display.set_mode((400,300))
done = False

cor_azul = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           done = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cor_azul = not cor_azul

    if cor_azul: color = (0,128,255)
    else: color = (255,0,0)
    pygame.draw.rect(screen, (0,128,255), pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen,color,(60,60),15) 
    pygame.display.flip()
    
