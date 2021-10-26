import utils
import pyxel

# Classe responsável por administrar as pellets (bolinhas)
class Pellets:
    def __init__(self) -> None:
        self.pellets_dict = {}

    def fill_dict(self):
        
        for i in range(0, utils.GRID_WIDTH):
            for j in range(0, utils.GRID_HEIGHT):
                if i == 0 and j == 0:
                    self.pellets_dict.update({(i, j): 2})
                elif i == 0 and j == utils.GRID_HEIGHT-1:
                    self.pellets_dict.update({(i, j): 2})
                elif i == utils.GRID_WIDTH-1 and j == 0:
                    self.pellets_dict.update({(i, j): 2})
                elif i == utils.GRID_WIDTH-1 and j == utils.GRID_HEIGHT-1:
                    self.pellets_dict.update({(i, j): 2})
                elif i != 8 or j != 6:
                    self.pellets_dict.update({(i, j): 1})
        
    def draw(self):
        for x in self.pellets_dict.items():
            if x[1] == 1:
                pyxel.pset(utils.align_in_grid(x[0][0]), utils.align_in_grid(x[0][1]), 9)
            else:
                pyxel.circ(utils.align_in_grid(x[0][0]), utils.align_in_grid(x[0][1]), 2, 9)
    
    def reset(self):
        self.pellets_dict.clear()
