import pygame
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
        self.light1 = Lights(0,0)
        self.light2 = Lights(0,100)
        self.light3 = Lights(0,200)
        self.light4 = Lights(0,300)
        self.light5 = Lights(0,400)
        self.light6 = Lights(100,0)
        self.light7 = Lights(100,100)
        self.light8 = Lights(100,200)
        self.light9 = Lights(100,300)
        self.light10 = Lights(100,400)
        self.light11 = Lights(200,0)
        self.light12 = Lights(200,100)
        self.light13 = Lights(200,200)
        self.light14 = Lights(200,300)
        self.light15 = Lights(200,400)
        self.light16 = Lights(300,0)
        self.light17 = Lights(300,100)
        self.light18 = Lights(300,200) 
        self.light19 = Lights(300,300)
        self.light20 = Lights(300,400)
        self.light21 = Lights(400,0)
        self.light22 = Lights(400,100)
        self.light23 = Lights(400,200)
        self.light24 = Lights(400,300)
        self.light25 = Lights(400,400)
        self.light_out1 = Lights_out(0,0)
        self.light_out2 = Lights_out(0,100)
        self.light_out3 = Lights_out(0,200)
        self.light_out4 = Lights_out(0,300)
        self.light_out5 = Lights_out(0,400)
        self.light_out6 = Lights_out(100,0)
        self.light_out7 = Lights_out(100,100)
        self.light_out8 = Lights_out(100,200)
        self.light_out9 = Lights_out(100,300)
        self.light_out10 = Lights_out(100,400)
        self.light_out11 = Lights_out(200,0)
        self.light_out12 = Lights_out(200,100)
        self.light_out13 = Lights_out(200,200)
        self.light_out14 = Lights_out(200,300)
        self.light_out15 = Lights_out(200,400)
        self.light_out16 = Lights_out(300,0)
        self.light_out17 = Lights_out(300,100)
        self.light_out18 = Lights_out(300,200) 
        self.light_out19 = Lights_out(300,300)
        self.light_out20 = Lights_out(300,400)
        self.light_out21 = Lights_out(400,0)
        self.light_out22 = Lights_out(400,100)
        self.light_out23 = Lights_out(400,200)
        self.light_out24 = Lights_out(400,300)
        self.light_out25 = Lights_out(400,400)
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

# affichage
    def display(self):
        self.light1.draw(screen)
        self.light2.draw(screen)
        self.light3.draw(screen)
        self.light4.draw(screen)
        self.light5.draw(screen)
        self.light6.draw(screen)
        self.light7.draw(screen)
        self.light8.draw(screen)
        self.light9.draw(screen)
        self.light10.draw(screen)
        self.light11.draw(screen)
        self.light12.draw(screen)
        self.light13.draw(screen)
        self.light14.draw(screen)
        self.light15.draw(screen)
        self.light16.draw(screen)
        self.light17.draw(screen)
        self.light18.draw(screen)
        self.light19.draw(screen)
        self.light20.draw(screen)
        self.light21.draw(screen)
        self.light22.draw(screen)
        self.light23.draw(screen)
        self.light24.draw(screen)
        self.light25.draw(screen)
        self.light_out5.draw(screen)
        self.pika.draw(screen)
    
        self.bulle2.draw(screen)     
      #  self.message.message1(screen)
        pygame.display.flip()
        

    def run(self):
        while self.running:
            self.handling_events()
            #self.update()
            #self.display()


pygame.init()

screen = pygame.display.set_mode((1080,720))
game = game(screen)
game.run()




    


