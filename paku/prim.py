from graph import Graph
from maze_utils import breakWalls, buildTree

import heapq

# Gera uma MST apartir do algoritmo de Prim

def prim_maze(g, start):
    """
    Gera uma MST, usada para desenhar o labirinto
    
    Params => g: Graph, start: String
    Return => path: Graph, edges: list
    """
    path = Graph()
    edges = []
    candidatas = []
    visited = []
    for u in g.node_dict[start].get_bros():
        heapq.heappush(candidatas,(g.node_dict[start].get_weight(u), (g.node_dict[start].get_id(), u.get_id())))
    visited.append(g.node_dict[start].get_id())
    
    while len(visited) < g.num_nodes:
        _ , (node_u,node_v) = heapq.heappop(candidatas)

        if node_v not in visited:
            visited.append(node_v)
            edges.append((node_u,node_v))
            current = node_v
            for bro in g.node_dict[current].get_bros():
                heapq.heappush(candidatas,(g.node_dict[current].get_weight(bro), (current, bro.get_id())))
                
    path = buildTree(edges)
    breakWalls(path, edges)

    return path, edges