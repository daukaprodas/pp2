import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("War")

icon=pygame.image.load("images/dino.png")

pygame.display.set_icon(icon)
screen.fill((255, 255, 255))

square=pygame.Surface((50,170))
square.fill('Yellow')

running=True
while running:
    screen.blit(square,(0,0)) 
   
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            
pygame.quit()