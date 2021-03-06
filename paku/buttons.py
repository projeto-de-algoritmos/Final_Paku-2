from math import dist
import pyxel

# Evitando import circular:
# from utils import align_text, col_mouse_bt
 
def align_text(x, str):
    """
        Função que alinha o texto dos botões

        Params: x: int, str: String
        Return: x: int
    """
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    """
        Verifica o clique no botão
    """
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True
    else:
        return False

# Fim da seção usada para evitar import circular


# Classe Button abstrata, pai de todos os outros buttons
class Button:

    def __init__(self, x, y, text):
        self.posx = x
        self.posy = y
        self.text = text
        self.offset = 4
        self.is_on = False
        self.color = 0
        self.subcolor = 0
        self.textCenter = False
        self.description = ""

    def update(self):
        """Atualiza o estado do botão"""
        ...

    def draw(self):
        """Desenha o botão na tela"""
        ...
        
class CircleButton(Button):
    def __init__(self, x, y, text, r=15, textCenter=False):
        super().__init__(x, y, text, )
        self.color = 10
        self.subcolor = 9
        self.radius = r
        self.textCenter = textCenter
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2

            pyxel.playm(3, loop=False)
        else:
            if self.is_on:
                self.offset = 2
            else:
                self.offset = 4


    def draw(self):
        pyxel.circ(self.posx, self.posy, self.radius, self.subcolor)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, self.color)

        if self.is_on: txt_color = 8
        else: txt_color = 7
        if self.textCenter:
            pyxel.text(align_text(self.posx, self.text), self.posy-self.offset-2, self.text, txt_color)
        else:
            pyxel.text(align_text(self.posx, self.text), self.posy+self.radius+3, self.text, txt_color)

class RectButton(Button):
    def __init__(self, x, y, text, w, h):
        super().__init__(x, y, text)
        self.width = w
        self.height = h
        self.color = 12
        self.subcolor = 5
        
    def update(self):

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2
        else:
            if self.is_on:
                self.offset = 2
            else:
                self.offset = 4
        

    def draw(self):
        pyxel.rect(self.posx-(self.width/2)-self.offset, self.posy-(self.height/2)-self.offset, self.width+self.offset, self.height+self.offset, self.subcolor)
        pyxel.rect(self.posx-(self.width/2)-self.offset, self.posy-(self.height/2)-self.offset, self.width, self.height, self.color)

        if self.is_on: txt_color = 8
        else: txt_color = 7

        pyxel.text(align_text(self.posx, self.text)-self.offset, self.posy-self.offset-2, self.text, txt_color)

# Botão de ativação única, (ou seja, não é do tipo 'toggle')
class PushButton(Button):
    def __init__(self, x, y, text, r, textCenter=False):
        super().__init__(x, y, text)
        self.color = 12
        self.subcolor = 5
        self.radius = r
        self.offset = 2
        self.textCenter = textCenter
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 2
            pyxel.playm(3, loop=False)
            return True
        else:
            self.offset = 2

    def draw(self):
        pyxel.circ(self.posx, self.posy, self.radius, self.subcolor)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, self.color)
        
        if self.textCenter:
            pyxel.text(align_text(self.posx, self.text), self.posy-self.offset-2, self.text, 7)
        else:
            pyxel.text(align_text(self.posx, self.text), self.posy+self.radius+3, self.text, 7)

# Botão Circular estilizado para o combinar com o Paku
class PlayButton(CircleButton):
    def __init__(self, x, y, text, ):
        super().__init__(x, y, text)
        self.radius = 30

    def draw(self):
        pyxel.circ(self.posx,  self.posy, self.radius, 9) # Sombra
        pyxel.circ(self.posx,  self.posy-self.offset, self.radius, 10)
        pyxel.circ(self.posx,  self.posy-15-self.offset, 3, 0)
        pyxel.pset(self.posx, self.posy, 10)

        tmp_color = 9
        if self.offset == 0: tmp_color = 0

        pos1 = [-1, -3]
        pos2 = [3, 2]
        pos3 = [25, -21]
        pos4 = [22, 10]

        # Parte escura abaixo da boca
        pyxel.tri( self.posx+pos1[0], self.posy+4-self.offset+pos1[1], self.posx+pos2[0], self.posy+4-self.offset+pos2[1], self.posx+pos3[0], self.posy+4-self.offset+pos3[1], tmp_color)
        pyxel.tri( self.posx+pos4[0], self.posy+4-self.offset+pos4[1], self.posx+pos2[0], self.posy+4-self.offset+pos2[1], self.posx+pos3[0], self.posy+4-self.offset+pos3[1], tmp_color)
        
        # Abertura da boca
        pyxel.tri(self.posx, self.posy+4-self.offset, self.posx+30, self.posy-20+4-self.offset, self.posx+30, self.posy+20+4-self.offset, 0)

        # Pequenas correções
        pyxel.pset(self.posx+pos1[0], self.posy+4-self.offset+pos1[1], 10)
        pyxel.pset(self.posx+pos1[0]+1, self.posy+4-self.offset+pos1[1]+2, tmp_color)

        # Correções das pontas da boca
        pyxel.rect(self.posx+23, self.posy+15, 10, 10, 0)
        pyxel.rect(self.posx+24, self.posy-24, 10, 18, 0)

        pyxel.text(align_text(self.posx, self.text), self.posy+40, self.text, 7)

# Outro botão Circular estilizado para o combinar com o Paku
class ExitButton(CircleButton):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)
        self.radius = 30

    def draw(self):
        pyxel.circ(self.posx,  self.posy, self.radius, 9) # Sombra
        pyxel.circ(self.posx,  self.posy-self.offset, self.radius, 10)
        pyxel.circ(self.posx-10,  self.posy-15-self.offset, 3, 0)
        pyxel.circ(self.posx+10,  self.posy-15-self.offset, 3, 0)
        # Boca opcional:
        # pyxel.line(self.posx-10, self.posy+10-self.offset, self.posx+10, self.posy+10-self.offset, 0)
        pyxel.text(align_text(self.posx, self.text), self.posy+40, self.text, 7)
