import os

import sections
from core.global_context import app_context


screen_manager = app_context.screen_manager

class MovieApp:
    def __init__(self):

        self.next_screen_key = 'home'
        self.next_screen_params = {}

        self.navigation_stack = []
        self.navigation_stack.append((self.next_screen_key, self.next_screen_params))
        self.running = True

    def run(self):
        while self.running:
            if self.next_screen_key == 'home':
                self._navigate_home()
            elif self.next_screen_key == 'back':
                self._navigate_back()
            elif self.next_screen_key == 'exit':
                self._exit()
            else:
                self._navigate_to_next_screen()

    def _navigate_to_next_screen(self):
        screen_key = self.next_screen_key
        screen_params = self.next_screen_params

        screen_function = screen_manager.get_screen_function(screen_key)
        
        if screen_manager.is_stackable(screen_key):
            self.navigation_stack.append((screen_key, screen_params))

        self._clear_screen()
        self.next_screen_key, self.next_screen_params = screen_function(screen_params)

    def _navigate_home(self):
        home_key = screen_manager.home_screen_key
        self.navigation_stack = [(home_key, self.next_screen_params)]
        self.next_screen_key, self.next_screen_params = screen_manager.get_screen_function(home_key)()
    
    def _navigate_back(self):
        self.navigation_stack.pop()
        self.next_screen_key, self.next_screen_params = self.navigation_stack[-1]

    def _exit(self):
        app_context.clients.close_all()
        self.running = False

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    app = MovieApp()
    app.run()
