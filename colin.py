import math
from random import random
import pygame

IMAGE_SIZE = 200
lightOn = pygame.transform.scale(pygame.image.load("./images/light.jpg"), (IMAGE_SIZE,IMAGE_SIZE))
lightOff = pygame.transform.scale(pygame.image.load("./images/light_out.jpg"), (IMAGE_SIZE,IMAGE_SIZE))

class game:
    def __init__(self, screen, mode=0) -> None:
        self.screen = screen
        self.images = [lightOn, lightOff]
        self.mode = mode
        self.running = True
        self.grid = [[0 for x in range(5)] for y in range(5)]
        
    def handling_events(self):
        while self.running:
            self.update()
            self.display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        self.grid[math.floor(random()*5)][math.floor(random()*5)] = math.floor(random()*2)
        

    def display(self):
        if self.mode == 0:
            print("----------- grid ---------")
            print(self.grid)
        else:
            #print("in pygame window")
            for i in range(5):
                for j in range(5):
                    self.screen.blit(self.images[self.grid[i][j]], (i*IMAGE_SIZE,IMAGE_SIZE, j*IMAGE_SIZE,IMAGE_SIZE))
            pygame.display.update()

    def run(self):
        while self.running:
            self.handling_events()

pygame.init()
screen = pygame.display.set_mode((1080,720))
game = game(screen, 1)
game.run()
