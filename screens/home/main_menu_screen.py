from globals import UI_ICONS


input_config = {
    'mode': 'selection',
    'options': [
        {
            'kind': 'static',
            'input': '1',
            'icon': UI_ICONS['movie_search'],
            'label': 'Movie Search',
            'description': 'Search for specific movies',
            'target': ('movie_search.movie_search_screen', {})
        },
        {
            'kind': 'static',
            'input': '2',
            'icon': UI_ICONS['movie_discovery'],
            'label': 'Movie Discovery',
            'description': 'Browse trending and recommended movies',
            'target': ('movie_discovery.movie_discovery_screen', {})
        },
        {
            'kind': 'static',
            'input': '3',
            'icon': UI_ICONS['movie_watchlist'],
            'label': 'Movie Watchlist',
            'description': 'View and manage your watchlist',
            'target': ('movie_watchlist.display_watchlist_screen', {})
        },
        {
            'kind': 'static',
            'input': '4',
            'label': 'Movie Ratings',
            'icon': UI_ICONS['movie_ratings'],
            'description': 'Track your favorite movies',
            'target': ('movie_rating.movie_ratings_screen', {})
        },
        # {
        #     'kind': 'static',
        #     'input': '8',
        #     'icon': UI_ICONS['login'],
        #     'label': 'Login',
        #     'description': 'Required for movie watchlist and ratings',
        #     'target': ('', {})
        # },
        # {
        #     'kind': 'static',
        #     'input': '9',
        #     'icon': UI_ICONS['title_screen'],
        #     'label': 'Title Screen',
        #     'target': ('', {})
        # },
        {
            'kind': 'static',
            'input': '0',
            'icon': UI_ICONS['exit'],
            'label': 'Exit',
            'target': ('exit', {})
        }
    ]
}

screen_components = [
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
        'options': input_config['options'],
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
