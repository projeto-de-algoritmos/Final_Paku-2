import utils
from entity import Entity
import pyxel

class Player(Entity):
    def __init__(self):
        super().__init__()
        
        self.posX = 128
        self.posY = 98
        self.isAlive = True
        self.facing = "right"
        self.points = 0
        self.death_animation = 0

    def update(self):
        self.atNode = utils.get_node_in_grid(self.posX, self.posY)

        # if self.death_animation != 0:
        #     if pyxel.frame_count % self.death_animation > 70:
        #         self.isAlive = False 
                
        if self.isAlive:
        
            if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
                self.canTurn = True
            else:
                self.canTurn = False
            
            if self.isAlive and self.canTurn:
                if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
                    self.turn("up")
                elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
                    self.turn("left")
                elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
                    self.turn("down")
                elif pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                    self.turn("right")
                   

            self.move()

    def draw(self):

        if self.death_animation == 0:

            if pyxel.frame_count%15 >= 7:
                frame = 0
            else:
                frame = 1

            if self.facing == "right":
                pyxel.blt(self.posX-7, self.posY-8, 0, frame*16, 0, 16, 16, 0)
            if self.facing == "left":
                pyxel.blt(self.posX-7, self.posY-8, 0, frame*16, 16, 16, 16, 0)
            if self.facing == "down":
                pyxel.blt(self.posX-8, self.posY-8, 0, frame*16, 32, 16, 16, 0)
            if self.facing == "up":
                pyxel.blt(self.posX-8, self.posY-8, 0, frame*16, 48, 16, 16, 0)

        else:

            frame = 6
            for i in range(0, 7):
                if pyxel.frame_count % self.death_animation < 10*i:
                    frame = i
                    break

            
            pyxel.blt(self.posX-8, self.posY-8, 0, frame*16, 0, 16, 16, 0)
            


    def kill_player(self):
        self.isAlive = False
        if self.death_animation == 0:    
            self.death_animation = pyxel.frame_count

    def reset(self):
        self.posX = 128
        self.posY = 98
        self.isAlive = True
        self.facing = "right"
        self.points = 0
        self.death_animation = 0