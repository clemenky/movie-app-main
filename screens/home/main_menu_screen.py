from globals import UI_ICONS


menu_options = [
    {
        'type': 'static',
        'input': '1',
        'icon': UI_ICONS['movie_search'],
        'label': 'Movie Search',
        'description': 'Search for specific movies',
        'action': 'movie_search.movie_search_screen'
    },
    {
        'type': 'static',
        'input': '2',
        'icon': UI_ICONS['movie_discovery'],
        'label': 'Movie Discovery',
        'description': 'Browse trending and recommended movies',
        'action': ''
    },
    {
        'type': 'static',
        'input': '3',
        'icon': UI_ICONS['movie_watchlist'],
        'label': 'Movie Watchlist',
        'description': 'View and manage your watchlist',
        'action': ''
    },
    {
        'type': 'static',
        'input': '4',
        'label': 'Movie Ratings',
        'icon': UI_ICONS['movie_ratings'],
        'description': 'Track your favorite movies',
        'action': ''
    },
    {
        'type': 'static',
        'input': '8',
        'icon': UI_ICONS['login'],
        'label': 'Login',
        'description': 'Required for movie watchlist and ratings',
        'action': ''
    },
    {
        'type': 'static',
        'input': '9',
        'icon': UI_ICONS['title_screen'],
        'label': 'Title Screen',
        'action': ''
    },
    {
        'type': 'static',
        'input': '0',
        'icon': UI_ICONS['exit'],
        'label': 'Exit',
        'action': 'exit'
    }
]

input_options = [*menu_options]

screen = [
    {
        'component': 'title',
        'icon': UI_ICONS['home'],
        'text': 'Home',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'menu',
        'prompt': 'Select an option by number:',
        'options': menu_options,
        'style': {
            'icons': True,
            'option_format': 'square_brackets',
            'spacing_after': 1
        }
    },
    {
        'component': 'divider',
        'char': '='
    }
]
