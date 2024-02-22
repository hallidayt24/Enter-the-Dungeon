from .mobile import Mobile
from FSMs import WalkingFSM, AccelerationFSM
from utils import vec, RESOLUTION
from gameObjects.drawable import Drawable
from pygame.locals import *

import pygame
import numpy as np


class Pilot(Mobile):
   def __init__(self, position):
      super().__init__(position, "pilot1.png")
      
      
   
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
      
   
      
      
   def handleEvent(self, event):
      if event.type == KEYDOWN:
         if event.key == K_UP:
            self.UD.decrease()
             
         elif event.key == K_DOWN:
            self.UD.increase()
            
         elif event.key == K_LEFT:
            self.flipImage[0] = True
            self.LR.decrease()
            
         elif event.key == K_RIGHT:
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
      
   def update(self, seconds): 
      self.LR.update(seconds)
      self.UD.update(seconds)
      
      
      
      super().update(seconds)

   def updateMovement(self):
      pass
   
