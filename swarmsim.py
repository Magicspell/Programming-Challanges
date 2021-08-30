import pygame

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Swarm')

class Swarm():
    def __init__(self, radius=3, color=(0,0,0), point_num=10, seperation=40):
        self.points = []
        self.loc = (width//2, height//2)
        self.color = color
        self.radius = radius
        self.main_point = self.loc
        self.point_num = point_num
        self.seperation = seperation
    def draw(self):
        i = 0
        for point in self.points:
            self.color = ((i*1)%255,(i*1)%255,(i*1)%255)
            pygame.draw.circle(screen, self.color, point, self.radius)
            i += 1
        pygame.draw.circle(screen, self.color, self.main_point, self.radius)
    def update(self):
        self.points = []
        for i in range(self.point_num):
            if i:
                pos_x = (self.seperation * i) + self.loc[0]
                neg_x = (self.seperation * i * -1) + self.loc[0]
                pos_y = (self.seperation * i) + self.loc[1]
                neg_y = (self.seperation * i * -1) + self.loc[1]
                self.points.append((pos_x, self.loc[1]))
                self.points.append((neg_x, self.loc[1]))
                self.points.append((self.loc[0], pos_y))
                self.points.append((self.loc[0], neg_y))
                for x in range(i):
                    self.points.append((pos_x - (self.seperation * x), pos_y))
                    self.points.append((pos_x, pos_y - (self.seperation * x)))
                    self.points.append((pos_x - (self.seperation * x), neg_y))
                    self.points.append((pos_x, neg_y + (self.seperation * x)))
                    self.points.append((neg_x + (self.seperation * x), neg_y))
                    self.points.append((neg_x, neg_y + (self.seperation * x)))
                    self.points.append((neg_x + (self.seperation * x), pos_y))
                    self.points.append((neg_x, pos_y - (self.seperation * x)))
        i = 0
        # for p in points:



swarm = Swarm()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    swarm.main_point = pygame.mouse.get_pos()
    swarm.update()
    swarm.draw()
    pygame.display.flip()