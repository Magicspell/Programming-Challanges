import pygame

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Grapher')
mainclock = pygame.time.Clock()

def calculate_y(x):
    y = 0.02*x**2
    return y

def graph():
    prev_point = (0,0)
    for x in range(width):
        y = calculate_y(x)
        if y > height or y < 0:
            break
        pygame.draw.line(screen, (255,255,255), prev_point, (x,height-y))
        prev_point = (x,height-y)
        # pygame.draw.circle(screen, (200, 200, 200), (x,y), 1)
    pygame.display.flip()

graph()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                graph()
        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width = event.w
            height = event.h