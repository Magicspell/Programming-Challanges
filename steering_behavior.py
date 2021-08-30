import pygame
import random
import vector
import numpy


(width, height) = (720, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('steering')
mainclock = pygame.time.Clock()
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 175)
text = font.render('Ralphie', True, (255,255,255))
screen.blit(text, (30, 100))

class Vehicle:
    def __init__(self, loc):
        self.loc = vector.VectorNew(random.randint(0,width), random.randint(0,height))
        self.target = vector.VectorNew(loc[0], loc[1])
        self.vel = vector.VectorNew(random.uniform(-1.0,1.0), random.uniform(-1.0,1.0))
        self.acc = vector.VectorNew(0, 0)
        self.max_speed = 5
        self.max_force = 0.3
    def update(self):
        self.loc = self.loc.add(self.vel)
        self.vel = self.vel.add(self.acc)
        self.acc = self.acc.mult(0)
    def draw(self):
        pygame.draw.circle(screen, (255,150,20), (self.loc.x, self.loc.y), 2)
    def apply_force(self, force):
        self.acc = self.acc.add(force)
    def seek(self, target):
        desired = target.sub(self.loc)
        desired.normalize()
        desired = desired.mult(self.max_speed)
        steer = desired.sub(self.vel)
        steer.limit(self.max_force)
        return steer
    def arrive(self, target):
        desired = target.sub(self.loc)
        distance = desired.mag()
        speed = self.max_speed
        if distance < 100:
            speed = numpy.interp(distance, [0, 100], [0, self.max_speed])
        else:
            speed 
        desired.normalize()
        desired = desired.mult(speed)
        steer = desired.sub(self.vel)
        steer.limit(self.max_force)
        return steer
    def apply_behavior(self):
        seek = self.arrive(self.target)
        self.apply_force(seek)




vehicles = []
for y in range(height):
    if not y%5:
        for x in range(width):
            if not x%5:
                if screen.get_at((x,y)) == (255,255,255):
                    vehicles.append(Vehicle((x,y)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((0,0,0))
    for v in vehicles:
        v.apply_behavior()
        v.update()
        v.draw()
    pygame.display.flip()
    mainclock.tick(60)