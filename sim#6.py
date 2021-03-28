import pygame

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sim #6')

points = []
minX = 0
maxX = width
minY = 0
maxY = height

def draw_recent_rect(amount):
    recent_points = points[-amount:]
    avgX = 0
    avgY = 0
    maxX = 1
    minX = 1
    maxY = 1
    minY = 1
    maxXcount = 0
    minXcount = 0
    maxYcount = 0
    minYcount = 0
    for point in recent_points:
        avgX += point[0]
        avgY += point[1]
    if len(recent_points) != 0:
        avgX /= len(recent_points)
    if len(recent_points) != 0:
        avgY /= len(recent_points)
    for point in recent_points:
        if point[0] >= avgX:
            maxX += point[0]
            maxXcount +=1
        else:
            minX += point[0]
            minXcount +=1
        if point[1] >= avgY:
            maxY += point[1]
            maxYcount +=1
        else:
            minY += point[1]
            minYcount +=1
    if maxXcount != 0:
        maxX /= maxXcount
    if minXcount != 0:
        minX /= minXcount
    if maxYcount != 0:
        maxY /= maxYcount
    if minYcount != 0:
        minY /= minYcount

    if minX > maxX:
        tempx = maxX
        maxX = minX
        minX = tempx
    if minY > maxY:
        tempy = maxY
        maxY = minY
        minY = tempy
    w = maxX-minX
    h = maxY-minY

    rect = pygame.Rect((minX-(w/2), minY-(h/2)), (w, h))
    pygame.draw.rect(screen, (0,0,255), rect)

def draw_rect():
    avgX = 0
    avgY = 0
    maxXcount = 0
    minXcount = 0
    maxYcount = 0
    minYcount = 0

    maxX = 1
    minX = 1
    maxY = 1
    minY = 1
    for point in points:
        avgX += point[0]
        avgY += point[1]
    if len(points) != 0:
        avgX /= len(points)
    if len(points) != 0:
        avgY /= len(points)
    for point in points:
        if point[0] >= avgX:
            maxX += point[0]
            maxXcount +=1
        else:
            minX += point[0]
            minXcount +=1
        if point[1] >= avgY:
            maxY += point[1]
            maxYcount +=1
        else:
            minY += point[1]
            minYcount +=1
    if maxXcount != 0:
        maxX /= maxXcount
    if minXcount != 0:
        minX /= minXcount
    if maxYcount != 0:
        maxY /= maxYcount
    if minYcount != 0:
        minY /= minYcount

    if minX > maxX:
        tempx = maxX
        maxX = minX
        minX = tempx
    if minY > maxY:
        tempy = maxY
        maxY = minY
        minY = tempy

    w = maxX-minX
    h = maxY-minY

    rect = pygame.Rect((minX-(w/2), minY-(h/2)), (w, h))
    pygame.draw.rect(screen, (255,0,0), rect)

draw_rect()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                points.append(pygame.mouse.get_pos())
                screen.fill((0,0,0))
                draw_rect()
                # draw_recent_rect(5)
                pygame.display.flip()