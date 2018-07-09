import pygame
from pygame.locals import *
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite)

	def __init__(self, color, width, height):

		super().__init__()

		self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.image = pygame.image.load("Things/Pictures/square.png")
        self.rect = self.image.get_rect()
