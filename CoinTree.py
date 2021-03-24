import pygame
import random
import time
prev_flip = 0
prev_coords = [(0,100)]
prev_x = 0
prev_y = 0
line_increment = 10

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
    prev_coords = 
    for coords in new_prev_coords:
        coinflip = random.randint(0,1)
        if coinflip == prev_flip:
            coords_taken = False
            new_coords = getline(0, coords[0], coords[1])
            if not new_coords in prev_coords:
                r = random.randint(1,255)
                g = random.randint(1,255)
                b = random.randint(1,255)
                pygame.draw.line(screen, (r,g,b), (coords[0], coords[1]), new_coords)
                if coinflip == 0:
                    prev_coords.append(new_coords)
                else:
                    prev_coords[i] = new_coords
            else:
                coords_taken = True
            new_coords = getline(1, coords[0], coords[1])
            if not new_coords in prev_coords:
                pygame.draw.line(screen, (r,g,b), (coords[0], coords[1]), new_coords)
                if coinflip == 1:
                    prev_coords.append(new_coords)
                else:
                    prev_coords[i] = new_coords
            elif coords_taken and coords in prev_coords:
                prev_coords.remove(coords)
                i -= 1
        else:
            new_coords = getline(coinflip, coords[0], coords[1])
            if not new_coords in prev_coords:
                r = random.randint(1,255)
                g = random.randint(1,255)
                b = random.randint(1,255)
                pygame.draw.line(screen, (r,g,b), (coords[0], coords[1]), new_coords)
                prev_coords.append(new_coords)
        i += 1
    pygame.display.flip()
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False