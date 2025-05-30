import shutil

from core.client_manager import ClientManager
from core.screen_manager import ScreenManager
from core.screen_components_manager import ScreenComponentsManager

class AppContext:
    def __init__(self):
        self.clients = ClientManager()
        self.screen_manager = ScreenManager()
        self.screen_components = ScreenComponentsManager()

        self.console_width = shutil.get_terminal_size().lines
        self.console_height = shutil.get_terminal_size().columns
    