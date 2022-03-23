import pygame

image1 = pygame.image.load("./images/light_out.jpg")
image_lights = pygame.transform.scale(image1, (100,100))

class Lights_out:
    def __init__(self, x, y):
        self.image = image_lights
        self.rect = self.image.get_rect(x=x, y=y) 

    def draw(self, screen):
        screen.blit(self.image, self.rect)