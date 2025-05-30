from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.home as home_screens


@app_context.screen_manager.register('home.main_menu_screen', stackable=True)
def main_menu_screen(**kwargs):
    return handle_screen(home_screens, 'main_menu_screen')
