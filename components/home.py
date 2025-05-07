import input_utils


class MainMenu:
    def __init__(self, clients):
        self.clients = clients
    
    def main_menu_screen(self):
        params = {
            'prompt': 'Choose a service:',
            'options': [
                {
                    'input': '1',
                    'text': 'Movie Info           – Find and explore detailed information about any movie.',
                    'function': 'movie_info.movie_search_screen'
                },
                # {
                #     'input': '2',
                #     'text': 'Trending Movies    – Browse trending movies from now or a specific time period.',
                #     'function': trending_movies
                # },
                # {
                #     'input': '3',
                #     'text': 'Movie Watchlist    – Keep track of movies you want to watch.',
                #     'function': movie_watchlist
                # },
                # {
                #     'input': '4',
                #     'text': 'Movie Ratings      – Rate movies you’ve watched and view your ratings.',
                #     'function': movie_ratings
                # },
                {
                    'input': '0',
                    'text': 'Exit',
                    'function': None
                }
            ]
        }
        return input_utils.handle_input(params)