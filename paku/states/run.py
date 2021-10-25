import utils

import pyxel

import globals
from globals import player1, ghosts, pellets_list
from globals import dij_b, bf_b
from states.gamestate import GameState

class RunState(GameState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        super().update()
        player1.update()
        # (player1.atNode)
        
        if pyxel.frame_count % 30 == 0 and player1.isAlive:
            self.timer += 1
        
        for i in range(len(ghosts)):
            if ghosts[i].base_color == 6:
                ghosts[i].friend_pos = [ghosts[(i+1)%4].posX, ghosts[(i+1)%4].posY]
            ghosts[i].update(player1.atNode, player1.facing)

        # PLAYER PELLET COLISÃO
        player_pos = utils.get_pos_in_grid(player1.posX, player1.posY)
        pellet = pellets_list.pellets_dict.get(player_pos)
        if pellet != None:
            pyxel.playm(2, loop=False)
            if pellet == 2:
                player1.points += 40
                for ghost in ghosts:
                    if ghost.state != "eaten":
                        ghost.change_state("frightened")

            pellets_list.pellets_dict.pop(player_pos)
            player1.points += 10

        # PLAYER GHOST COLISÃO
        for ghost in ghosts:
            if utils.col_player_ghost(player1.posX, player1.posY, ghost.posX, ghost.posY):
                if ghost.state == "chase" and player1.isAlive:
                    player1.kill_player()
                    pyxel.playm(1, loop=False)

                    utils.register_record("PLAYER", player1.points, self.timer)
                elif ghost.state == "frightened":
                    player1.points += 100
                    ghost.change_state("eaten")

        if pellets_list.pellets_dict == {}:
            globals.next_state = "win"

        if not player1.isAlive and pyxel.frame_count % player1.death_animation >= 70:
            globals.next_state = "game_over"

    def draw(self):
        super().draw()
        utils.draw_grid()

        for i in range(0, len(utils.edges)):
            utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
        
        pyxel.text(20, utils.HEIGHT-10,  f"TEMPO: {(self.timer//60):02d}:{(self.timer%60):02d}", 7)
        pyxel.text(utils.WIDTH-60, utils.HEIGHT-10, f'PONTOS: {player1.points}', 7)

        for i in range(len(ghosts)):
            if ghosts[i].ghost_path != []:
                if (ghosts[i].base_color == 8 and dij_b.is_on) or (ghosts[i].base_color == 2 and bf_b.is_on):
                    for j in ghosts[i].ghost_path:
                        pos = utils.coord_int(j)
                        pyxel.circ(utils.align_in_grid(pos[0]), utils.align_in_grid(pos[1]), 2, ghosts[i].base_color)

        pellets_list.draw()
        player1.draw()
        
        for ghost in ghosts:
            ghost.draw()