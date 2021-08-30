import pygame

(width, height) = (720, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shadows')
mainclock = pygame.time.Clock()

class Curve:
    def __init__(self, anchor_p, ctrl_p):
        self.anchor_p = anchor_p
        self.ctrl_p = ctrl_p


c = Curve([(60, 360), (650, 360)], [(250, 150), (450, 450)])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((0,0,0))
    for p in c.anchor_p:
        pygame.draw.circle(screen, (255,255,255), p, 5)
    for p in c.ctrl_p:
        pygame.draw.circle(screen, (255,255,255), p, 5)

    pygame.display.flip()
    mainclock.tick(60)