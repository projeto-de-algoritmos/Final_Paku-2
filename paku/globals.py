import pellets
import player

from buttons import PlayButton, CircleButton, ExitButton, PushButton
from states.gamestate import GameState

WIDTH = 256
HEIGHT = 196

current_state = GameState()

# global next_state
next_state = "menu"

player1 = player.Player()
ghosts = []
ghosts_id = [0, 1, 2, 4]

pellets_list = pellets.Pellets()

# BOTOES MENU
start_b = PlayButton(WIDTH/2, HEIGHT/2, "Jogar")

records_b = CircleButton(WIDTH/4-20, HEIGHT/2, "Recordes")
settings_b = CircleButton(WIDTH/2+WIDTH/4+20, HEIGHT/2, "Ajustes")

# BOTOES AJUSTES
mirror_b = CircleButton(WIDTH/4, HEIGHT/2, "Espelhar Labirinto", 12)
mirror_b.description = "Gera o labirinto\nsimetrico no eixo Y"

kruskal_b = CircleButton((WIDTH/4)*3-20, HEIGHT/2+8, "kruskal", 7)
kruskal_b.description = "Gera o labirinto a partir\nda MST do algoritmo de\nKruskal"
prim_b = CircleButton((WIDTH/4)*3+20, HEIGHT/2+8, "Prim", 7)
prim_b.description = "Gera o labirinto a partir\nda MST do algoritmo de\nPrim"

dij_b = CircleButton(WIDTH/4, HEIGHT/6, "Mostrar Dijkstra", 12)
dij_b.description = "Mostra a rota calculada\npelo fanstama Blinky usando\no algoritmo de Dijkstra"
bf_b =  CircleButton((WIDTH/4)*3, HEIGHT/6, "Mostrar Bellman-Ford", 12)
bf_b.description = "Mostra a rota calculada\npelo fanstama Bordy usando\no algoritmo de Bellman-Ford"

gx = 18
ghost1_b = PushButton(gx,  HEIGHT-28, "Ghost 1", 8)
ghost2_b = PushButton(gx+(30*1), HEIGHT-28, "Ghost 2", 8)
ghost3_b = PushButton(gx+(30*2), HEIGHT-28, "Ghost 3", 8)
ghost4_b = PushButton(gx+(30*3), HEIGHT-28, "Ghost 4", 8)

back_b = CircleButton(15, 15, "<", 5, textCenter=True)

# BOTOES GAME OVER
restart_b = PlayButton(WIDTH/2-60, HEIGHT/2, "Menu")
exit_b = ExitButton(WIDTH/2+60, HEIGHT/2, "Sair")