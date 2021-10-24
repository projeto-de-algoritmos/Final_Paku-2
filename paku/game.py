import utils 
import states.gamestate as gs

import pyxel

class Game:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="Project Paku", fps=30)
        pyxel.mouse(True)       
        pyxel.load("assets.pyxres")

        self.gamestate = gs.GameState()
        self.gamestate.state = "records"

        pyxel.run(self.update, self.draw)

    def update(self):
        self.gamestate.update()


    def draw(self):
        self.gamestate.draw()        
        
Game()