import pygame
import random

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Circle sim')

mainclock = pygame.time.Clock()

size = 100
speed = 10000
bluechance = 2000

x = random.randint(0, width-1)
y = random.randint(0, height-1)
pygame.draw.circle(screen, (0,0,255), (x,y), size)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    color = tuple(screen.get_at((x,y))[:3])
    if color == (0,0,0):
        pygame.draw.circle(screen, (255,255,255), (x,y), size)
        pygame.display.flip()
        size += 1
    elif color == (255,255,255):
        pygame.draw.circle(screen, (0,0,0), (x,y), size)
        pygame.display.flip()
        size -= 2
        if size < 1:
            size = 1
    elif color == (0,0,255):
        if random.randint(0,2) == 1:
            pygame.draw.circle(screen, (0,0,255), (x,y), size+10)
            pygame.display.flip()
        else:
            pygame.draw.circle(screen, (0,0,0), (x,y), size)
            pygame.display.flip()
    if random.randint(0,bluechance) == 1:
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        pygame.draw.circle(screen, (0,0,255), (x,y), size)
        pygame.display.flip()
    mainclock.tick(speed)