import utils

import pyxel

import globals
from globals import back_b
from states.gamestate import GameState

class RecordsState(GameState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        super().update()
        back_b.update()

        if back_b.is_on:
            back_b.is_on = False
            globals.next_state = "menu"

    def draw(self):
        super().draw()
        #|--|#|NOME|PONTOS|TEMPO|--|
        lst_records = []
        back_b.draw()
        
        pos_id = utils.WIDTH/2-100
        pos_name = utils.WIDTH/2-80
        pos_points = utils.WIDTH/2-10
        pos_time = utils.WIDTH/2+60
        
        # print((pyxel.frame_count%43 // 3)+1)
        pyxel.text(utils.align_text(utils.WIDTH/2, "RECORDS - TOP 10"), 10, "RECORDS - TOP 10", (pyxel.frame_count%40 // 3)+2)
        
        # pyxel.text(pos_id, 30, "", 7)
        pyxel.text(pos_name,   35, "NOME", 7)
        pyxel.text(pos_points, 35, "PONTOS", 7)
        pyxel.text(pos_time,   35, "TEMPO", 7)

        if len(lst_records) == 0:
            lst_records = utils.mergeSort(utils.get_records())
        K = 45
        for i in range(0, min(len(lst_records), 10)):
            time = int(lst_records[i][2])
            pyxel.text(pos_id,     K+(10*i), f"#{i+1}", 7)
            pyxel.text(pos_name,   K+(10*i), f"{lst_records[i][0]}", 7)
            pyxel.text(pos_points, K+(10*i), f"{lst_records[i][1]}", 7)
            pyxel.text(pos_time,   K+(10*i), f"{(time//60):02d}:{(time%60):02d}", 7)