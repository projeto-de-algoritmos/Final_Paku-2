import utils

import pyxel

import globals
from globals import start_b, records_b, settings_b
from states.gamestate import GameState

class MenuState(GameState):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        super().update()
        start_b.update()
        records_b.update()
        settings_b.update()

        if records_b.is_on:
            records_b.is_on = False
            globals.next_state = "records"

        if settings_b.is_on:
            settings_b.is_on = False
            globals.next_state = "settings"

        if start_b.is_on:
            start_b.is_on = False
            globals.next_state = "start"

    def draw(self):
        super().draw()
        title = 'PAKU PAKU 2'
        pyxel.text(utils.align_text(utils.WIDTH/2, title),40, title, 7)
        start_b.draw()
        settings_b.draw()
        records_b.draw()