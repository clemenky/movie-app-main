import os

import sections
from core.global_context import app_context


screen_manager = app_context.screen_manager

class MovieApp:
    def __init__(self):
        self.navigation_stack = []
        self.navigation_stack.append((screen_manager.current_screen_key, screen_manager.current_screen_params))
        self.running = True

    def run(self):
        while self.running:
            screen_key = screen_manager.current_screen_key
            if screen_key == 'home':
                self._navigate_home()
            elif screen_key == 'back':
                self._navigate_back()
            elif screen_key == 'return':
                self._return_to_return_state()
            elif screen_key == 'exit':
                self._exit()
            self._navigate_to_next_screen()

    def _navigate_to_next_screen(self):
        screen_key, screen_params = screen_manager.get_current_screen_state()
        screen_function = screen_manager.get_screen_function(screen_key)
        
        if screen_manager.is_stackable(screen_key):
            if self.navigation_stack and self.navigation_stack[-1][0] == screen_key:
                # If the stack is not empty and the top screen is the same, replace it
                self.navigation_stack[-1] = (screen_key, screen_params)
            else:
                self.navigation_stack.append((screen_key, screen_params))

        self._clear_screen()
        #print(screen_params)
        next_screen_state = screen_function(screen_params)
        screen_manager.set_current_screen_state(next_screen_state)

    def _navigate_home(self):
        screen_manager.set_current_screen_state((screen_manager.home_screen_key, {}))
        self.navigation_stack = [screen_manager.get_current_screen_state()]
    
    def _navigate_back(self):
        self.navigation_stack.pop()
        screen_manager.set_current_screen_state(self.navigation_stack[-1])

    def _return_to_return_state(self):
        screen_manager.return_to_return_state()

    def _exit(self):
        app_context.clients.close_all()
        self.running = False

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    app = MovieApp()
    app.run()
