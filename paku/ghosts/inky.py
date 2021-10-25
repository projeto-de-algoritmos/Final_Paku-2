from ghosts.ghost import Ghost
import utils

class Inky(Ghost):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.color = 6
        self.base_color = 6
        self.facing = "left"
        self.blinky_pos = [0, 0]

    def update(self, _, __):
        super().update()

        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
            choice = self.calc_target()
        else:
            self.canTurn = False
        
        if self.canTurn:
            if self.state == "chase":
                self.turn(choice)

            elif self.state == "frightened":
                choice = utils.inv_dir(choice)

                if choice in self.directions():
                    self.turn(choice)
                else:
                    self.turn(self.random_move())
                
        if self.state != "eaten":
            self.move()

    def calc_target(self):

        target = [utils.GRID_WIDTH-1-self.blinky_pos[0], utils.GRID_HEIGHT-1-self.blinky_pos[1]]
        ghost_pos = utils.coord_int(self.atNode.get_id())

        valid_dir = self.directions()
        min = float('inf')
        for dir in valid_dir:
            if dir == "up":
                ghost_pos[1] -= 1    
            elif dir == "right":
                ghost_pos[0] += 1
            elif dir == "down":
                ghost_pos[1] += 1
            elif dir == "left":
                ghost_pos[0] -= 1
                
            dist = (target[0] - ghost_pos[0])**2 + (target[1] - ghost_pos[1])**2
            if min > dist:
                min = dist
                go_to = dir

        return go_to

    def reset(self, x, y):
        super().reset(x, y)
        self.color = 11
        self.base_color = 11
        self.facing = "left"
        self.blinky_pos = [0, 0]
