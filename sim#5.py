import pygame
import random
import math

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))   
pygame.display.set_caption('Sim #5')
mainclock = pygame.time.Clock()

circles = {}
circle_size = 20
selected_circles = []

#set up circles
for i in range(int(input("Number of starting circles: "))):
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    circle = pygame.draw.circle(screen,color,(x,y),circle_size)
    circles[i] = {}
    circles[i]['loc'] = (x,y)
    circles[i]['color'] = color


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for circle in circles:
                    circx,circy = circles[circle]['loc']
                    x, y = event.pos
                    sqx = (x - circx)**2
                    sqy = (y - circy)**2
                    if math.sqrt(sqx+sqy) < circle_size:
                        print(circle)
                        if circle in selected_circles:
                            selected_circles.remove(circle)
                        else:
                            selected_circles.append(circle)
                        if len(selected_circles) == 2:
                            color1 = circles[selected_circles[0]]['color']
                            color2 = circles[selected_circles[1]]['color']
                            r = (color1[0] + color2[0])/2
                            g = (color1[1] + color2[1])/2
                            b = (color1[2] + color2[2])/2
                            x = random.randint(0,width-1)
                            y = random.randint(0,height-1)
                            pygame.draw.circle(screen,(r,g,b),(x,y),circle_size)
                            newcircle = len(circles)
                            circles[newcircle] = {}
                            circles[newcircle]['loc'] = (x,y)
                            circles[newcircle]['color'] = (r,g,b)
                            pygame.display.flip()
                            selected_circles = []
                            break
                        print(selected_circles)