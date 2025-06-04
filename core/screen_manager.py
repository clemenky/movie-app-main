class ScreenManager:
    def __init__(self):
        self._screens = {}
        self._non_stackable_screens = set()
        self.home_screen_key = 'home.main_menu_screen'
        self.current_screen_state = ('home', {})
        self._return_screen_state = None

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
    
    def get_current_screen_state(self):
        return self.current_screen_state
    
    @property
    def current_screen_key(self):
        return self.current_screen_state[0]
    
    @property
    def current_screen_params(self):
        return self.current_screen_state[1]

    def set_current_screen_state(self, screen_state):
        self.current_screen_state = screen_state
    
    def set_return_screen_state(self, params=None):
        self._return_screen_state = self.current_screen_state
    
    def return_to_return_state(self, params=None):
        self.set_current_screen_state(self._return_screen_state)
