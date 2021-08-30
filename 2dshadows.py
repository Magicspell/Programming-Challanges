import pygame
from math import gcd

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shadows')
mainclock = pygame.time.Clock()

screen.fill((255,255,255))
pygame.display.flip()

obsticals = [(100,100,100), (300, 400, 50), (700, 400, 10)]

shadows = []
points = []

class Shadow():
    def __init__(self):
        self.points = []
        self.has_corner = False
    def add_point(self, point):
        self.points.append(point)
    def draw(self):
        for point in self.points:
            if point in points:
                print(points.index(self.points[0]))
        # endpoint_max = 
        if len(self.points) > 2:
            pygame.draw.polygon(screen, (0,0,0), self.points)

def draw_obsticals():
    for obstical in obsticals:
        x = obstical[0]
        y = obstical[1]
        r = obstical[2]
        rect = pygame.Rect(x-r, y-r, r*2, r*2)
        pygame.draw.rect(screen, (200,200,200), rect)

def raycast(x, y):
    m_x = pygame.mouse.get_pos()[0]
    m_y = pygame.mouse.get_pos()[1]
    run = x - m_x
    rise = y - m_y
    run /= 300
    rise /= 300
    prev_x = m_x
    prev_y = m_y
    hit = False
    prev_hit = False
    global points
    for i in range(300):
        o = 0
        for obstical in obsticals:
            other_max_x = obstical[0] + obstical[2]
            other_min_x = obstical[0] - obstical[2]
            other_max_y = obstical[1] + obstical[2]
            other_min_y = obstical[1] - obstical[2]

            touching_x = prev_x > other_min_x and prev_x < other_max_x
            touching_y = prev_y > other_min_y and prev_y < other_max_y
            if touching_x and touching_y:
                hit = True
            elif not hit:
                pygame.draw.line(screen, (0,0,0), (prev_x, prev_y), (prev_x + run, prev_y + rise))
            if not prev_hit and hit:
                pygame.draw.circle(screen, (0,0,255), (prev_x, prev_y), 4)
                points.append((prev_x, prev_x))
                shadows[o].add_point((prev_x, prev_y))
                return
            prev_hit = hit
            o += 1
        error_margin = 10
        if prev_y < (y + error_margin) and prev_x < (x + error_margin) and not hit:
            pygame.draw.circle(screen, (0,0,255), (x, y), 4)
            points.append((prev_x, prev_y))
        prev_x += run
        prev_y += rise
        prev_x = round(prev_x, 3)
        prev_y = round(prev_y, 3)


line_space = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    draw_obsticals()
    w = 0
    h = 0
    shadows = []
    for obstical in obsticals:
        shadows.append(Shadow())
    points = []
    raycast(200,0)
    while w < width - line_space:
        w += line_space
        raycast(w,0)
        raycast(w,height)
    while h < height - line_space:
        h += line_space
        raycast(0,h)
        raycast(width,h)
    for shadow in shadows:
        shadow.draw()
    pygame.display.flip()
    mainclock.tick(60)