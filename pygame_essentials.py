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