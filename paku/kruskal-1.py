from graph import Graph
import utils
import random

# Ordenar arestas
# Incluir arestas de menor peso na Min S Tree
# Se ambos os nos que formam a aresta fazem parte do mesmo subgrupo isso gera um ciclo e nao eh permitido

g = Graph()
# g.add_edge("0-0","0-1", 4)
# g.add_edge("0-0","3-4", 8)
# g.add_edge("0-1","3-4", 11)
# g.add_edge("0-1","1-1", 8)
# g.add_edge("3-4","4-4", 7)
# g.add_edge("3-4","3-3", 1)
# g.add_edge("1-1","4-4", 2)
# g.add_edge("1-1","1-2", 7)
# g.add_edge("1-1","2-3", 4)
# g.add_edge("3-3","4-4", 6)
# g.add_edge("3-3","2-3", 2)
# g.add_edge("2-3","1-2", 14)
# g.add_edge("2-3","2-2", 10)
# g.add_edge("1-2","2-2", 9)
for i in range(0, utils.GRID_WIDTH):
    for j in range(0, utils.GRID_HEIGHT):
        if(i != 0):
            g.add_edge(utils.coord_str(i, j), utils.coord_str(i-1, j), random.randint(1, 20))
        if(j != 0):
            g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j-1), random.randint(1, 20))
        if(i != utils.GRID_WIDTH-1):
            g.add_edge(utils.coord_str(i, j), utils.coord_str(i+1, j), random.randint(1, 20))
        if(j != utils.GRID_HEIGHT-1):
            g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j+1), random.randint(1, 20))

edges = []
for node in g:
    for bro in node.get_bros():
        edges.append([node.get_id(), bro.get_id(), node.get_weight(bro)])
edges = sorted(edges, key=lambda item: item[2])

print(edges)

def kruskal(sorted_edges):
    ans_edges = []
    lists = []
    create_lst = True

    weight = 0

    count = 0 

    # for edge in sorted_edges:
    #     print(edge)
    for edge in sorted_edges:
        create_lst = True
        a, b, w = edge[0], edge[1], edge[2]

        for lst in lists:

            if a in lst and b not in lst:
                for lst2 in lists:
                    count +=1
                    if b in lst2:
                        lists.append(lst + lst2)
                        lists.remove(lst)
                        lists.remove(lst2)
                        break
                if b not in lst: lst.append(b)
                create_lst = False
                ans_edges.append((a, b))
                weight += w 
                break

            elif b in lst and a not in lst:
                for lst2 in lists:
                    count +=1
                    if a in lst2:
                        lists.append(lst + lst2)
                        lists.remove(lst)
                        lists.remove(lst2)
                        break
                if a not in lst: lst.append(a)
                create_lst = False
                ans_edges.append((a, b))
                weight += w
                break

            elif a in lst and b in lst:
                create_lst = False
                break

        if create_lst:
            lists.append([a, b])
            ans_edges.append((a, b))
            weight += w 

    print("RESPOSTA:")
    print(ans_edges)
    print("PESO:")
    print(weight)
    print("COUNT")
    print(count)
        
kruskal(edges)