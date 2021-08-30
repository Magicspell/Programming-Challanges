import pygame
import emitter

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Mouse Particles')
mainclock = pygame.time.Clock()

move_right = False
move_left = False
move_up = False
move_down = False

class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
    def draw(self):
        rect = pygame.Rect((self.x,self.y),(20,20))
        pygame.draw.rect(screen,(255,200,0),rect)


p = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up = True
                move_down = False
            if event.key == pygame.K_s:
                move_down = True
                move_up = False
            if event.key == pygame.K_a:
                move_left = True
                move_right = False
            if event.key == pygame.K_d:
                move_right = True
                move_left = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
    if move_up == True:
        p.y -= 5
    if move_down == True:
        p.y += 5
    if move_left == True:
        p.x -= 5
    if move_right == True:
        p.x += 5
    screen.fill((0,0,0))
    p.draw()
    pygame.display.flip()
    mainclock.tick(10)