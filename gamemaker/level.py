import pygame

class level:
    def __init__(self, screen, player):
        self.obstacles = []
        self.player = player
    def draw(self):
        self.player.draw(self.screen)
        for o in self.obstacles:
            o.draw(self.screen)
        
