import pygame

from . import Drawable, Pilot, Pistol

from utils import vec, RESOLUTION

class GameEngine(object):
    import pygame

    def __init__(self):       
        self.pilot = Pilot((0,0))
        self.pistol = Pistol((200,200))
        self.size = vec(*RESOLUTION)
        self.background = Drawable((0,0), "background.png")
    
    def draw(self, drawSurface):        
        self.background.draw(drawSurface)
        
        self.pilot.draw(drawSurface)
        

        self.pistol.draw(drawSurface)
            
    def handleEvent(self, event):
        self.pilot.handleEvent(event)
        self.pistol.handleEvent(event)
    
    def update(self, seconds):
        self.pilot.update(seconds)
        
        self.pistol.update(seconds)
        
        Drawable.updateOffset(self.pilot, self.size)
        Drawable.updateOffset(self.pistol, self.size)
    

