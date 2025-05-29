from globals import UI_ICONS


menu_options = [
    {
        'type': 'static',
        'key': '1',
        'icon': UI_ICONS['movie_search'],
        'label': 'Movie Search',
        'description': 'Search for specific movies',
        'action': 'movie_search.movie_search_screen'
    },
    {
        'type': 'static',
        'key': '2',
        'icon': UI_ICONS['movie_discovery'],
        'label': 'Movie Discovery',
        'description': 'Browse trending and recommended movies',
        'action': ''
    },
    {
        'type': 'static',
        'key': '3',
        'icon': UI_ICONS['movie_watchlist'],
        'label': 'Movie Watchlist',
        'description': 'View and manage your watchlist',
        'action': ''
    },
    {
        'type': 'static',
        'key': '4',
        'label': 'Movie Ratings',
        'icon': UI_ICONS['movie_ratings'],
        'description': 'Track your favorite movies',
        'action': ''
    },
    {
        'type': 'static',
        'key': '8',
        'icon': UI_ICONS['login'],
        'label': 'Login',
        'description': 'Required for movie watchlist and ratings',
        'action': ''
    },
    {
        'type': 'static',
        'key': '9',
        'icon': UI_ICONS['title_screen'],
        'label': 'Title Screen',
        'action': ''
    },
    {
        'type': 'static',
        'key': '0',
        'icon': UI_ICONS['exit'],
        'label': 'Exit',
        'action': 'exit'
    }
]

screen = [
    {
        'component': 'title',
        'content': {
            'icon': UI_ICONS['home'],
            'text': 'Home'
        },
        'icon': True
    },
    {
        'component': 'menu',
        'prompt': 'Select an option by number:',
        'options': menu_options,
        'icons': True
    }
]
