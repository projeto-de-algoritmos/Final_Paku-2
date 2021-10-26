import utils

import pyxel

import globals
from globals import player1, ghosts, pellets_list, next_state
from states.gamestate import GameState

# Estado em que o labirinto está sendo construído na tela
class MazeState(GameState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        super().update()
        if(utils.delay!=len(utils.edges)-1):
            utils.delay += 1
        else:
            globals.next_state = "run"

    def draw(self):
        super().draw()
        pyxel.cls(1)
        utils.draw_grid()

        if utils.edges != []:
            for i in range(0, utils.delay+1):
                utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
        
        pellets_list.draw()
        player1.draw()

        for ghost in ghosts:
            ghost.draw()