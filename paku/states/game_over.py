import utils

import pyxel

import globals
from globals import player1
from globals import dij_b, bf_b, restart_b, exit_b
from states.gamestate import GameState

class GameOverState(GameState):
    def __init__(self) -> None:
        super().__init__()


    def update(self):
        super().update()
        restart_b.update()
        exit_b.update()
        if exit_b.is_on:
            pyxel.quit()
        if restart_b.is_on:
            globals.next_state = "menu"
            restart_b.is_on = False
            dij_b.is_on = False
            bf_b.is_on = False

    def draw(self):
        super().draw()
        text_score = f'PONTOS: {player1.points}'
        text_gameOver = 'GAME OVER'
        pyxel.text(utils.align_text(utils.WIDTH/2, text_score) -1, utils.HEIGHT/2, text_score, 7)
        pyxel.text(utils.align_text(utils.WIDTH/2, text_gameOver),utils.HEIGHT/2-20, text_gameOver, 7)
        restart_b.draw()
        exit_b.draw()