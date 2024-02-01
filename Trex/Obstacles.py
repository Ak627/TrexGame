import pygame
import random


class obstacles:
    def __init__(self):
        self.height = random.randrange(10, 50)
        self.xpos = random.randrange(900, 2500)
        self.ypos = 300 - self.height
        self.vy = 0
        self.width = 25
        
        self.atSide = False
    def move(self):
        if self.atSide == False:
            self.vx = -5
        else:
            self.vx = 0
            self.xpos = random.randrange(900, 2500)
            self.height = random.randrange(10, 50)
            self.ypos = 300 - self.height
        self.xpos += self.vx

        if self.xpos <= 0:
            self.atSide = True
        else:
            self.atSide = False
            
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.xpos, self.ypos, self.width, self.height))
