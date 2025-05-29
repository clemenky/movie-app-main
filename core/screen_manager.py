class ScreenManager:
    def __init__(self):
        self._screens = {}
        self._non_stackable_screens = set()
        self.home_screen_key = 'home.main_menu_screen'

    def register(self, screen_key, stackable=True):
        def decorator(screen_function):
            self._screens[screen_key] = screen_function
            if not stackable:
                self._non_stackable_screens.add(screen_key)
            return screen_function
        return decorator
    
    def get_screen_function(self, screen_key):
        return self._screens.get(screen_key)

    def get_all_screens(self):
        return self._screens.copy()

    def is_stackable(self, screen_key):
        return screen_key not in self._non_stackable_screens
    
    def is_home_screen(self, screen_key):
        return screen_key == self.home_screen_key
