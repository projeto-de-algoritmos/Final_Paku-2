import utils
from graph import Graph

import random

# Funções utilizadas em ambos os algoritmos de construção de labirinto

def buildTree(edges):
    """
        Constrói uma arvore a partir de uma lista de edges
        
        Params => edges: list 
        Return => path: Graph
    """
    tree = Graph()
    for i in range(0, utils.GRID_WIDTH):
        for j in range(0, utils.GRID_HEIGHT):
            tree.add_node(utils.coord_str(i, j))

    for edge in edges:
        tree.add_edge(edge[0], edge[1], 1)
    return tree


def breakWalls(path: Graph, edges):
    """
        Quebra paredes do labirinto

        Params => path: Graph
        Return => edges: list 
    """
    for i in range(0, utils.GRID_WIDTH):
        for j in range(0, utils.GRID_HEIGHT):
            node = path.node_dict[utils.coord_str(i, j)]


            if len(node.get_bros()) == 1:
                side = [1, 2, 3, 4]
                coords = utils.coord_int(node.get_id())

                for bro in node.get_bros():
                    bro_coords = utils.coord_int(bro.get_id())

                if coords[0] > bro_coords[0]: # bro a esquerda
                    side.remove(3)
                elif coords[0] < bro_coords[0]: # bro a direita
                    side.remove(1)
                elif coords[1] > bro_coords[1]: # bro acima
                    side.remove(4)
                elif coords[1] < bro_coords[1]: # bro abaixo
                    side.remove(2)

                if(coords[0] == 0):
                    side.remove(3)
                if(coords[1] == 0):
                    side.remove(4)
                if(coords[0] == utils.GRID_WIDTH-1):
                    side.remove(1)
                if(coords[1] == utils.GRID_HEIGHT-1):
                    side.remove(2)

                s = random.choice(side)
                side.remove(s)

                if s == 1: # DIREITA
                    next_node = path.get_node(utils.coord_str(coords[0]+1, coords[1]))
                elif s == 2: # BAIXO
                    next_node = path.get_node(utils.coord_str(coords[0], coords[1]+1))
                elif s == 3: # ESQUERDA
                    next_node = path.get_node(utils.coord_str(coords[0]-1, coords[1]))
                elif s == 4: # CIMA
                    next_node = path.get_node(utils.coord_str(coords[0], coords[1]-1))

                path.add_edge(node.get_id(), next_node.get_id(), 0)
                edges.append((node.get_id(), next_node.get_id()))