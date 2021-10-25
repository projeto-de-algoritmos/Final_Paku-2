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
ghosts_id = [0, 1, 2, 3]

pellets_list = pellets.Pellets()

# BOTOES MENU
start_b = PlayButton(WIDTH/2, HEIGHT/2, "Jogar")

records_b = CircleButton(WIDTH/4-20, HEIGHT/2, "Recordes")
settings_b = CircleButton(WIDTH/2+WIDTH/4+20, HEIGHT/2, "Ajustes")

# BOTOES AJUSTES
mirror_b = CircleButton(WIDTH/4-20, HEIGHT/4, "Espelhar Labirinto")
dij_b = CircleButton(WIDTH/2+WIDTH/4+20, HEIGHT/4, "Mostrar Dijkstra")
bf_b = CircleButton(WIDTH/2, HEIGHT/4+20, "Mostrar Bellman-Ford")
kruskal_b = CircleButton(WIDTH/4-20, HEIGHT/2+10, "kruskal")
prim_b = CircleButton(WIDTH/2+WIDTH/4+20, HEIGHT/2+10, "Prim")

ghost1_b = PushButton(80,  HEIGHT-30, "Ghost 1", 10)
ghost2_b = PushButton(110, HEIGHT-30, "Ghost 2", 10)
ghost3_b = PushButton(140, HEIGHT-30, "Ghost 3", 10)
ghost4_b = PushButton(170, HEIGHT-30, "Ghost 4", 10)

back_b = CircleButton(15, 15, "<", 5, textCenter=True)

# BOTOES GAME OVER
restart_b = PlayButton(WIDTH/2-60, HEIGHT/2, "Menu")
exit_b = ExitButton(WIDTH/2+60, HEIGHT/2, "Sair")