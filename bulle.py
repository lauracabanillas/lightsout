import pygame

image1 = pygame.image.load("./images/image_bulle1.png")
image_lights1 = pygame.transform.scale(image1, (430,400))

image2 = pygame.image.load("./images/image_bulle2.png")
image_lights2 = pygame.transform.scale(image2, (430,400))

class Bulle1:
    def __init__(self, x, y):
        self.image = image_lights1
        self.rect = self.image.get_rect(x=x, y=y) 

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Bulle2:
    def __init__(self, x, y):
        self.image = image_lights2
        self.rect = self.image.get_rect(x=x, y=y) 

    def draw(self, screen):
        screen.blit(self.image, self.rect)

