import math

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y
    def mult(self, num):
        self.x *= num
        self.y *= num
    def mag(self):
        return math.sqrt((self.x**2)+(self.y**2))
    def normalize(self):
        if self.mag():
            tempx = self.x / self.mag()
            tempy = self.y / self.mag()
            self.x = tempx
            self.y = tempy

class VectorNew():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self, vector):
        v = VectorNew(self.x + vector.x, self.y + vector.y)
        return v
    def sub(self, vector):
        v = VectorNew(self.x - vector.x, self.y - vector.y)
        return v
    def mult(self, num):
        v = VectorNew(self.x * num, self.y * num)
        return v
    def mag(self):
        return math.sqrt((self.x**2)+(self.y**2))
    def normalize(self):
        if self.mag():
            tempx = self.x / self.mag()
            tempy = self.y / self.mag()
            self.x = tempx
            self.y = tempy
    def limit(self, max):
        if self.x > max:
            self.x = max
        if self.x < -1 * max:
            self.x = -1 * max
        if self.y > max:
            self.y= max
        if self.y < -1 * max:
            self.y = -1 * max

