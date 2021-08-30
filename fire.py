import pygame
import emitter
import win32api
import win32con
import win32gui

(width, height) = (720, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Circle sim')
mainclock = pygame.time.Clock()



fire = emitter.Emitter(screen, (width/2,height/2), 10, "square", (255,0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    fire.draw()
    pygame.display.flip()
    mainclock.tick(60)