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
    def __init__(self, loc, color=(255,150,20)):
        self.loc = vector.VectorNew(random.randint(0,width), random.randint(0,height))
        self.target = vector.VectorNew(loc[0], loc[1])
        self.vel = vector.VectorNew(random.uniform(-1.0,1.0), random.uniform(-1.0,1.0))
        self.acc = vector.VectorNew(0, 0)
        self.max_speed = 5
        self.max_force = 0.3
        self.color = color
    def update(self):
        self.loc = self.loc.add(self.vel)
        self.vel = self.vel.add(self.acc)
        self.acc = self.acc.mult(0)
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.loc.x, self.loc.y), 2)
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
        if distance < 500:
            speed = numpy.interp(distance, [0, 100], [0, self.max_speed])
        else:
            speed 
        desired.normalize()
        desired = desired.mult(speed)
        steer = desired.sub(self.vel)
        steer.limit(self.max_force)
        return steer
    def apply_behavior(self):
        mouse_pos = vector.VectorNew(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if abs(mouse_pos.sub(self.loc).mag() > 100):
            seek = self.arrive(self.target)
        else:
            seek = self.seek(self.target)
        self.apply_force(seek)




vehicles = []
r = 255
r_increasing = False
g = 0
b = 255
b_increasing = False
for y in range(height):
    if r >= 255:
        r_increasing = False
    if r <= 100:
        r_increasing = True
    if not r_increasing:
        r -= 1
    else:
        r += 1
    if not y%5:
        for x in range(width):
            if b >= 255:
                b_increasing = False
            if b <= 100:
                b_increasing = True
            if not b_increasing:
                b -= 1
            else:
                b += 1
            if not x%5:
                if screen.get_at((x,y)) == (255,255,255):
                    vehicles.append(Vehicle((x,y), (r,g,b)))


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