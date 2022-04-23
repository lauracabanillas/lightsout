import pygame
import numpy as np
from lights import Lights
from pika import Pika
# from text import Message
from lights_out import Lights_out
from bulle import Bulle1
from bulle import Bulle2

 
class game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.grille = np.matrix("1 0 0 0 0;0 0 0 0 0;0 0 1 0 0;0 0 0 0 0;0 0 0 0 0")
        self.light00 = Lights(0,0)
        self.light10 = Lights(0,100)
        self.light20 = Lights(0,200)
        self.light30 = Lights(0,300)
        self.light40 = Lights(0,400)
        self.light01 = Lights(100,0)
        self.light11 = Lights(100,100)
        self.light21 = Lights(100,200)
        self.light31 = Lights(100,300)
        self.light41 = Lights(100,400)
        self.light02 = Lights(200,0)
        self.light12 = Lights(200,100)
        self.light22 = Lights(200,200)
        self.light32 = Lights(200,300)
        self.light42 = Lights(200,400)
        self.light03 = Lights(300,0)
        self.light13 = Lights(300,100)
        self.light23 = Lights(300,200) 
        self.light33 = Lights(300,300)
        self.light43 = Lights(300,400)
        self.light04 = Lights(400,0)
        self.light14 = Lights(400,100)
        self.light24 = Lights(400,200)
        self.light34 = Lights(400,300)
        self.light44 = Lights(400,400)
        self.light_out00 = Lights_out(0,0)
        self.light_out10 = Lights_out(0,100)
        self.light_out20 = Lights_out(0,200)
        self.light_out30 = Lights_out(0,300)
        self.light_out40 = Lights_out(0,400)
        self.light_out01 = Lights_out(100,0)
        self.light_out11 = Lights_out(100,100)
        self.light_out21 = Lights_out(100,200)
        self.light_out31 = Lights_out(100,300)
        self.light_out41 = Lights_out(100,400)
        self.light_out02 = Lights_out(200,0)
        self.light_out12 = Lights_out(200,100)
        self.light_out22 = Lights_out(200,200)
        self.light_out32 = Lights_out(200,300)
        self.light_out42 = Lights_out(200,400)
        self.light_out03 = Lights_out(300,0)
        self.light_out13 = Lights_out(300,100)
        self.light_out23 = Lights_out(300,200) 
        self.light_out33 = Lights_out(300,300)
        self.light_out43 = Lights_out(300,400)
        self.light_out04 = Lights_out(400,0)
        self.light_out14 = Lights_out(400,100)
        self.light_out24 = Lights_out(400,200)
        self.light_out34 = Lights_out(400,300)
        self.light_out44 = Lights_out(400,400)
        self.pika = Pika(900, 400)
        self.bulle1 = Bulle1(600, 50)
        self.bulle2 = Bulle2(600, 50)


        #self.message = Message(500, 100)    

# gestion des évènements
    def handling_events(self):
        while self.running:
            self.update()
            self.display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

#mises à jour du jeu
    def update(self):
        pass

    def changer_matrice(self):
        for i in range(0,4):
            for j in range(0,4):
                if eval("self.light"+str(i)+str(j)):
                    if self.grille[i,j]==1:
                       self.grille[i,j]=0
                    else:
                        self.grille[i,j]=1
                    if i+1 >4:
                        continue
                    elif 


        

# affichage
    def display(self):

        for i in range (0,5):
            for j in range (0,5):
                if self.grille[i,j]==1:
                    eval("self.light"+str(i)+str(j)+".draw(screen)")
                else:
                    eval("self.light_out"+str(i)+str(j)+".draw(screen)")


                      
        self.pika.draw(screen)
    
        self.bulle2.draw(screen)     
      #  self.message.message1(screen)
        pygame.display.flip()
        

    def run(self):
        while self.running:
            self.handling_events()
            self.changer_matrice()
            self.update()
            self.display()


pygame.init()

screen = pygame.display.set_mode((1080,720))
game = game(screen)
game.run()




    


