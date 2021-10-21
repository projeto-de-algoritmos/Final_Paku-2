from ghosts.ghost import Ghost
import utils

class Pinky(Ghost):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.color = 14
        self.base_color = 14
        self.facing = "left"

    def update(self, player_node, player_facing):
        super().update()

        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
            choice = self.calc_target(player_node, player_facing)
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

    def calc_target(self, player_node, player_facing):

        target = utils.coord_int(player_node.get_id())
        ghost_pos = utils.coord_int(self.atNode.get_id())
        
        offset = 2
        if player_facing == "up":
            target[1] -= offset
        elif player_facing == "right":
            target[0] += offset
        elif player_facing == "down":
            target[1] += offset
        elif player_facing == "left":
            target[0] -= offset

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
            # print(f"dir: {dir} - dist: {dist}")
            if min > dist:
                min = dist
                go_to = dir

        # self.turn(dir)                
        return go_to

    def reset(self, x, y):
        super().reset(x, y)
        self.color = 14
        self.base_color = 14
        self.facing = "left"
        