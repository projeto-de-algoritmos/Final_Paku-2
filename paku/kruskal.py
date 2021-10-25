from graph import Graph
import utils

# def buildTree(tree, edges):
#     for i in range(0, utils.GRID_WIDTH):
#         for j in range(0, utils.GRID_HEIGHT):
#             tree.add_node(utils.coord_str(i, j))

#     for edge in edges:
#         tree.add_edge(edge[0], edge[1], 1)

def find(parent, i):
		if parent[i] == i:
			return i
		return find(parent, parent[i])

# A function that does union of two sets of x and y
# (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# The main function to construct MST using Kruskal's
    # algorithm
def KruskalMST(graph):

    result = [] # This will store the resultant MST
    
    # An index variable, used for sorted edges
    i = 0
    edges = []
    # An index variable, used for result[]
    e = 0
    for node in graph:
        for bro in node.get_bros():
            edges.append([node.get_id(), bro.get_id(), node.get_weight(bro)])
    # Step 1: Sort all the edges in
    # non-decreasing order of their
    # weight. If we are not allowed to change the
    # given graph, we can create a copy of graph
    edges = sorted(edges,
                        key=lambda item: item[2])
    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(graph.num_nodes):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < graph.num_nodes - 1:

        # Step 2: Pick the smallest edge and increment
        # the index for next iteration
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does't
        # cause cycle, include it in result
        # and increment the indexof result
        # for next edge
        if x != y:
            e = e + 1
            result.append([u, v, w])
            
            union(parent, rank, x, y)
        # Else discard the edge
    minimumCost = 0
    for u, v, weight in result:
        minimumCost += weight
    print(minimumCost)
    print(result)
    print(parent)

    # for edge in result:
    #     ans_g = graph.Graph()
    #     ans_e = []
    #     ans_g.add_edge(edge[0], edge[1], edge[2])
    #     ans_e.append((edge[0], edge[1]))


g = Graph()
# g.add_edge(0,1,4)
# g.add_edge(0,7,8)
# g.add_edge(1,7,11)
# g.add_edge(1,2,8)
# g.add_edge(7,8,7)
# g.add_edge(7,6,1)
# g.add_edge(2,8,2)
# g.add_edge(2,3,7)
# g.add_edge(2,5,4)
# g.add_edge(6,8,6)
# g.add_edge(6,5,2)
# g.add_edge(5,3,14)
# g.add_edge(5,4,10)
# g.add_edge(3,4, 9)

g.add_edge("0-0","0-1", 4)
g.add_edge("0-0","3-4", 8)
g.add_edge("0-1","3-4", 11)
g.add_edge("0-1","1-1", 8)
g.add_edge("3-4","4-4", 7)
g.add_edge("3-4","3-3", 1)
g.add_edge("1-1","4-4", 2)
g.add_edge("1-1","1-2", 7)
g.add_edge("1-1","2-3", 4)
g.add_edge("3-3","4-4", 6)
g.add_edge("3-3","2-3", 2)
g.add_edge("2-3","1-2", 14)
g.add_edge("2-3","2-2", 10)
g.add_edge("1-2","2-2", 9)

ed = KruskalMST(g)

print(ed)