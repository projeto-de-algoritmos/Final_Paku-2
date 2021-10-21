from ghost import Ghost
import utils
import heapq

class Blinky(Ghost):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.color = 8
        self.base_color = 8
        self.facing = "right"
        self.gost_path = []

    
    def update(self, player_node, _):
        super().update()

        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
            self.calc_target(player_node)
        else:
            self.canTurn = False

        if self.canTurn:
            if self.gost_path != []:

                dir = self.facing
                
                next_node = utils.coord_int(self.gost_path[-1])
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
                    # print(f"Blinky: {self.state}")
                    # print(dir)
                    # print(self.directions())
                    # print("")

                    if dir in self.directions():
                        self.turn(dir)
                    else:
                        self.turn(self.random_move())

                elif self.state == "frightened":
                    dir = utils.inv_dir(dir)
                    # print(f"Blinky: {self.state}")
                    # print(dir)
                    # print(self.directions())
                    # print("")
                    
                    if dir in self.directions():
                        # print("random")
                        self.turn(dir)
                    else:
                        # print("random")
                        self.turn(self.random_move())
            else:
                self.turn(self.random_move())


        if self.state != "eaten":
            self.move()

    def calc_target(self, player_node):

        visited = [] # Nós visitados
        end = player_node.get_id()
        current = self.atNode.get_id()
        pq  = []
        nodeData = {}
        for x in utils.path.get_nodes():
            nodeData[x] = {'weight': float('inf'), 'parent': []}
        
        nodeData[current]['weight'] = 0
        while len(visited)+1 < utils.path.num_nodes:
            # print(len(visited)+1)
            # print(utils.path.num_nodes)
            if current not in visited:
                visited.append(current)
                node_dij = utils.path.get_node(current)
                for neighbour in node_dij.get_bros():
                    neighbour = neighbour.get_id()

                    if neighbour not in visited:
                        weight = nodeData[current]['weight'] + 1
                        if weight < nodeData[neighbour]['weight']:
                            nodeData[neighbour]['weight'] = weight
                            nodeData[neighbour]['parent'] = current

                        heapq.heappush(pq, (nodeData[neighbour]['weight'], neighbour))
                heapq.heapify(pq)

            if pq == []: break
            _, current = heapq.heappop(pq)
            
        x = end
        self.gost_path = []
        while x != self.atNode.get_id():
            self.gost_path.append(x)
            x = nodeData[x]['parent']

    def reset(self, x, y):
        super().reset(x, y)
        self.color = 8
        self.base_color = 8
        self.facing = "right"
        self.gost_path = []