from globals import UI_ICONS, MOVIE_SEARCH_ICONS


input_config = {
    'mode': 'selection',
    'options': [
        {
            'kind': 'static',
            'input': '1',
            'icon': MOVIE_SEARCH_ICONS['search_by_title'],
            'label': 'By Title',
            'target': ('movie_search.search_by_title_screen', {})
        },
        {
            'kind': 'static',
            'input': '2',
            'icon': MOVIE_SEARCH_ICONS['search_by_id'],
            'label': 'By TMDB ID',
            'target': ('movie_search.search_by_id_screen', {}),
            'style': {
                'spacing_after': 1
            }
        },
        {
            'kind': 'static',
            'input': 'b',
            'icon': UI_ICONS['back'],
            'label': 'Back',
            'target': ('back', {})
        }
    ]
}

screen_components = [
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
