import pygame

image1 = pygame.image.load("./images/light.jpg")
image_lights = pygame.transform.scale(image1, (100,100))

class Lights:
    def __init__(self, x, y):
        self.image = image_lights
        self.rect = self.image.get_rect(x=x, y=y) 
        self.clicked = False

    def draw(self, screen):
# variable pour détecter dans le programme principal quand une lights est cliquée
        event = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouse and click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] ==1 and self.clicked == False:
                self.clicked = True
                event = True
                       
            if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False
            
        if event == False :
            screen.blit(self.image, self.rect)

        return event
                


       


