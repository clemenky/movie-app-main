from globals import UI_ICONS, MOVIE_SEARCH_ICONS


menu_options = [
    {
        'type': 'static',
        'input': '1',
        'icon': MOVIE_SEARCH_ICONS['search_by_title'],
        'label': 'By Title',
        'action': ''
    },
    {
        'type': 'static',
        'input': '2',
        'icon': MOVIE_SEARCH_ICONS['search_by_tmdb_id'],
        'label': 'By TMDB ID',
        'action': '',
        'style': {
            'spacing_after': 1
        }
    },
    {
        'type': 'static',
        'input': 'b',
        'icon': UI_ICONS['back'],
        'label': 'Back',
        'action': 'back'
    }
]

input_options = [*menu_options]

screen = [
    {
        'component': 'title',
        'icon': UI_ICONS['movie_search'],
        'text': 'Movie Search',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'menu',
        'prompt': 'Select a search option:',
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
