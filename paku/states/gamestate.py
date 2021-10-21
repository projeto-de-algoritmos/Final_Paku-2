import utils
import prim
import player
import pellets
from buttons import PlayButton, Button, ExitButton

from ghosts.blinky import Blinky 
from ghosts.clyde import Clyde
from ghosts.pinky import Pinky
from ghosts.inky import Inky

import pyxel
import random


player1 = player.Player()
ghosts = []
ghosts.append(Blinky(0, 0))
ghosts.append(Inky(0, utils.GRID_HEIGHT-1))
ghosts.append(Pinky(utils.GRID_WIDTH-1, 0))
ghosts.append(Clyde(utils.GRID_WIDTH-1, utils.GRID_HEIGHT-1))

# ghosts[0].state = "eaten"
# ghosts[1].state = "eaten"
# ghosts[2].state = "eaten"
# ghosts[3].state = "eaten"

pellets_list = pellets.Pellets()

mirror_b = Button("Espelhar Labirinto", utils.WIDTH/4-20, utils.HEIGHT/2 )
start_b = PlayButton("Jogar", utils.WIDTH/2, utils.HEIGHT/2 )
dij_b = Button("Mostrar Dijkstra", utils.WIDTH/2+utils.WIDTH/4+20, utils.HEIGHT/2 )

restart_b = PlayButton("Jogar", utils.WIDTH/2-60, utils.HEIGHT/2 )
exit_b = ExitButton("Sair", utils.WIDTH/2+60, utils.HEIGHT/2 )

class GameState:

    def __init__(self):
        self.state = "menu"
        self.points = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if(self.state == "menu"):
            if start_b.update():
                print("start")
            if mirror_b.update():
                print("mirror")
            if dij_b.update():
                print("dij")

            if start_b.isOn:
                self.state = "start"
                start_b.isOn = False

        if(self.state == "start"):
            pyxel.playm(0, loop=False)

            player1.reset()

            ghosts[0].reset(0, 0)
            ghosts[1].reset(0, utils.GRID_HEIGHT-1)
            ghosts[2].reset(utils.GRID_WIDTH-1, 0)
            ghosts[3].reset(utils.GRID_WIDTH-1, utils.GRID_HEIGHT-1)

            pellets_list.reset()
            pellets_list.fill_dict()

            utils.g.reset()
            utils.path.reset
            utils.edges = []
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

            # if menu var ...
            start = utils.coord_str(random.randint(0, utils.GRID_WIDTH-1), random.randint(0, utils.GRID_HEIGHT-1))
            utils.path, utils.edges = prim.prim_maze(utils.g, start, utils.edges)

            # utils.path, utils.edges = utils.mirror(utils.path, utils.edges)

            if mirror_b.isOn:
                utils.path = utils.mirror()
                mirror_b.isOn = False

            self.state = "prim"
                
        elif(self.state == "prim"):

            if(utils.delay!=len(utils.edges)-1):
                utils.delay += 1
            else:
                pyxel.playm(2, loop=True)
                self.state = "run"

        elif(self.state == "run"):
            player1.update()
            (player1.atNode)

            ghosts[1].blinky_pos = [ghosts[0].posX, ghosts[0].posY]
            for ghost in ghosts:
                ghost.update(player1.atNode, player1.facing)

            if pyxel.btnp(pyxel.KEY_P):
                pyxel.stop()

            # PLAYER PELLET COLISÃO
            player_pos = utils.get_pos_in_grid(player1.posX, player1.posY)
            pellet = pellets_list.pellets_dict.get(player_pos)
            if pellet != None:
                if pellet == 2:
                    player1.points += 40
                    for ghost in ghosts:
                        if ghost.state != "eaten":
                            ghost.change_state("frightened")

                pellets_list.pellets_dict.pop(player_pos)
                player1.points += 10

            # PLAYER GHOST COLISÃO
            for ghost in ghosts:
                # print(ghost.atNode.get_id())
                if player1.atNode.get_id() == ghost.atNode.get_id():
                    if ghost.state == "chase":
                        player1.kill_player()
                        pyxel.playm(1, loop=False)
                        # player1.isAlive = False
                    elif ghost.state == "frightened":
                        player1.points += 100
                        ghost.change_state("eaten")

            if pellets_list.pellets_dict == {}:
                self.state = "win"

            if player1.isAlive == False:
                self.state = "game_over"

                    
            
        elif(self.state == "win" or self.state == "game_over"):
            restart_b.update()
            exit_b.update()
            if exit_b.isOn:
                pyxel.quit()
            if restart_b.isOn:
                self.state = "menu"
                restart_b.isOn = False
                dij_b.isOn = False

                


    def draw(self):
        pyxel.cls(1)

        if(self.state == "menu"):
            pyxel.cls(0)
            title = 'PaKu PaKu'
            pyxel.text(utils.align_fix(utils.WIDTH/2, title),40, title, 7)
            start_b.draw()
            mirror_b.draw()
            dij_b.draw()
            
        elif(self.state == "start"):
            utils.draw_grid()
            
        elif(self.state == "prim"):
            utils.draw_grid()

            if utils.edges != []:
                for i in range(0, utils.delay+1):
                    utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
            
            pellets_list.draw()
            player1.draw()

            for ghost in ghosts:
                ghost.draw()


            
        elif(self.state == "run"):
            utils.draw_grid()

            for i in range(0, len(utils.edges)):
                utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
            
            pyxel.text(10, utils.HEIGHT-10, """Pressione "P" remover o som de Paku""", 7)
            pyxel.text(utils.WIDTH-60, utils.HEIGHT-10, f'PONTOS: {player1.points}', 7)

            if dij_b.isOn:
                if ghosts[0].gost_path != []:
                    for i in ghosts[0].gost_path:
                        pos = utils.coord_int(i)
                        pyxel.circ(utils.align_in_grid(pos[0]), utils.align_in_grid(pos[1]), 2, 8)

            pellets_list.draw()
            player1.draw()
            
            for ghost in ghosts:
                ghost.draw()

            

        elif(self.state == "win"):
            pyxel.cls(0)
            text_score = f'PONTOS: {player1.points}'
            pyxel.text(utils.align_fix(utils.WIDTH/2, "Ganhou!") -1, utils.HEIGHT/2, "Ganhou!", 7)
            pyxel.text(utils.align_fix(utils.WIDTH/2, text_score) -1, utils.HEIGHT/2, text_score, 7)
            restart_b.draw()
            exit_b.draw()

        elif(self.state == "game_over"):
            pyxel.cls(0)
            text_score = f'PONTOS: {player1.points}'
            text_gameOver = 'GAME OVER'
            # pyxel.text(utils.x_fix(utils.WIDTH/2, txt)-1, utils.HEIGHT/2+70-1, txt, outline_col)
            pyxel.text(utils.align_fix(utils.WIDTH/2, text_score) -1, utils.HEIGHT/2, text_score, 7)
            pyxel.text(utils.align_fix(utils.WIDTH/2, text_gameOver),utils.HEIGHT/2-20, text_gameOver, 7)
            restart_b.draw()
            exit_b.draw()

