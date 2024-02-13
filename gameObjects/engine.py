import pygame

from . import Drawable, Pilot

from utils import vec, RESOLUTION

class GameEngine(object):
    import pygame

    def __init__(self):       
        self.pilot = Pilot((0,0))
        self.size = vec(*RESOLUTION)
        self.background = Drawable((0,0), "background.png")
    
    def draw(self, drawSurface):        
        self.background.draw(drawSurface)
        
        self.pilot.draw(drawSurface)
            
    def handleEvent(self, event):
        self.pilot.handleEvent(event)
    
    def update(self, seconds):
        self.pilot.update(seconds)
        
        Drawable.updateOffset(self.pilot, self.size)
    

