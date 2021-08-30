import pygame
import random

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))   
pygame.display.set_caption('Starfield')
mainclock = pygame.time.Clock()

class Star:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.z = 0
    def update(self):
        self.z += 0.1
    def draw(self):
        sx = (self.x / self.z)
        sy = (self.y / self.z)
        print(self.z)
        pygame.draw.circle(screen, (255,255,255), (sx,sy), 4)
        # pygame.draw.circle(screen, (255,255,255), (self.x,self.y), 4)

stars = []
for i in range(100):
    s = Star()
    stars.append(s)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    for star in stars:
        star.update()
        star.draw()
    pygame.display.flip()