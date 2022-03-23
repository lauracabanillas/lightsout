import pygame

font = pygame.font.Font('freesansbold.ttf', 32)
img = font.render('Les solutions du jeu Lights Out', True, green, blue)

class Message:
    def __init__(self, x, y):
        self.rect = self.image.get_rect(x=x, y=y) 
        self.image = img

    def message1(self, screen):
        screen.blit(self.image, self.rect)