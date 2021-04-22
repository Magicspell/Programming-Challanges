import pygame
import pygame_essentials

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shadows')
pygame.init()
font = pygame.font.SysFont('bigcaslonttf', 48)
mainclock = pygame.time.Clock()


highest_error = (0,0)

class Ray():
    def __init__(self, start_point, end_point, colliding_obstacle):
        self.start_point = start_point
        self.end_point = end_point
        self.colliding_obstacle = colliding_obstacle
    def draw(self):
        pygame.draw.line(screen, (0,0,0), self.start_point, self.end_point)
    def cast(self, target):
        self.start_point = pygame.mouse.get_pos()
        self.end_point = target
        res = 2
        x_change = target[0] - self.start_point[0]
        y_change = target[1] - self.start_point[1]
        error_margin = (7,3)
        if x_change == 0:
            x_change += 1
        if y_change == 0:
            y_change += 1
        if (y_change / (x_change/3)) > 20 or (y_change / (x_change/3)) < -20 :
            y_change /= 100
            x_change /= 100
        else:
            y_change /= (x_change/res)
            if x_change > 0:
                x_change = res
            else:
                x_change = -1*res
                y_change *= -1
        cur_x = self.start_point[0]
        cur_y = self.start_point[1]
        iteration_number = abs(int((self.start_point[0] - target[0])//x_change))
        for i in range(iteration_number):
            # pygame.draw.circle(screen, (0,0,255), (cur_x, cur_y), 4)
            if (cur_x < (target[0] + abs(x_change)) and (cur_x > target[0] - abs(x_change))) and (cur_y < (target[1] + abs(y_change)) and (cur_y > target[1] - abs(y_change))):
                self.end_point = (cur_x, cur_y)
                if debug:
                    pygame.draw.circle(screen, (255,0,0), (cur_x, cur_y), 4)
                return
            point = pygame_essentials.Object('s', (cur_x, cur_y), (200,200,200), radius=1)
            for o in obstacles:
                if point.is_touching(o):
                    if debug:
                        pygame.draw.circle(screen, (255,0,0), (cur_x, cur_y), 4)
                    self.end_point = (cur_x, cur_y)
                    return
            cur_x += x_change
            cur_y += y_change
        # print(f'Target: {target} | Actual: {(cur_x, cur_y)} | Error-Margin: {abs(x_change), abs(y_change)}')



screen.fill((20,20,20))
pygame.display.flip()

obstacles = []
testray = Ray(None, None, None)
rays = []
o = pygame_essentials.Object('s', (100,100), (100,100,100), radius=100)
obstacles.append(o)
o = pygame_essentials.Object('s', (300,400), (100,100,100), radius=50)
obstacles.append(o)
o = pygame_essentials.Object('s', (700,400), (100,100,100), radius=30)
obstacles.append(o)
o = pygame_essentials.Object('s', (800,120), (100,100,100), radius=100)
obstacles.append(o)

def draw_obstacles():
    for obstacle in obstacles:
        obstacle.draw(screen)

def draw_light():
    points = []
    i = 0
    for ray in rays:
        points.append(ray.end_point)
        if debug:
            font1 = pygame.font.SysFont('chalkduster.ttf', 20)
            img = font1.render(str(i), True, (0,0,0))
            screen.blit(img, ray.end_point)
        i += 1
    if len(points) > 2:
        pygame.draw.polygon(screen, (200,200,200), points)

debug = False
running = True
while running:
    raynum = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((20,20,20))
    raynum /= 4
    # ray = Ray(pygame.mouse.get_pos(), None, None)
    # rays.append(ray)
    # ray.cast((100,0))
    # ray.draw()
    draw_light()
    draw_obstacles()
    rays = []
    for i in range(int(raynum)):
        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((i*(width//raynum),0))
        if debug:
            ray.draw()

    for i in range(int(raynum)):
        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((width,i*(height//raynum)))
        if debug:
            ray.draw()

    h = int(raynum)
    for i in range(int(raynum)):
        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((h*(width//raynum),height))
        if debug:
            ray.draw()
        h -= 1

    h = int(raynum)
    for i in range(int(raynum)):
        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((0,h*(height//raynum)))
        if debug:
            ray.draw()
        h -= 1

    pygame.display.flip()
    mainclock.tick(60)