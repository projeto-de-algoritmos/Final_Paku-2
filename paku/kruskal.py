from graph import Graph
from maze_utils import breakWalls, buildTree

# Gera uma MST apartir do algoritmo de Kruscal

def find(parent, item):
    if parent[item] == item:
        return item
    return find(parent, parent[item])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_maze(graph, edges):
    """
    Gera uma MST, que será usada para desenhar o labirinto
    
    Params => graph: Graph, edges: list
    Return => path: Graph, edges: list
    """
    path = Graph()
    i, e = 0, 0
    parent = {}
    lst_edges = []

    for node in graph:
        parent[node.get_id()] = node.get_id()
        for bro in node.get_bros():
            lst_edges.append([node.get_id(), bro.get_id(), node.get_weight(bro)])
    
    rank = dict.fromkeys(graph.node_dict, 0)
    lst_edges = sorted(lst_edges, key=lambda item: item[2])
    while e < graph.num_nodes - 1:
        s, d, _ = lst_edges[i]
        i += 1
        x = find(parent, s)
        y = find(parent, d)
        if x != y:
            e += 1
            edges.append((s,d))
            union(parent, rank, x,y)
    
    path = buildTree(edges)
    breakWalls(path, edges)

    return path, edges
