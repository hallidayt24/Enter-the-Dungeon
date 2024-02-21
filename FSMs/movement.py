from . import AbstractGameFSM
from utils import vec, magnitude, EPSILON, scale, RESOLUTION

from statemachine import State
import pygame

class MovementFSM(AbstractGameFSM):
    
    def __init__(self, obj):
        super().__init__(obj)
    
    
    def update(self, seconds):
        super().update(seconds)
    


class AccelerationFSM(MovementFSM):
    """Axis-based acceleration with gradual stopping."""
    not_moving = State(initial=True)
    
    negative = State()
    positive = State()
    
    stalemate = State()
    
    decrease  = not_moving.to(negative) | positive.to(stalemate)
    
    increase = not_moving.to(positive) | negative.to(stalemate)
    
    stop_decrease = negative.to(not_moving) | stalemate.to(positive) | not_moving.to.itself(internal = True) | positive.to.itself(internal = True)
    
    stop_increase = positive.to(not_moving) | stalemate.to(negative) | not_moving.to.itself(internal = True) | negative.to.itself(internal = True)
    
    
    stop_all      = not_moving.to.itself(internal=True) | negative.to(not_moving) | \
                    positive.to(not_moving) | stalemate.to(not_moving)
    
    def __init__(self, obj, axis=0):
        self.axis      = axis
        self.direction = vec(0,0)
        self.direction[self.axis] = 1
        self.accel = 200
        self.flipped = False
        self.original_flipped = False
        # self.flip_x = False
        
        super().__init__(obj)

    def update(self, seconds=0):
        
        if self.obj.velocity[self.axis] < 0:
            if self.flipped != self.original_flipped:
                print("Flipping")
                self.obj.image = pygame.transform.flip(self.obj.image, True, False)
                self.flipped = not self.flipped
        elif self.obj.velocity[self.axis] > 0:
            if self.flipped == self.original_flipped :
                self.obj.image = pygame.transform.flip(self.obj.image, True, False)
                self.flipped = not self.flipped
        if self.obj.position[self.axis] < 0:
            self.stop_decrease()
            self.obj.velocity[self.axis] = max(0, self.obj.velocity[0])
        elif self.obj.position[self.axis] > RESOLUTION[self.axis] - self.obj.getSize()[self.axis]:
            self.stop_increase()
        if self.obj.position[self.axis] < 0:
            self.stop_decrease()
            self.obj.velocity[self.axis] = min(0, self.obj.velocity[0])
        elif self.obj.position[self.axis] > RESOLUTION[self.axis] - self.obj.getSize()[self.axis]:
            self.stop_increase()
        
        
            

        if self == "positive":
            self.obj.velocity += self.direction * self.accel * seconds
        elif self == "negative":
            self.obj.velocity -= self.direction * self.accel * seconds

       
                

                
        elif self == "stalemate":
            pass
        else:
            if self.obj.velocity[self.axis] > self.accel * seconds:
                self.obj.velocity[self.axis] -= self.accel * seconds
            elif self.obj.velocity[self.axis] < -self.accel * seconds:
                self.obj.velocity[self.axis] += self.accel * seconds
            else:
                self.obj.velocity[self.axis] = 0

        # if self ==  "negative":  # Moving left
        #     print("Moving left")
        #     self.flip_x = True
        # else:
        #     self.flip_x = False

        # if self.flip_x != self.flipped:
        #     self.obj.image = pygame.transform.flip(self.obj.image, self.flip_x, False)
        #     self.flipped = self.flip_x

        
        super().update(seconds)