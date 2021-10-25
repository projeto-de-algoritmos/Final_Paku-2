from ghosts.ghost import Ghost
import utils

import random

# Bellman Ford Ghost
class Bordy(Ghost):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.color = 2
        self.base_color = 2
        self.facing = "right"
        self.ghost_path = []

    
    def update(self, player_node, _):
        super().update()

        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
            self.calc_target_bellman(player_node)
        else:
            self.canTurn = False

        if self.canTurn:
            if self.ghost_path != []:

                dir = self.facing

                next_node = utils.coord_int(self.ghost_path[0])
                ghost_node = utils.coord_int(self.atNode.get_id())
                if ghost_node[0] > next_node[0]:
                        dir = "left"
                elif ghost_node[0] < next_node[0]:
                        dir = "right"
                elif ghost_node[1] > next_node[1]:
                        dir = "up"
                elif ghost_node[1] < next_node[1]:
                        dir = "down"
            
                if self.state == "chase":


                    if dir in self.directions():
                        self.turn(dir)
                    else:
                        self.turn(self.random_move())

                elif self.state == "frightened":
                    dir = utils.inv_dir(dir)

                    
                    if dir in self.directions():
                        self.turn(dir)
                    else:
                        self.turn(self.random_move())
            else:
                self.turn(self.random_move())


        if self.state != "eaten":
            self.move()

    # Bellman Ford
    def calc_target_bellman (self, player_node):
        dist = {}
        edges = []

        g = utils.path

        for node in g:
            dist.update({node.get_id(): float("Inf")})
            for bro in node.get_bros():
                edges.append([node.get_id(), bro.get_id(), random.randint(1,10)])

        dist.update({player_node.get_id(): 0})

        path = {}
        for _ in range(g.num_nodes - 1):
            for u, v, w in edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    path.update({v:u})
    
        self.ghost_path = []
        current = self.atNode.get_id()

        while current != player_node.get_id():
            self.ghost_path.append(path[current])
            current = path[current]

        print("GHOST PATH")
        print(self.ghost_path)

    def reset(self, x, y):
        super().reset(x, y)
        self.color = 2
        self.base_color = 2
        self.facing = "right"
        self.ghost_path = []