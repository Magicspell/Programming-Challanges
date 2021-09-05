import pygame

(width, height) = (720, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('placing paintings')
mainclock = pygame.time.Clock()
pygame.init()


class Placeable:
    def __init__(self, loc, img_path, width, height):
        self.x = loc[0]
        self.y = loc[1]
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (width, height))
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

paintings = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            x /= 80
            x = round(x)*80
            y /= 80
            y = round(y)*80
            x -= 38
            y -= 38
            paintings.append(Placeable((x,y), "./static/10.png", 75, 75))
    screen.fill((0,0,0))
    for p in paintings:
        p.draw()
    pygame.display.flip()
    mainclock.tick(60)