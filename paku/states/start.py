import utils
import prim
import kruskal

import pyxel
import random

import globals
from globals import player1, ghosts, ghosts_id, pellets_list
from globals import mirror_b, prim_b
from states.gamestate import GameState

# Estado responsável por setar todas as variáveis para o estado correto antes de um estado 'run' começar
class StartState(GameState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        super().update()
        pyxel.playm(0, loop=False)

        player1.reset()

        ghosts.clear()
        for i in range(4):
            ghosts.append(utils.pick_ghost(ghosts_id[i], i))

        pellets_list.reset()
        pellets_list.fill_dict()

        utils.g.reset()
        utils.path.reset()
        utils.edges = []

        # Código usado para acelerar a animação de construção do labirinto, 
        # utils.delay = 220
        utils.delay = 0

        for i in range(0, utils.GRID_WIDTH):
            for j in range(0, utils.GRID_HEIGHT):
                utils.g.add_node(utils.coord_str(i, j))

        for i in range(0, utils.GRID_WIDTH):
            for j in range(0, utils.GRID_HEIGHT):
                if(i != 0):
                    utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i-1, j), random.randint(1, 20))
                if(j != 0):
                    utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j-1), random.randint(1, 20))
                if(i != utils.GRID_WIDTH-1):
                    utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i+1, j), random.randint(1, 20))
                if(j != utils.GRID_HEIGHT-1):
                    utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j+1), random.randint(1, 20))

        # EDGES = Lista de arestas (string)
        # PATH  = Objeto Grafo com as conexões presentes no labirinto
        if prim_b.is_on:
            start = utils.coord_str(random.randint(0, utils.GRID_WIDTH-1), random.randint(0, utils.GRID_HEIGHT-1))
            utils.path, utils.edges = prim.prim_maze(utils.g, start)
        else:
            utils.path, utils.edges = kruskal.kruskal_maze(utils.g, utils.edges)

        if mirror_b.is_on:
            utils.path = utils.mirror()
            mirror_b.is_on = False

        globals.next_state = "maze"

    def draw(self):
        super().draw()
        pyxel.cls(1)
        utils.draw_grid()
