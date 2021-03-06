import graph
import globals 

from ghosts import blinky, bordy, inky, pinky, clyde

from states.game_over import GameOverState
from states.maze import MazeState
from states.menu import MenuState
from states.records import RecordsState
from states.run import RunState
from states.settings import SettingsState
from states.start import StartState
from states.win import WinState

import pyxel
from math import dist
import os

WIDTH = globals.WIDTH
HEIGHT = globals.HEIGHT
GRID_WIDTH = 17
GRID_HEIGHT = 12

g = graph.Graph()
path = graph.Graph()
edges = []
delay = 220

def get_width():
    return WIDTH

def get_height():
    return HEIGHT

def change_state():
    """
    Muda os estados da aplicação
    """
    if globals.next_state != "":


        if globals.next_state == "game_over":
            globals.current_state = GameOverState()

        elif globals.next_state == "maze":
            globals.current_state = MazeState()

        elif globals.next_state == "menu":
            globals.current_state = MenuState()

        elif globals.next_state == "records":
            globals.current_state = RecordsState()

        elif globals.next_state == "run":
            globals.current_state = RunState()

        elif globals.next_state == "settings":
            globals.current_state = SettingsState()

        elif globals.next_state == "start":
            globals.current_state = StartState()

        elif globals.next_state == "win":
            globals.current_state = WinState()

        globals.next_state = ""

def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    """
        Verifica o clique no botão
    """
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True
    else:
        return False

def col_player_ghost(px, py, gx, gy):
    """
        Verifica Colisão Player-Ghost
    """
    if dist([px, py], [gx, gy]) < 11:
        return True
    else:
        return False

def inv_dir(dir):
    new_dir = ""
    if dir == "right": new_dir = "left"
    elif dir == "left": new_dir = "right"
    elif dir == "up": new_dir = "down"
    elif dir == "down": new_dir = "up"

    return new_dir

def align_in_grid(x):
    return x*15+7

def get_node_in_grid(x, y):
    """
        Recebe a posição na tela e retorna um String da posição no Grid
    """
    gx = x//15
    gy = y//15

    return g.get_node(coord_str(gx, gy))

def get_pos_in_grid(x, y):
    gx = x//15
    gy = y//15

    return (gx, gy)

def draw_grid():
    """
    Desenha o grid sobre o qual será montado o labirinto
    """
    for i in range(0, GRID_WIDTH+1):
        pyxel.line(15*i, 0, 15*i, GRID_HEIGHT*15, 5)

    for i in range(0, GRID_HEIGHT+1):
        pyxel.line(0, 15*i, GRID_WIDTH*15, 15*i, 5)
        
    for i in range(1, GRID_WIDTH):
        for j in range(1, GRID_HEIGHT):
            pyxel.pset(15*i, 15*j, 0)

def rect_custom(x1, y1, x2, y2, color):

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    pyxel.rect(x1, y1, x2-x1, y2-y1, color)

def coord_str(x, y):
    """
    Transformar a coordenada de int para String

    Params => x: int, y: int
    Return => "x-y": String
    """
    return (str(x) + "-" + str(y))

def coord_int(coord):
    st = coord.split("-")
    return [int(st[0]), int(st[1])]

def pick_ghost_info(id):

    name = ""
    description = ""

    if id == 0:
        name = "BLINKY"
        description = "Blinky persegue o jogador\nusando o algortimo de\nDijkstra"
    elif id == 1:
        name = "INKY"
        description = "Inky tenta se unir a outro\nfantasma para emboscar Paku"
    elif id == 2:
        name = "PINKY"
        description = "Pinky tenta estar sempre\num passo a frente de Paku\npara surpreende-lo"
    elif id == 3:
        name = "CLYDE"
        description = "Clyde nao sabe muito bem\npor onde ir"
    elif id == 4:
        name = "BORDY"
        description = "Bordy persegue o jogador\nusando o algortimo de\nBellman-Ford"

    return name, description

def pick_ghost(id, pos_id):
    """
        Retorna um Ghost a partir do id do fantasma escolhido

        Params => id: int, pos_id: int
        Return => Ghost
    """
    pos = []

    if pos_id == 0:
        pos = [0, 0]
    elif pos_id == 1:
        pos = [0, GRID_HEIGHT-1]
    elif pos_id == 2:
        pos = [GRID_WIDTH-1, 0]
    elif pos_id == 3:
        pos = [GRID_WIDTH-1, GRID_HEIGHT-1]

    if id == 0:
        return blinky.Blinky(pos[0], pos[1])
    elif id == 1:
        return inky.Inky(pos[0], pos[1])
    elif id == 2:
        return pinky.Pinky(pos[0], pos[1])
    elif id == 3:
        return clyde.Clyde(pos[0], pos[1])
    elif id == 4:
        return bordy.Bordy(pos[0], pos[1])

def get_close_node(node: graph.Node, direction):
    coords = coord_int(node.get_id())

    bro_node = node

    if(direction == "up"):
        if(coords[1] != 0):
            bro_node = g.get_node(coord_str(coords[0], coords[1]-1))

    elif(direction == "left"):
        if(coords[0] != 0):
            bro_node = g.get_node(coord_str(coords[0]-1, coords[1]))
            
    elif(direction == "down"):
        if(coords[1] != GRID_HEIGHT-1):
            bro_node = g.get_node(coord_str(coords[0], coords[1]+1))
            
    elif(direction == "right"):
        if(coords[0] != GRID_WIDTH-1):
            bro_node = g.get_node(coord_str(coords[0]+1, coords[1]))
    
    return bro_node.get_id()

