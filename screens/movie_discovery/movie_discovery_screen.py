from globals import UI_ICONS, MOVIE_DISCOVERY_ICONS


input_config = {
    'mode': 'selection',
    'options': [
        {
            'kind': 'static',
            'input': '1',
            'label': 'Trending Movies',
            'icon': MOVIE_DISCOVERY_ICONS['trending_movies'],
            'target': ('movie_discovery.trending_movies_filter_screen', {})
        },
        {
            'kind': 'static',
            'input': '2',
            'label': 'Movie Recommendations',
            'icon': MOVIE_DISCOVERY_ICONS['movie_recommendations'],
            'target': ('', {}),
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
        'icon': UI_ICONS['movie_discovery'],
        'text': 'Movie Discovery',
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
