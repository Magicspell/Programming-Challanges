import pygame
import emitter

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Game')
mainclock = pygame.time.Clock()
pygame.init()

class Background():
    def __init__(self):
        self.pixels = [[]]
        for w in range(width):
            hlist = []
            for h in range(height):
                if h <= height/4:
                    hlist.append((190,255,0))
                else:
                    hlist.append((0,0,0))
            self.pixels.append(hlist)
    def draw(self):
        screen.fill((0, 162, 255))
        rect = pygame.Rect(0,height*3/4,width,height/4)
        pygame.draw.rect(screen,(61, 41, 12), rect)

class Burn():
    def __init__(self):
        self.burnt = []
    def burn(self, loc):
        if screen.get_at(loc) == (61, 41, 12):
            self.burnt.append(loc)
    def draw(self):
        for pixel in self.burnt:
            rect = pygame.Rect(pixel[0],pixel[1],10,10)
            pygame.draw.rect(screen,(10, 6, 0), rect)

class Player():
    def __init__(self):
        self.coins = 10
    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        img = font.render(f'Coins: {self.coins}', True, (255,255,255))
        screen.blit(img, (20, 20))

class Plants():
    def __init__(self):
        self.plants = {}
    def grow(self, loc, player):
        if loc not in self.plants.keys():
            player.coins -= 1
            self.plants[loc] = 0
        else:
            self.plants[loc] += 1
    def draw(self):
        for plant in self.plants.keys():
            rect = pygame.Rect(plant[0],plant[1] - (10*self.plants[plant]),10,10*self.plants[plant])
            pygame.draw.rect(screen,(19, (100+self.plants[plant]%255) + 1, 0), rect)
    def burn(self, loc):
        if loc in self.plants.keys():
            del self.plants[loc]
        for i in range(10):
            if (loc[0]+i, loc[1]) in self.plants.keys():
                del self.plants[(loc[0]+i, loc[1])]
            elif (loc[0], loc[1]+i) in self.plants.keys():
                del self.plants[(loc[0], loc[1]+i)]
    def harvest(self, player):
        for plant in self.plants:
            player.coins += self.plants[plant]
        self.plants = {}
 


fire = emitter.Emitter(screen,(0,0),10,'square',(255,150,0))
water = emitter.Emitter(screen,(0,0),10,'square',(41, 177, 255))
back = Background()
b = Burn()
p = Plants()
pygame.display.flip()
player = Player()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                p.harvest(player)
    back.draw()
    b.draw()
    p.draw()
    player.draw()
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        b.burn(pos)
        p.burn(pos)
        fire.loc = pos
        fire.draw()
    elif pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()
        water.loc = pos
        water.draw()
        for i in range(10):
            if (pos[0]+i, pos[1]) in b.burnt:
                if player.coins > 0:
                    p.grow(pos, player)
            elif (pos[0], pos[1]+i) in b.burnt:
                if player.coins > 0:
                    p.grow(pos, player)
    else:
        fire.no_add_draw()
        water.no_add_draw()
    pygame.display.flip()
    mainclock.tick(100)