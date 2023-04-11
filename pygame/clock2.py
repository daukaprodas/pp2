import pygame
import os

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")

songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song = 0

pygame.mixer.init()
pygame.mixer.music.load(songs[current_song])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))

    pygame.display.update()
    clock.tick(60)