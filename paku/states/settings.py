import utils

import pyxel
from math import dist

import globals
from globals import ghosts_id
from globals import mirror_b, dij_b, bf_b, kruskal_b, prim_b, ghost1_b, ghost2_b, ghost3_b, ghost4_b, back_b
from states.gamestate import GameState

# Estado de configurações, chamado também de ajustes
class SettingsState(GameState):
    def __init__(self) -> None:
        super().__init__()
        self.description = ""

    def update(self):
        super().update()
        
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

        if back_b.update():
            globals.next_state = "menu"

        
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        if dist(mouse_pos, [mirror_b.posx, mirror_b.posy]) < mirror_b.radius:
            self.description = mirror_b.description
        elif dist(mouse_pos, [dij_b.posx, dij_b.posy]) < dij_b.radius:
            self.description = dij_b.description
        elif dist(mouse_pos, [bf_b.posx, bf_b.posy]) < bf_b.radius:
            self.description = bf_b.description
        elif dist(mouse_pos, [kruskal_b.posx, kruskal_b.posy]) < kruskal_b.radius:
            self.description = kruskal_b.description
        elif dist(mouse_pos, [prim_b.posx, prim_b.posy]) < prim_b.radius:
            self.description = prim_b.description
        
        elif dist(mouse_pos, [ghost1_b.posx, ghost1_b.posy]) < ghost1_b.radius:
            self.description = ghost1_b.description
        elif dist(mouse_pos, [ghost2_b.posx, ghost2_b.posy]) < ghost2_b.radius:
            self.description = ghost2_b.description
        elif dist(mouse_pos, [ghost3_b.posx, ghost3_b.posy]) < ghost3_b.radius:
            self.description = ghost3_b.description
        elif dist(mouse_pos, [ghost4_b.posx, ghost4_b.posy]) < ghost4_b.radius:
            self.description = ghost4_b.description
        else:
            self.description = ""


    def draw(self):
        super().draw()

        # Desenha grid
        pyxel.text(30, 4, "ROTAS:", 7)
        pyxel.line(0, utils.HEIGHT//3, utils.WIDTH, utils.HEIGHT//3, 7)
        pyxel.text(3, utils.HEIGHT//3+4, "LABIRINTO:", 7)
        pyxel.line(0, (utils.HEIGHT//3)*2, utils.WIDTH, (utils.HEIGHT//3)*2, 7)
        pyxel.text(3, (utils.HEIGHT//3)*2+4, "FANSTASMAS:", 7)
        pyxel.line(utils.WIDTH/2, (utils.HEIGHT//3)*2, utils.WIDTH/2, utils.HEIGHT, 7)

        
        pyxel.text(utils.align_text((utils.WIDTH/4)*3, "Algoritmo Gerador"), utils.HEIGHT/2-20, "Algoritmo Gerador", 7)
        pyxel.text(utils.WIDTH/2+10, ((utils.HEIGHT/3)*2)+10, self.description, 7)

        back_b.draw()
        mirror_b.draw()
        dij_b.draw()
        bf_b.draw()
        prim_b.draw()
        kruskal_b.draw()

        ghost1_b.text, ghost1_b.description = utils.pick_ghost_info(ghosts_id[0])
        ghost2_b.text, ghost2_b.description = utils.pick_ghost_info(ghosts_id[1])
        ghost3_b.text, ghost3_b.description = utils.pick_ghost_info(ghosts_id[2])
        ghost4_b.text, ghost4_b.description = utils.pick_ghost_info(ghosts_id[3])

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