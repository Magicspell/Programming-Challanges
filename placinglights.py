import pygame
import pygame_essentials as pe

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Placing lights')
mainclock = pygame.time.Clock()

obstacles = []
o = pe.Object('s', (100,100), (100,100,100), radius=100)
obstacles.append(o)
o = pe.Object('s', (300,400), (100,100,100), radius=50)
obstacles.append(o)
o = pe.Object('s', (700,400), (100,100,100), radius=30)
obstacles.append(o)
o = pe.Object('s', (800,120), (100,100,100), radius=100)
obstacles.append(o)

mainlight = pe.Light(screen, pygame.mouse.get_pos(), obstacles, brightness=80)
placed_lights = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
        l = pe.Light(screen, pygame.mouse.get_pos(), obstacles, raynum=50, brightness=80)
        l.cast()
        placed_lights.append(l)
    screen.fill((0,0,0))
    for l in placed_lights:
        l.draw()
    mainlight.loc = pygame.mouse.get_pos()
    mainlight.cast()
    mainlight.draw()

    for o in obstacles:
        o.draw(screen)
    pygame.display.flip()
    mainclock.tick(60)