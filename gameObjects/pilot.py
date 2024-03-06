from .mobile import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION
from gameObjects.drawable import Drawable
from pygame.locals import *

import pygame
import numpy as np

worldSize = vec(*RESOLUTION)

class Orb(Mobile):
    def __init__(self, position, direction):
        super().__init__(position, "orb.png")
        self.direction = direction
        self.speed = 1000  # You can adjust this value
        

    def update(self, seconds):
        self.position += self.direction * self.speed * seconds
        super().update(seconds)
        
         
class Pilot(Mobile):
   def __init__(self, position):
      super().__init__(position, "pilot1.png")
      
      self.direction = vec(0,0)
   
      # Animation variables specific to Pilot
      self.framesPerSecond = 6.67
      self.nFrames = 6
      
      self.nFramesList = {
         "moving"   : 6,
         "standing" : 6
      }
      
      self.rowList = {
         "moving"   : 1,
         "standing" : 0
      }
      
      self.framesPerSecondList = {
         "moving"   : 6.67,
         "standing" : 6.67
      }
            
      self.FSManimated = WalkingFSM(self)
      self.LR = AccelerationFSM(self, axis=0)
      self.UD = AccelerationFSM(self, axis=1)

      self.orbs = []  # Add this line to create a group for orbs

      
   def draw(self, drawSurface):
      super().draw(drawSurface)
      for orbs in self.orbs:
         orbs.draw(drawSurface)
      
      
   def handleEvent(self, event):
      if event.type == KEYDOWN:
         if event.key == K_UP:
            self.direction =  vec(0,-1)
            self.UD.decrease()
             
         elif event.key == K_DOWN:
            self.direction =  vec(0,1)
            self.UD.increase()
            
         elif event.key == K_LEFT:
            self.direction =  vec(-1,0)
            self.flipImage[0] = True
            self.LR.decrease()
            
         elif event.key == K_RIGHT:
            self.direction =  vec(1,0)
            self.flipImage[0] = False
            self.LR.increase()
            
            

      elif event.type == KEYUP:
         if event.key == K_UP:
            self.UD.stop_decrease()
             
         elif event.key == K_DOWN:
            self.UD.stop_increase()
             
            
         elif event.key == K_LEFT:
            self.LR.stop_decrease()
            
         elif event.key == K_RIGHT:
            self.LR.stop_increase()

      elif event.type == MOUSEBUTTONDOWN:
            self.orbs.append(Orb(self.position, self.direction))
            

   def update(self, seconds): 
      for orbs in self.orbs:
         orbs.update(seconds)
      self.LR.update(seconds)
      self.UD.update(seconds)

      
      
      
      
      super().update(seconds)

   def updateMovement(self):
      pass
   
