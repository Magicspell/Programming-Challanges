import pygame
import emitter

(width, height) = (1280, 720)
# screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Mouse Particles')
mainclock = pygame.time.Clock()

e = emitter.Emitter(screen, (0,0), 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pos = pygame.mouse.get_pos()
    e.loc = pos
    e.draw()
    pygame.display.flip()
    mainclock.tick(50)