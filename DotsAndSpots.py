import pygame
import random

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
# icon = pygame.image.load('icon.png')
# pygame.display.set_icon(icon)
pygame.display.set_caption('Pete sim')
mainclock = pygame.time.Clock()

speed = 9000
branch_size = 3
start_branch_offset = 50
cont_branch_offset = 20
mountain_chance = 50000
selected_color = (0,0,255)

def get_red_branch():
    possible_starts = []
    branches = []
    for x in range(width):
        for y in range(height):
            color = tuple(screen.get_at((x,y))[:3])
            if color == (255,100,0):
                possible_starts.append((x,y))
            if color == (255,0,0):
                branches.append((x,y))
    if possible_starts:
        start_branch = random.choice(possible_starts)
        pygame.draw.circle(screen, (255,0,0), start_branch, branch_size)
    if branches:
        cont_branch = random.choice(branches)
        pygame.draw.circle(screen, (255,0,0), cont_branch, branch_size)
def gen_starting_point(color):
    if color == 'blue':
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)
        pygame.draw.circle(screen, (0,100,255), (x,y), 50)
    if color == 'red':
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)
        pygame.draw.circle(screen, (255,100,0), (x,y), 50)
def near_colors(x,y):
    colors = []
    for xdiff in range(3):
        for ydiff in range(3):
            tempx = x + xdiff
            tempy = y + ydiff
            if tempx >= width:
                tempx = width-1
            if tempy >= height:
                tempy = height-1
            colors.append(tuple(screen.get_at((tempx,tempy))[:3]))
    return colors



#GENERATE MOUNTAINS
def gen_mountain(num):
    for i in range(num):
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)
        rect = pygame.Rect((x,y), (30,50))
        pygame.draw.rect(screen, (128,128,128), rect)




gen_starting_point('blue')
gen_starting_point('red')
gen_mountain(5)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                loc = pygame.mouse.get_pos()
                rect = pygame.Rect(loc, (30,50))
                pygame.draw.rect(screen, (128,128,128), rect)
            if event.button == 4:
                selected_color = (255,0,0)
            if event.button == 5:
                selected_color = (0,0,255)

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,selected_color,pos,branch_size)

    # get_red_branch()
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    color = tuple(screen.get_at((x,y))[:3])
    if color == (128,128,128):
        if (0,0,255) in near_colors(x,y):
            pygame.draw.circle(screen, (0,100,255), (x,y), 50)
        if (255,0,0) in near_colors(x,y):
            pygame.draw.circle(screen, (255,100,0), (x,y), 50)
    if color == (0,100,255):
        for i in range(10):
            tempx = x + random.randint(-1*start_branch_offset,start_branch_offset)
            tempy = y + random.randint(-1*start_branch_offset,start_branch_offset)
            pygame.draw.circle(screen, (0,0,255), (tempx,tempy), branch_size)
    if color == (0,0,255):
        tempx = x + random.randint(-1*cont_branch_offset,cont_branch_offset)
        tempy = y + random.randint(-1*cont_branch_offset,cont_branch_offset)
        pygame.draw.circle(screen, (0,0,255), (tempx,tempy), branch_size)
    if color == (255,100,0):
        for i in range(10):
            tempx = x + random.randint(-1*start_branch_offset,start_branch_offset)
            tempy = y + random.randint(-1*start_branch_offset,start_branch_offset)
            pygame.draw.circle(screen, (255,0,0), (tempx,tempy), branch_size)
    if color == (255,0,0):
        tempx = x + random.randint(-1*cont_branch_offset,cont_branch_offset)
        tempy = y + random.randint(-1*cont_branch_offset,cont_branch_offset)
        pygame.draw.circle(screen, (255,0,0), (tempx,tempy), branch_size)
    if random.randint(0,mountain_chance) == 1:
        gen_mountain(1)



    pygame.display.flip()
    mainclock.tick(speed)