import pygame
import pygame_essentials

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shadows')
pygame.init()
font = pygame.font.SysFont('bigcaslonttf', 48)
mainclock = pygame.time.Clock()

obstacles = []
o = pygame_essentials.Object('s', (100,100), (100,100,100), radius=100)
obstacles.append(o)
o = pygame_essentials.Object('s', (300,400), (100,100,100), radius=50)
obstacles.append(o)
o = pygame_essentials.Object('s', (700,400), (100,100,100), radius=30)
obstacles.append(o)
o = pygame_essentials.Object('s', (800,120), (100,100,100), radius=100)
obstacles.append(o)

light = pygame_essentials.Light()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False