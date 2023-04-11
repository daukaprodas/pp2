import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")

mickey_image = pygame.image.load("mickeyclock.jpeg").convert_alpha()
mickey_rect = mickey_image.get_rect(center=(400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    now = datetime.datetime.now()
    minute_angle = now.minute * 6
    second_angle = now.second * 6

    minute_hand = pygame.transform.rotate(mickey_image, -minute_angle)
    minute_rect = minute_hand.get_rect(center=mickey_rect.center)
    screen.blit(minute_hand, minute_rect)

    second_hand = pygame.transform.rotate(mickey_image, -second_angle)
    second_rect = second_hand.get_rect(center=mickey_rect.center)
    screen.blit(second_hand, second_rect)

    pygame.display.update()
    clock.tick(60)