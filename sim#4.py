import pygame
import random

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))   
pygame.display.set_caption('Sim #4')
mainclock = pygame.time.Clock()

starting_points = []
endpoints = []
start_point_chance = 100
endpoint_chance = 100
line_vary = 25
speed = 1000

def get_color(prevcoords, x,y):
    prevx = prevcoords[0]
    prevy = prevcoords[1]
    color = (x/255,y%255,random.randint(0,254))
    # if prevx > x:
    #     color = (random.randint(0,200),random.randint(0,150),random.randint(0,30))
    # if x > prevx:
    #     color = (random.randint(0,30),random.randint(0,150),random.randint(0,200))
    # elif prevy > y:
    #     color = (random.randint(0,150),random.randint(0,30),random.randint(0,200))
    # elif y > prevy:
    #     color = (random.randint(0,150),random.randint(0,200),random.randint(0,30))
    # else:
    #     color = (random.randint(0,254),random.randint(0,254),random.randint(0,254))
    return color


for i in range(1):
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    starting_points.append((x,y))
    pygame.draw.circle(screen,(0,255,0),(x,y),5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                loc = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(0,255,0),loc,5)
                starting_points.append(loc)
    for point in starting_points:
        if random.randint(0,start_point_chance) == 1:
            endpoints.append(point)
    for point in endpoints:
        if random.randint(0,endpoint_chance) == 1:
            tempx = point[0]
            tempy = point[1]
            x = random.randint(-1*line_vary, line_vary) + tempx
            y = random.randint(-1*line_vary,line_vary) + tempy
            pygame.draw.line(screen,get_color(point,x,y),point,(x,y))
            endpoints.remove(point)
            endpoints.append((x,y))
    pygame.display.flip()
    mainclock.tick(speed)