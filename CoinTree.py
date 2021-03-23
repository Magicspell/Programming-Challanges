import pygame
import random
import time
prev_flip = 0
prev_coords = [[0,100]]
prev_x = 0
prev_y = 0
line_increment = 5

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Coin Tree')


pygame.display.flip()

def getline(mode, prev_x, prev_y):
    # global prev_x
    # global prev_y
    global prev_flip
    if mode == 0:
        x = prev_x + line_increment
        y = prev_y
    if mode == 1:
        x = prev_x + line_increment
        y = prev_y + line_increment
    
    # prev_x = x
    # prev_y = y
    prev_flip = mode
    return x,y


running = True
while running:
    i = 0
    new_prev_coords = prev_coords.copy()
    for coords in new_prev_coords:
        coinflip = random.randint(0,1)
        if coinflip == prev_flip:
            new_coords = getline(0, coords[0], coords[1])
            if not new_coords in prev_coords:
                pygame.draw.line(screen, (255,255,255), (coords[0], coords[1]), new_coords)
                if coinflip == 0:
                    prev_coords.append(new_coords)
                else:
                    prev_coords[i] = new_coords
            new_coords = getline(1, coords[0], coords[1])
            if not new_coords in prev_coords:
                pygame.draw.line(screen, (255,255,255), (coords[0], coords[1]), new_coords)
                if coinflip == 1:
                    prev_coords.append(new_coords)
                else:
                    prev_coords[i] = new_coords
        else:
            new_coords = getline(coinflip, coords[0], coords[1])
            if not new_coords in prev_coords:
                pygame.draw.line(screen, (255,255,255), (coords[0], coords[1]), new_coords)
                prev_coords.append(new_coords)
        i += 1
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False