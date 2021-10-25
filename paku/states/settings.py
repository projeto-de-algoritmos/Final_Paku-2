import utils

import globals
from globals import ghosts_id
from globals import mirror_b, dij_b, bf_b, kruskal_b, prim_b, ghost1_b, ghost2_b, ghost3_b, ghost4_b, back_b
from states.gamestate import GameState

class SettingsState(GameState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        super().update()
        back_b.update()
        mirror_b.update()
        dij_b.update()
        bf_b.update()

        if ghost1_b.update():
            ghosts_id[0] = (ghosts_id[0]+1)%5
        if ghost2_b.update():
            ghosts_id[1] = (ghosts_id[1]+1)%5
        if ghost3_b.update():
            ghosts_id[2] = (ghosts_id[2]+1)%5
        if ghost4_b.update():
            ghosts_id[3] = (ghosts_id[3]+1)%5

        prim_b.update()
        if prim_b.is_on:
            kruskal_b.is_on = False
        else:
            kruskal_b.is_on = True

        kruskal_b.update()
        if kruskal_b.is_on:
            prim_b.is_on = False
        else:
            prim_b.is_on = True

        if back_b.is_on:
            back_b.is_on = False
            globals.next_state = "menu"

    def draw(self):
        super().draw()
        back_b.draw()
        mirror_b.draw()
        dij_b.draw()
        bf_b.draw()
        prim_b.draw()
        kruskal_b.draw()

        ghost1_b.draw()
        draw_ghost = utils.pick_ghost(ghosts_id[0], 0)
        draw_ghost.posX = ghost1_b.posx
        draw_ghost.posY = ghost1_b.posy-20
        draw_ghost.draw()

        ghost2_b.draw()
        draw_ghost = utils.pick_ghost(ghosts_id[1], 0)
        draw_ghost.posX = ghost2_b.posx
        draw_ghost.posY = ghost2_b.posy-20
        draw_ghost.draw()

        ghost3_b.draw()
        draw_ghost = utils.pick_ghost(ghosts_id[2], 0)
        draw_ghost.posX = ghost3_b.posx
        draw_ghost.posY = ghost3_b.posy-20
        draw_ghost.draw()

        ghost4_b.draw()
        draw_ghost = utils.pick_ghost(ghosts_id[3], 0)
        draw_ghost.posX = ghost4_b.posx
        draw_ghost.posY = ghost4_b.posy-20
        draw_ghost.draw()