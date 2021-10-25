from entity import Entity
import utils

import time
import pyxel
import random

class Ghost(Entity):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.state = "chase"
        self.posX = utils.align_in_grid(x) + 1
        self.posY = utils.align_in_grid(y) + 1
        self.home = [self.posX, self.posY]
        self.target = None
        self.color = 0
        self.base_color = 0
        self.ghost_path = []
        self.countdown = 0

    def update(self):
        if self.state == "frightened":
            if round(time.time()) - self.countdown == 15:
                self.change_state("chase")
        if self.state == "eaten":
            if round(time.time()) - self.countdown == 10:
                self.change_state("chase")
      
    def draw(self):

        if self.state != "eaten":
            # CORPO
            pyxel.circ(self.posX, self.posY, 4, self.color)
            utils.rect_custom(self.posX-4, self.posY, self.posX+5, self.posY+5, self.color)

            # PERNINHAS
            if pyxel.frame_count%30 >= 15:
                if self.state == "frightened" and round(time.time()) - self.countdown >= 10:
                    self.color = self.base_color
                pyxel.pset(self.posX-4, self.posY+5, self.color)
                pyxel.pset(self.posX-2, self.posY+5, self.color)
                pyxel.pset(self.posX, self.posY+5, self.color)
                pyxel.pset(self.posX+2, self.posY+5, self.color)
                pyxel.pset(self.posX+4, self.posY+5, self.color)
            else:
                if self.state == "frightened" and round(time.time()) - self.countdown >= 10:
                    self.color = 12
                pyxel.pset(self.posX-3, self.posY+5, self.color)
                pyxel.pset(self.posX-1, self.posY+5, self.color)
                pyxel.pset(self.posX+1, self.posY+5, self.color)
                pyxel.pset(self.posX+3, self.posY+5, self.color)
        
        # OLHOS
        pyxel.circ(self.posX-2, self.posY-1, 1, 7)
        pyxel.circ(self.posX+2, self.posY-1, 1, 7)
        pyxel.pset(self.posX-2, self.posY-1, 0)
        pyxel.pset(self.posX+2, self.posY-1, 0)
        
        
    
    def random_move(self):
        dir = self.directions()

        if dir == []:
            dir = ["up", "down", "right", "left"]

        return random.choice(dir)

    def change_state(self, state):
        self.state = state

        if state == "chase":
            self.facing = utils.inv_dir(self.facing)
            self.color = self.base_color

        if state == "frightened":
            self.facing = utils.inv_dir(self.facing)
            self.color = 12
            self.countdown = round(time.time())

        if state == "eaten":
            self.posX = self.home[0]
            self.posY = self.home[1]
            self.color = 0
            self.countdown = round(time.time())
            
    def reset(self, x, y):
        self.state = "chase"
        self.posX = utils.align_in_grid(x) + 1
        self.posY = utils.align_in_grid(y) + 1
        self.home = [self.posX, self.posY]
        self.target = None
        self.color = 0
        self.base_color = 0
        self.countdown = 0                    
