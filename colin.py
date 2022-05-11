import math
from random import random
import pygame
import time
import solveur_matrice
import numpy as np

#hello
#je ne sais pas

IMAGE_SIZE = 100
DIRECTIONS = [
    (1,0),  
    (-1,0),
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
        self.pika = pygame.transform.scale(pygame.image.load("./images/pikatchu.jpg"), (200,400))
        self.bulle1 = pygame.transform.scale(pygame.image.load("./images/image_bulle1.png"), (330,250))

    def handling_events(self):
        matrice_printed=0
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
            if not solveur_matrice.soluble(np.matrix(self.grid)) and matrice_printed ==0: 
                print("la configuration n'etait pas soluble, veuillez recommencer")
                self.running = False
            else:
                if solveur_matrice.soluble(np.matrix(self.grid)) and matrice_printed==0:
                    print(solveur_matrice.solution(np.matrix(self.grid)))
                    matrice_printed=1
            
            
            

    def handle_click(self):
        pos = pygame.mouse.get_pos()
        if pos[0] >= 5*IMAGE_SIZE or pos[1] >= 5*IMAGE_SIZE:   #pos[0]= la position en x, et pos[1] la position en y
            return                                       #pourquoi y a un return avec rien
        for direction in DIRECTIONS:
            if 0<=pos[0]//IMAGE_SIZE+direction[0] <5 and 0<= pos[1]//IMAGE_SIZE+direction[1] < 5:   #pourquoi c'est compris entre 0 et 5 ?
                self.toggle(pos[0]//IMAGE_SIZE+direction[0], pos[1]//IMAGE_SIZE+direction[1])    #comment ce truc change le truc qu'on clique et les 4 autoue ?

        self.checkWin()


    def toggle(self, i, j):
        self.grid[i][j]=(self.grid[i][j]+1)%2  #si c'est 0, il affiche 1, et sinon il affiche 0
        #self.grid[math.floor(random()*5)][math.floor(random()*5)] = math.floor(random()*2)
        
    def checkWin(self):          #si la matrice ne contient que des 0, on affiche "won" et le jeu s'arrête
        if not any(0 in x for x in self.grid):
            print("won !")
            self.running = False
#        if not solveur_matrice.soluble(np.matrix(self.grid)):
 #           print("la configuration n'etait pas soluble, veuillez recommencer")
  #          self.running = False
   #     else:
    #        print(solveur_matrice.solution(np.matrix(self.grid)))


    def display(self):     #affiche la matrice
        if self.mode == 0:                 #quand on est en mode 0, il affiche juste la matrice dans le terminal
            print("----------- grid ---------")
            print(self.grid)
        else:
            #print("in pygame window")
            for i in range(5):
                for j in range(5):
                    self.screen.blit(self.images[self.grid[i][j]], (i*IMAGE_SIZE,j*IMAGE_SIZE))
            screen.blit(self.pika,(800,300))
            screen.blit(self.bulle1, (600,100))
            pygame.display.update()

    def run(self):
        while self.running:   #tant qu'on n'a pas arrêté le code, il rafraîchit les évènements
            self.handling_events()

pygame.init()
screen = pygame.display.set_mode((1080,720))
game = game(screen, 1)
game.run()

