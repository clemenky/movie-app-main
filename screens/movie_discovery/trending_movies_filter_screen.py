from globals import MOVIE_DISCOVERY_ICONS


input_config = {
    'mode': 'selection',
    'options': [
        {
            'kind': 'static',
            'input': '1',
            'label': 'Genre',
            'target': ('', {})
        },
        {
            'kind': 'static',
            'input': '2',
            'label': 'Time Period',
            'target': ('', {})
        },
        {
            'kind': 'static',
            'input': '3',
            'label': 'Genre + Time Period',
            'target': ('', {})
        },
        {
            'kind': 'static',
            'input': '4',
            'label': 'All Trending Movies',
            'target': ('movie_discovery.trending_movies_screen', {}),
            'style': {
                'spacing_after': 1
            }
        },
        {
            'kind': 'static',
            'input': 'b',
            'label': 'Back',
            'target': ('back', {})
        },
        {
            'kind': 'static',
            'input': 'h',
            'label': 'Home',
            'target': ('home', {})
        }
    ]
}

screen_components = [
    {
        'component': 'title',
        'icon': MOVIE_DISCOVERY_ICONS['trending_movies'],
        'text': 'Trending Movies Filter',
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
            'option_format': 'square_brackets',
            'spacing_after': 1
        }
    },
    {
        'component': 'divider',
        'char': '='
    }
]
