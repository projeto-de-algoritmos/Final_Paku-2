import pyxel

class GameState:

    def __init__(self):
        self.timer = 0
        # self.state = "menu"
        # self.points = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()           

    def draw(self):
        pyxel.cls(0)