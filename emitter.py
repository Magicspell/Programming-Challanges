import pygame
import random

class Particle():
    def __init__(self, loc, radius, color, surface):
        self.loc = loc
        self.radius = radius
        self.color = color
        self.vx = random.uniform(-2,2)
        self.vy = random.uniform(-1,5)
        self.surface = surface

    def show(self):
        s = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        s.fill((0,0,0,0))
        pygame.draw.circle(s, self.color, (self.radius,self.radius), self.radius)
        self.surface.blit(s, self.loc)

    def update(self):
        x = self.loc[0]
        y = self.loc[1]
        alpha = self.color[3]
        self.vx *= 0.98
        self.vy *= 0.98
        x += self.vx
        y += self.vy
        self.loc = (x,y)
        alpha /= 1.03
        if alpha < 0.1:
            alpha = 0
        self.color = (self.color[0],self.color[1],self.color[2],alpha)

    def finished(self):
        return self.color[3] == 0

class SquareParticle():
    def __init__(self, loc, size, color, surface):
        self.loc = loc
        self.size = size
        self.color = color
        self.vx = random.uniform(-0.5,0.5)
        self.vy = random.uniform(-3,0.5)
        self.surface = surface

    def show(self):
        s = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        s.fill(self.color)
        self.surface.blit(s, self.loc)

    def update(self):
        x = self.loc[0]
        y = self.loc[1]
        alpha = self.color[3]
        self.vx *= 0.98
        self.vy *= 0.98
        x += self.vx
        y += self.vy
        self.loc = (x,y)
        alpha /= 1.04
        if alpha < 0.1:
            alpha = 0
        self.color = (self.color[0],self.color[1],self.color[2],alpha)

    def finished(self):
        return self.color[3] == 0

class Emitter():
    def __init__(self, surface, loc, pnum, shape, color):
        self.particles = []
        self.loc = loc
        self.surface = surface
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.shape = shape

        for i in range(pnum):
            if shape == 'circle':
                p = Particle(self.loc, 8, (self.r,self.g,self.b,255), surface)
            if shape =='square':
                p = SquareParticle(self.loc, 8, (self.r,self.g,self.b,255), surface)
            self.particles.append(p)

    def add_p(self, pnum):
        for i in range(pnum):
            if self.shape == 'circle':
                p = Particle(self.loc, 8, (self.r,self.g,self.b,255), self.surface)
            if self.shape =='square':
                p = SquareParticle(self.loc, 8, (self.r,self.g,self.b,255), self.surface)
            self.particles.append(p)

    def draw(self):
        self.add_p(7)
        # self.surface.fill((0,0,0))

        # self.r = random.randint(150,240)
        # self.g = random.randint(150,240)
        # # self.b = random.randint(0,254)

        for p in self.particles:
            p.update()
            p.show()
            if p.finished():
                self.particles.remove(p)

    def no_add_draw(self):
        # self.surface.fill((0,0,0))
        for p in self.particles:
            p.update()
            p.show()
            if p.finished():
                self.particles.remove(p)
