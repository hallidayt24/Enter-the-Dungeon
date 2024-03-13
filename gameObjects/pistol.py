from .mobile import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION
from gameObjects.drawable import Drawable
from pygame.locals import *

import pygame
import numpy as np



class Pistol(Mobile):
    def __init__(self, position):
        super().__init__(position, "pistol.png")

        self.angle = 0
        self.image = pygame.transform.scale(self.image, (1000, 1000))  # Resize the image
        self.rect = self.image.get_rect()

    def handleEvent(self, event):
        if event.type == MOUSEMOTION:
            self.update_angle(event.pos)

    def update_angle(self, mouse_pos):
        rel_x, rel_y = mouse_pos[0] - self.position[0], mouse_pos[1] - self.position[1]
        self.angle = (180 / np.pi) * -np.arctan2(rel_y, rel_x)

    def update(self, seconds): 
        self.rimage = pygame.transform.rotate(self.image, self.angle)
        self.image = pygame.transform.scale(self.rimage, (1000, 1000))
        self.rect = self.image.get_rect(center=self.rect.center)

        super().update(seconds)

    def updateMovement(self):
        pass