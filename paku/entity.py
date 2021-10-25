import utils

class Entity:
    def __init__(self) -> None:
        self.posX = 0
        self.posY = 0
        self.atNode = None
        self.canTurn = True
        self.facing = None
        
    def move(self):

        go = True
        if self.canTurn == True:
            close_node = utils.get_close_node(self.atNode, self.facing)
            if (self.atNode.get_id(), close_node) not in utils.edges and (close_node, self.atNode.get_id()) not in utils.edges:
                go = False

        if go:
            if self.facing == "down":
                self.posY += 1
            if self.facing == "right":
                self.posX += 1
            if self.facing == "up":
                self.posY -= 1
            if self.facing == "left":
                self.posX -= 1
            
    def directions(self):
        dir_list = ["up", "down", "right", "left"]
        valids_dir = []
        dir_list.remove(utils.inv_dir(self.facing))

        for dir in dir_list:
            close_node = utils.get_close_node(self.atNode, dir)

            if (self.atNode.get_id(), close_node) in utils.edges or (close_node, self.atNode.get_id()) in utils.edges:
                valids_dir.append(dir)

        return valids_dir

    def turn(self, direction):
        if self.canTurn == True:
            close_node = utils.get_close_node(self.atNode, direction)
            if (self.atNode.get_id(), close_node) in utils.edges or (close_node, self.atNode.get_id()) in utils.edges :
                self.facing = direction