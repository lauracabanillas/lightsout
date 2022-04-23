import math
from random import random
import pygame
import time

IMAGE_SIZE = 100
DIRECTIONS = [
    #(1,1),
    (1,0),
    #(1,-1),
    #(-1,1),
    (-1,0),
    #(-1,-1),
    (0,1),
    (0,0),
    (0,-1),
]

lightOn = pygame.transform.scale(pygame.image.load("./images/light.jpg"), (IMAGE_SIZE,IMAGE_SIZE))
lightOff = pygame.transform.scale(pygame.image.load("./images/light_out.jpg"), (IMAGE_SIZE,IMAGE_SIZE))

class game:
    def __init__(self, screen, mode=0) -> None:
        self.screen = screen
        self.images = [lightOn, lightOff]
        self.mode = mode
        self.running = True
        self.grid = [[math.floor(random()*2) for x in range(5)] for y in range(5)]
        
    def handling_events(self):
        while self.running:
            self.display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        self.handle_click()
                        print("Left Mouse key was clicked")

    def handle_click(self):
        pos = pygame.mouse.get_pos()
        if pos[0] >= 5*IMAGE_SIZE or pos[1] >= 5*IMAGE_SIZE:
            return
        for direction in DIRECTIONS:
            if 0<=pos[0]//IMAGE_SIZE+direction[0] <5 and 0<= pos[1]//IMAGE_SIZE+direction[1] < 5:
                self.toggle(pos[0]//IMAGE_SIZE+direction[0], pos[1]//IMAGE_SIZE+direction[1])

        self.checkWin()


    def toggle(self, i, j):
        self.grid[i][j]=(self.grid[i][j]+1)%2
        #self.grid[math.floor(random()*5)][math.floor(random()*5)] = math.floor(random()*2)
        
    def checkWin(self):
        if not any(1 in x for x in self.grid):
            print("won !")
            self.running = False

    def display(self):
        if self.mode == 0:
            print("----------- grid ---------")
            print(self.grid)
        else:
            #print("in pygame window")
            for i in range(5):
                for j in range(5):
                    self.screen.blit(self.images[self.grid[i][j]], (i*IMAGE_SIZE,j*IMAGE_SIZE))
            pygame.display.update()

    def run(self):
        while self.running:
            self.handling_events()

pygame.init()
screen = pygame.display.set_mode((1080,720))
game = game(screen, 1)
game.run()
