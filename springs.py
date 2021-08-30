import pygame
import vector

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')
mainclock = pygame.time.Clock()




class Spring():
    def __init__(self, bob, anchor, radius):
        self.bob = vector.Vector(bob[0],bob[1])
        self.anchor = vector.Vector(anchor[0],anchor[1])
        self.radius = radius
        self.rest_length = 200
        self.spring_constant = 0.01
        self.v = vector.Vector(0,0)
        self.g = vector.Vector(0,0.1)
    def draw(self):
        screen.fill((0,0,0))
        pygame.draw.line(screen,(255,255,255),(self.bob.x,self.bob.y), (self.anchor.x,self.anchor.y))
        pygame.draw.circle(screen,(255,150,150),(self.bob.x,self.bob.y),self.radius)
        pygame.draw.circle(screen,(150,150,255),(self.anchor.x,self.anchor.y),self.radius)
    def update(self):
        force = vector.Vector(self.bob.x,self.bob.y)
        force.sub(self.anchor)
        x = force.mag() - self.rest_length
        force.normalize()
        force.mult(-1*self.spring_constant*x)

        self.v.add(force)
        self.v.add(self.g)

        self.bob.add(self.v)
        # self.v.mult(0.99)
    def set_loc(self, loc):
        self.bob.x = loc[0]
        self.bob.y = loc[1]
        self.v = vector.Vector(0,0)


s = Spring((350,250),(300,200),30)
s.draw()
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        s.set_loc(pos)
    s.update()
    s.draw()
    pygame.display.flip()
    mainclock.tick(50)