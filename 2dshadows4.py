import pygame

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shadows')
mainclock = pygame.time.Clock()

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
        x_change = target[0] - self.start_point[0]
        y_change = target[1] - self.start_point[1]
        error_margin = 2
        if x_change == 0:
            x_change += 1
        if y_change == 0:
            y_change += 1
        if (y_change / (x_change/3)) > 20 or (y_change / (x_change/3)) < -20 :
            y_change /= 100
            x_change /= 100
        else:
            y_change /= (x_change/3)
            x_change = 3
            
        cur_x = self.start_point[0]
        cur_y = self.start_point[1]
        for x in range(int((self.start_point[0] - target[0])//x_change)):
            for y in range(int((self.start_point[1] - target[1])//y_change)):
                # pygame.draw.circle(screen, (0,0,255), (cur_x, cur_y), 4)
                if (cur_x < (target[0] + x_change) and (cur_x > target[0] - x_change)) and (cur_y < (target[1] + y_change) and (cur_y > target[1] - y_change)):
                    self.end_point = (cur_x, cur_y)
                    pygame.draw.circle(screen, (0,0,255), (cur_x, cur_y), 4)
                    return
                cur_x -= x_change
                cur_y -= y_change


screen.fill((255,255,255))
pygame.display.flip()

obstacles = [(100,100,100), (300, 400, 50), (700, 400, 10)]
testray = Ray(None, None, None)
rays = []


running = True
while running:
    raynum = 20
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    raynum /= 4
    for i in range(int(raynum)):
        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((i*(width//raynum),0))
        ray.draw()

        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((i*(width//raynum),height))
        ray.draw()

        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((0,i*(height//raynum)))
        ray.draw()


        ray = Ray(pygame.mouse.get_pos(), None, None)
        rays.append(ray)
        ray.cast((width,i*(height//raynum)))
        ray.draw()
    pygame.display.flip()
    mainclock.tick(60)