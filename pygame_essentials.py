import pygame

class Object():
    def __init__(self, type, loc, color, radius = None, height = None, width = None):
        if type == 'square' or type == 's':
            self.type = 's'
            self.radius = radius
        if type == 'circle' or type == 'c':
            self.type = 'c'
            self.radius = radius
        if type == 'rectangle' or type =='r':
            self.type = 'r'
            self.width = width
            self.height = height
        self.x = loc[0]
        self.y = loc[1]
        self.color = color
        self.forces = []
    def draw(self, screen):
        if self.type == 's':
            rect = pygame.Rect(self.x - (self.radius), self.y-(self.radius), self.radius*2, self.radius*2)
            pygame.draw.rect(screen, self.color, rect)
        if self.type == 'c':
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.type == 'r':
            rect = pygame.Rect((self.x - self.width/2), (self.y - self.height/2), self.width, self.height)
            pygame.draw.rect(screen, self.color, rect)
    def is_touching(self, other):
        if self.type == 's' or self.type == 'c':
            self_max_x = self.x + self.radius
            self_min_x = self.x - self.radius
            self_max_y = self.y + self.radius
            self_min_y = self.y - self.radius
        else:
            self_max_x = self.x + self.width/2
            self_min_x = self.x - self.width/2
            self_max_y = self.y + self.height/2
            self_min_y = self.y - self.height/2
        if other.type == 's' or other.type == 'c':
            other_max_x = other.x + other.radius
            other_min_x = other.x - other.radius
            other_max_y = other.y + other.radius
            other_min_y = other.y - other.radius
        else:
            other_max_x = other.x + other.width/2
            other_min_x = other.x - other.width/2
            other_max_y = other.y + other.height/2
            other_min_y = other.y - other.height/2
            
        right_side = self_max_x > other_min_x and self_min_x < other_max_x
        left_side = self_min_x > other_min_x and self_max_x < other_max_x
        top_side = self_max_y > other_min_y and self_min_y < other_max_y
        bottom_side = self_min_y > other_min_y and self_max_y < other_max_y
        return (right_side or left_side) and (top_side or bottom_side)
    def move(self, x=0, y=0, loc=None):
        self.x += x
        self.y += y
    def applyforces(self):
        for force in self.forces:
            self.move(force[0], force[1])

class Ray():
    def __init__(self, start_point, end_point, colliding_obstacle, obstacles):
        self.start_point = start_point
        self.end_point = end_point
        self.colliding_obstacle = colliding_obstacle
        self.obstacles = obstacles
    def draw(self):
        pygame.draw.line(screen, (0,0,0), self.start_point, self.end_point)
    def cast(self, start, target):
        self.start_point = start
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
            if (cur_x < (target[0] + abs(x_change)) and (cur_x > target[0] - abs(x_change))) and (cur_y < (target[1] + abs(y_change)) and (cur_y > target[1] - abs(y_change))):
                self.end_point = (cur_x, cur_y)
                return
            point = Object('s', (cur_x, cur_y), (200,200,200), radius=1)
            for o in self.obstacles:
                if point.is_touching(o):
                    self.end_point = (cur_x, cur_y)
                    return
            cur_x += x_change
            cur_y += y_change

class Light():
    def __init__(self, surface, loc, obstacles, raynum=100, brightness=255, color=(255,255,255)):
        self.surface = surface
        self.loc = loc
        self.obstacles = obstacles
        self.rays = []
        self.raynum = raynum/4
        self.width = surface.get_width()
        self.height = surface.get_height()
        self.brightness = brightness
        self.color = color
    def draw(self):
        points = []
        i = 0
        for ray in self.rays:
            points.append(ray.end_point)
            i += 1
        if len(points) > 2:
            s = pygame.Surface((self.width, self.height))
            s.set_alpha(self.brightness)
            pygame.draw.polygon(s, self.color, points)
            self.surface.blit(s, (0,0))

    def cast(self):
        self.rays = []
        for i in range(int(self.raynum)):
            ray = Ray(self.loc, None, None, self.obstacles)
            self.rays.append(ray)
            ray.cast(self.loc, (i*(self.width//self.raynum),0))

        for i in range(int(self.raynum)):
            ray = Ray(self.loc, None, None, self.obstacles)
            self.rays.append(ray)
            ray.cast(self.loc, (self.width,i*(self.height//self.raynum)))

        h = int(self.raynum)
        for i in range(int(self.raynum)):
            ray = Ray(self.loc, None, None, self.obstacles)
            self.rays.append(ray)
            ray.cast(self.loc, (h*(self.width//self.raynum),self.height))
            h -= 1

        h = int(self.raynum)
        for i in range(int(self.raynum)):
            ray = Ray(self.loc, None, None, self.obstacles)
            self.rays.append(ray)
            ray.cast(self.loc, (0,h*(self.height//self.raynum)))
            h -= 1