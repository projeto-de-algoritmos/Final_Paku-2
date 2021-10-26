import pyxel

# Classe abstrata, pai para todos os estados do jogo
class GameState:

    def __init__(self):
        self.timer = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()           

    def draw(self):
        pyxel.cls(0)