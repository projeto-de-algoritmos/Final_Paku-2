from utils import align_fix

from math import dist
import pyxel

class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.posx = x
        self.posy = y
        self.isOn = False
        self.offset = 4
        self.radius = 15
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 0
        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            
            if self.isOn:
                self.isOn = False
                self.offset = 4
            else:
                self.isOn = True
                self.offset = 2

    def draw(self):

        pyxel.circ(self.posx, self.posy, self.radius, 5)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, 12)

        if self.isOn: txt_color = 8
        else: txt_color = 7
        
        pyxel.text(align_fix(self.posx, self.text), self.posy+17, self.text, txt_color)

class PlayButton(Button):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.radius = 30

    def draw(self):
        pyxel.circ(self.posx,  self.posy, self.radius, 9) # Sombra
        pyxel.circ(self.posx,  self.posy-self.offset, self.radius, 10)
        pyxel.circ(self.posx,  self.posy-15-self.offset, 3, 0)
        pyxel.tri(self.posx, self.posy, self.posx+30, self.posy-20, self.posx+30, self.posy+20, 0)

        pyxel.text(align_fix(self.posx, self.text), self.posy+40, self.text, 7)
class ExitButton(Button):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.radius = 30

    def draw(self):
        pyxel.circ(self.posx,  self.posy, self.radius, 9) # Sombra
        pyxel.circ(self.posx,  self.posy-self.offset, self.radius, 10)
        pyxel.circ(self.posx-10,  self.posy-15-self.offset, 3, 0)
        pyxel.circ(self.posx+10,  self.posy-15-self.offset, 3, 0)
        pyxel.line(self.posx-10, self.posy+10-self.offset, self.posx+10, self.posy+10-self.offset, 0)
        pyxel.text(align_fix(self.posx, self.text), self.posy+40, self.text, 7)
        