def cave_paint(current, bro):
    """
        Apaga a fronteira entre dois nós no labirinto, formando um caminho
    """
    current_pos = coord_int(current)
    bro_pos = coord_int(bro)

    x1 = current_pos[0]*15+1
    y1 = current_pos[1]*15+1
    x2 = bro_pos[0]*15+1
    y2 = bro_pos[1]*15+1
    
    if x1 < x2 or y1 < y2:
        x2 += 14
        y2 += 14
    elif x1 > x2 or y1 > y2:
        x1 += 14
        y1 += 14

    rect_custom(x1, y1, x2, y2, 0)

def mirror():
    """
    Espelha o labirinto gerado pelo Prim ou Kruskal

    Return => new_path: Graph
    """
    new_path = graph.Graph()

    for i in range(0, GRID_WIDTH):
        for j in range(0, GRID_HEIGHT):
            new_path.add_node(coord_str(i, j))

    for i in range(GRID_WIDTH//2+1, GRID_WIDTH):
        for j in range(0, GRID_HEIGHT):
            if (coord_str(i, j), coord_str(i+1, j)) in edges: edges.remove((coord_str(i, j), coord_str(i+1, j)))
            if (coord_str(i, j), coord_str(i-1, j)) in edges: edges.remove((coord_str(i, j), coord_str(i-1, j)))
            if (coord_str(i, j), coord_str(i, j+1)) in edges: edges.remove((coord_str(i, j), coord_str(i, j+1)))
            if (coord_str(i, j), coord_str(i, j-1)) in edges: edges.remove((coord_str(i, j), coord_str(i, j-1)))

    for i in range(GRID_WIDTH//2, GRID_WIDTH):
        for j in range(0, GRID_HEIGHT):
            mirror = GRID_WIDTH-1-i

            if (coord_str(mirror, j), coord_str(mirror, j+1)) in edges:
                edges.append((coord_str(i, j), coord_str(i, j+1)))
            if (coord_str(mirror, j), coord_str(mirror, j-1)) in edges:
                edges.append((coord_str(i, j), coord_str(i, j-1)))

            if (coord_str(mirror, j), coord_str(mirror+1, j)) in edges:
                edges.append((coord_str(i, j), coord_str(i-1, j)))
            if (coord_str(mirror, j), coord_str(mirror-1, j)) in edges:
                edges.append((coord_str(i, j), coord_str(i+1, j)))

    edges.append( ( coord_str(GRID_WIDTH//2, 0) , coord_str(GRID_WIDTH//2+1, 0) ) )
    edges.append( ( coord_str(GRID_WIDTH//2, 0) , coord_str(GRID_WIDTH//2-1, 0) ) )

    edges.append( ( coord_str(GRID_WIDTH//2, GRID_HEIGHT-1), coord_str(GRID_WIDTH//2+1, GRID_HEIGHT-1) ) )
    edges.append( ( coord_str(GRID_WIDTH//2, GRID_HEIGHT-1), coord_str(GRID_WIDTH//2-1, GRID_HEIGHT-1) ) )

    for j in range(0, GRID_HEIGHT):
        posx = GRID_WIDTH//2

        if j!= GRID_HEIGHT-1:
            if (coord_str(posx, j), coord_str(posx, j+1)) not in edges: 
                edges.append((coord_str(posx, j), coord_str(posx, j+1)))
            if (coord_str(posx, j+1), coord_str(posx, j)) not in edges: 
                edges.append((coord_str(posx, j+1), coord_str(posx, j)))

        if j!= 0:
            if (coord_str(posx, j), coord_str(posx, j-1)) not in edges: 
                edges.append((coord_str(posx, j), coord_str(posx, j-1)))
            if (coord_str(posx, j-1), coord_str(posx, j)) not in edges: 
                edges.append((coord_str(posx, j-1), coord_str(posx, j)))

    for edge in edges:
        new_path.add_edge(edge[0], edge[1], 1)

    return new_path


def register_record(name, points, time):
    """
        Salva o score em um arquivo
    """
    file_name = ".paku_records.txt"
    file = open(file_name, "a")

    file.write(f"{name} {points} {time}\n")
    file.close()

def get_records():
    """
        Pega os scores salvos em um arquivo

        Return => records: list
    """
    records = []
    file_name = ".paku_records.txt"

    if os.path.exists(file_name):
        file = open(file_name, "r")
        lines = file.readlines()

        for line in lines:
            name, points, time = line.strip().split(" ")
            records.append([name, int(points), int(time)])

        file.close()

    return records

# MERGE SORT Adaptado com desempate
def mergeSort(lst):
    """
        Ordena as pontuações da maior para menor, com desempate pelo menor tempo

        Params => lst: list
        Return => lst: list
    """
    if len(lst) > 1:
        mid = len(lst)//2
  
        left = lst[:mid]
        right = lst[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0 
        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                    lst[k] = left[i]
                    i += 1
            elif left[i][1] == right[j][1]:
                    if  left[i][2] <= right[j][2]:
                        lst[k] = left[i]
                        i += 1
                    else:
                        lst[k] = right[j]
                        j += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
  
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
            
    return lst