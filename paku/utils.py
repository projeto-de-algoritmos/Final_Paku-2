import graph

import pyxel
import math

WIDTH = 256
HEIGHT = 196
GRID_WIDTH = 17
GRID_HEIGHT = 12

g = graph.Graph()
path = graph.Graph()
edges = []
delay = 220


def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    """
        Verifica o clique no botão
    """
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True

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
    '''
        Recebe a posição na tela e retorna um String da posição no Grid
    '''
    gx = x//15
    gy = y//15

    return g.get_node(coord_str(gx, gy))

def get_pos_in_grid(x, y):
    gx = x//15
    gy = y//15

    return (gx, gy)

def draw_grid():
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
    return (str(x) + "-" + str(y))

def coord_int(coord):
    st = coord.split("-")
    return [int(st[0]), int(st[1])]

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
    # print(current)
    # print(bro)
    current_pos = coord_int(current)
    bro_pos = coord_int(bro)

    # print(current_pos)
    # print(bro_pos)

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
        # dead_end = 0

        # if (coord_str(posx, j), coord_str(posx+1, j)) not in edges and (coord_str(posx+1, j), coord_str(posx, j)) not in edges: dead_end +=1
        # if (coord_str(posx, j), coord_str(posx-1, j)) not in edges and (coord_str(posx-1, j), coord_str(posx, j)) not in edges: dead_end +=1
        # if (coord_str(posx, j), coord_str(posx, j+1)) not in edges and (coord_str(posx, j+1), coord_str(posx, j)) not in edges: dead_end +=1
        # if (coord_str(posx, j), coord_str(posx, j-1)) not in edges and (coord_str(posx, j-1), coord_str(posx, j)) not in edges: dead_end +=1

        # if dead_end >= 3:
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
    file = open("paku/paku_records.txt", "a")

    file.write(f"{name} {points} {time}\n")
    file.close()

def get_records():
    records = []
    file = open("paku/paku_records.txt", "r")
    
    lines = file.readlines()

    for line in lines:
        name, points, time = line.strip().split(" ")
        records.append([name, points, time])

    file.close()

    return records

# MERGE SORT Adaptado com desempate
def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
  
        i = j = k = 0
        left = lst[:mid]
        right = lst[mid:]
        mergeSort(left)
        mergeSort(right)
  
        while i < len(left) and j < len(right):
            if left[i][1] >= right[j][1]:
                if left[i][1] == right[j][1]:
                    if  left[i][2] < right[j][2]:
                        lst[k] = left[i]
                        i += 1
                    else:
                        lst[k] = right[j]
                        j += 1
                else:
                    lst[k] = left[i]
                    i += 1
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

# DEBUG

# DESCOBRE QUANTAS CELULAS POSSO TER
# for i in range(1, 21):
#     print("pixels por celula: ")
#     print((256-i-1)/i)
#     print("celulas: ")
#     print(i)
#     print()