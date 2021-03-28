import pygame
import random

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sim #7: Particles')
mainclock = pygame.time.Clock()

particles = []

class Particle():
    def __init__(self, loc, radius, color):
        self.loc = loc
        self.radius = radius
        self.color = color
        self.vx = random.uniform(-1,1)
        self.vy = random.uniform(-5,-1)
        # self.alpha = 255

    def show(self):
        s = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        s.fill((0,0,0,0))
        pygame.draw.circle(s, self.color, (self.radius,self.radius), self.radius)
        screen.blit(s, self.loc)

    def update(self):
        x = self.loc[0]
        y = self.loc[1]
        alpha = self.color[3]
        self.vx *= 0.98
        self.vy *= 0.98
        x += self.vx
        y += self.vy
        self.loc = (x,y)
        alpha /= 1.05
        if alpha < 0.1:
            alpha = 0
        self.color = (self.color[0],self.color[1],self.color[2],alpha)

    def finished(self):
        return self.color[3] == 0

def setup(pnum):
    for i in range(pnum):
        p = Particle((300,480), 8, (0,255,255,255))
        particles.append(p)

def draw():
    setup(7)
    screen.fill((0,0,0))
    for p in particles:
        p.update()
        p.show()
        if p.finished():
            particles.remove(p)
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    mainclock.tick(50)