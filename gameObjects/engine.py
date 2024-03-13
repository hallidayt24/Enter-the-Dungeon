import pygame

from . import Drawable, Pilot, Pistol, Enemy

from utils import vec, RESOLUTION , worldSize

class GameEngine(object):
    import pygame

    def __init__(self):     
        self.size = vec(*RESOLUTION)
        self.pilot = Pilot(self.size / 2)
        self.background = Drawable((0,0), "blackbackground.png")
        self.rooms = {'room1' : Drawable(((0,0)), "room.png")}
        self.floor = Drawable((37,50), "floor.png")
        self.currentRoom = self.rooms['room1']
        self.currentRoom.scale((400,400))
        self.floor.scale((325,300))
        self.enemy = Enemy((100,100), vec(1,0))
    
    def draw(self, drawSurface):        
        self.background.draw(drawSurface)
        self.currentRoom.draw(drawSurface) 
        self.floor.draw(drawSurface)
        self.pilot.draw(drawSurface)
        self.enemy.draw(drawSurface)
            
    def handleEvent(self, event):
        self.pilot.handleEvent(event)
        
    
    def update(self, seconds):
        self.pilot.update(seconds)
        self.enemy.update(seconds)
        
        if self.pilot.position[0] < self.floor.position[0]:
            self.pilot.position[0] = self.floor.position[0]
        elif self.pilot.position[0] > self.floor.position[0] + self.floor.getSize()[0]:
            self.pilot.position[0]= self.floor.position[0] + self.floor.getSize()[0]

        if self.pilot.position[1] < self.floor.position[1]:
            self.pilot.position[1] = self.floor.position[1]
        elif self.pilot.position[1] > self.floor.position[1] + self.floor.getSize()[1]:
            self.pilot.position[1] = self.floor.position[1] + self.floor.getSize()[1]
            
        if self.enemy.position[0] < self.floor.position[0]:
            self.enemy.position[0] = self.floor.position[0]
        elif self.enemy.position[0] > self.floor.position[0] + self.floor.getSize()[0]:
            self.enemy.position[0]= self.floor.position[0] + self.floor.getSize()[0]
        
        if self.enemy.position[1] < self.floor.position[1]:
            self.enemy.position[1] = self.floor.position[1]
        elif self.enemy.position[1] > self.floor.position[1] + self.floor.getSize()[1]:
            self.enemy.position[1] = self.floor.position[1] + self.floor.getSize()[1]
    

