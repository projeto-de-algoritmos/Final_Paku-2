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
        text_win = 'PARABENS!'
        pyxel.text(utils.align_text(utils.WIDTH/2, text_win),utils.HEIGHT/2-40, text_win, 7)
