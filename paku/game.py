import utils 
import globals
import states.gamestate as gs

import pyxel

class Game:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="PAKU PAKU 2", fps=30)
        pyxel.mouse(True)       
        pyxel.load("assets.pyxres")
        
        pyxel.run(self.update, self.draw)

    def update(self):
        globals.current_state.update()

        utils.change_state()

    def draw(self):
        globals.current_state.draw()        

        
Game()