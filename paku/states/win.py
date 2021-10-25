import utils

import pyxel

from states.game_over import GameOverState

class WinState(GameOverState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        super().update()

    def draw(self):
        super().draw()
        self.title_text = 'PARABENS!'
        pyxel.rect(utils.WIDTH/2-25, utils.HEIGHT/2-25, 50, 15, 0)
        pyxel.text(utils.align_text(utils.WIDTH/2, self.title_text),utils.HEIGHT/2-20, self.title_text, 7)
