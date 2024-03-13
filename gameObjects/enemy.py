from .mobile import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION
from gameObjects.drawable import Drawable
from pygame.locals import *
from gameObjects.pilot import Orb

import pygame
import numpy as np

class Enemy(Mobile):
    def __init__(self, position, direction):
        super().__init__(position, "enemy1.png")
        self.direction = direction
        self.speed = 50  # You can adjust this value

        self.framesPerSecond = 6.67
        self.nFrames = 6

        self.hitCounter = 0
        self.nFramesList = {
            "moving": 6,
            "standing": 6
        }
        self.rowList = {
            "moving": 1,
            "standing": 0
        }

        self.framesPerSecondList = {
            "moving": 6.67,
            "standing": 6.67
        }

        self.FSManimated = WalkingFSM(self)
        self.orbs = []
    def hit(self):
        self.hitCounter += 1
        if self.hitCounter == 3:
            self.kill()
            self.hitCounter = 0

    def update(self, seconds):
        # Move in the direction
        self.position += self.direction * self.speed * seconds
        self.FSManimated.update(seconds)

        for orb in self.orbs:
            if self.rect.colliderect(orb.rect):
                self.hit()
                
        super().update(seconds)