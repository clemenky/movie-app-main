import ui.screen_renderer as screen_renderer
import core.input_handler as input_handler

import screens.home as home_screens
from core.global_context import app_context


@app_context.screen_manager.register('home.main_menu_screen', stackable=True)
def main_menu_screen(**kwargs):
    screen_data = home_screens.main_menu_screen.screen
    screen_renderer.render_screen(screen_data)
    #action = input_handler.get_next_action(screen_data)
    action = ('home', {})
    action = None
    return action
