from client_manager import ClientManager
from components import home
from components import movie_info
from components import movie_watchlist


class MovieApp:
    def __init__(self):
        self.clients = ClientManager()
        self.home = home.MainMenu(self.clients)
        self.movie_info = movie_info.MovieInfo(self.clients)
        self.movie_watchlist = movie_watchlist.MovieWatchlist(self.clients)
        self.current_screen_key = 'home'
        self.current_params = {}

        self.screens = {
            'home': self.home.main_menu_screen,
            'movie_info.movie_search_screen': self.movie_info.movie_search_screen,
            'movie_info.search_by_title_screen': self.movie_info.search_by_title_screen,
            'movie_info.search_by_title_results_screen': self.movie_info.search_by_title_results_screen,
            'movie_info.search_by_id_screen': self.movie_info.search_by_id_screen,
            'movie_info.show_movie_info_screen': self.movie_info.show_movie_info_screen,            
            None: None
        }

        self.navigation_stack = []
        self.non_stackable_screens = ['movie_info.search_by_title_screen', 'movie_info.search_by_id_screen']
    
    def navigate_to(self, screen_key, params=None):
        if params is None:
            params = {}
        if self.current_screen_key not in self.non_stackable_screens and self.current_screen_key != 'home' and screen_key != 'back':
            self.navigation_stack.append((self.current_screen_key, self.current_params))
        self.current_screen_key = screen_key
        self.current_params = params

    def go_back(self):
        if self.navigation_stack:
            prev_screen_key, prev_params = self.navigation_stack.pop()
            self.current_screen_key = prev_screen_key
            self.current_params = prev_params
        else:
            self.current_screen_key = 'home'
            self.current_params = {}

    def run(self):
        while self.current_screen_key:
            screen_key = self.current_screen_key
            params = self.current_params

            if screen_key == 'back':
                self.go_back()
                continue

            next_action = self.screens[screen_key](**params)

            if next_action:
                next_screen_key, next_params = next_action
                self.navigate_to(next_screen_key, next_params)
            elif self.current_screen_key != 'home':
                pass
            elif self.current_screen_key == 'home' and next_action is None:
                break

        self.clients.close_all()

if __name__ == '__main__':
    app = MovieApp()
    app.run()
