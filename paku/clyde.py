from ghost import Ghost
import utils

class Clyde(Ghost):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.color = 9
        self.base_color = 9
        self.facing = "left"

    def update(self, player_node, _):
        super().update()
        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
        else:
            self.canTurn = False

        if self.canTurn: 
            self.turn(self.random_move())

       
        if self.state != "eaten":
            self.move()
    def reset(self, x, y):
        super().reset(x, y)
        self.color = 9
        self.base_color = 9
        self.facing = "left"
