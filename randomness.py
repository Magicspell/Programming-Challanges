import pygame
import random
import time

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('IDK')
pygame.display.flip()

running = True
i = 0
while running:
    i += 1
    shape = random.randint(1,2)
    color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    position = (random.randint(0,width), random.randint(0,height))
    size = random.randint(0,i%100)
    size2 = random.randint(0,i%150)
    if shape == 1:
        rect = pygame.Rect(position, (size, size2))
        pygame.draw.rect(screen, color, rect)
    else:
        pygame.draw.circle(screen, color, position, size)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(0.05)