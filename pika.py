import pygame

image1 = pygame.image.load("./images/pikatchu.jpg")
image_pika = pygame.transform.scale(image1, (150,300))

class Pika:
    def __init__(self, x, y):
        self.image = image_pika
        self.rect = self.image.get_rect(x=x, y=y) 

    def draw(self, screen):
        screen.blit(self.image, self.rect)