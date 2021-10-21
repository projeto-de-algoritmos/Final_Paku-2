class Node:
    def __init__(self, node):
        self.id = node
        self.bros = {}

    def __str__(self):
        return str(self.id) + str([x.id for x in self.bros])

    # Adiciona vizinho a lista de adjacência
    def add_bro(self, bro, weight=0):
        self.bros[bro] = weight
    
    # Retorna lista de vizinhos
    def get_bros(self):
        return self.bros.keys()  

    # Retorna ID do nó
    def get_id(self):
        return self.id

    # Retorna PESO da aresta do nó com o vizinho
    def get_weight(self, neighbor):
        return self.bros[neighbor]

class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.node_dict.values())

    # Adciona nó ao grafo
    def add_node(self, node):
        self.num_nodes = self.num_nodes + 1
        new_node = Node(node)
        self.node_dict[node] = new_node
        return new_node

    # Retorna nó se ele estiver no grafo
    def get_node(self, n):
        if n in self.node_dict:
            return self.node_dict[n]
        else:
            return None

    # Adiciona aresta entre 2 nós
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.node_dict:
            self.add_node(frm)
        if to not in self.node_dict:
            self.add_node(to)

        self.node_dict[frm].add_bro(self.node_dict[to], cost)
        self.node_dict[to].add_bro(self.node_dict[frm], cost)

    # Retorna dicionário com nós
    def get_nodes(self):
        return self.node_dict.keys()

    def reset(self):
        self.node_dict.clear()
        self.num_nodes = 0