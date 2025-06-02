from globals import UI_ICONS, MOVIE_SEARCH_ICONS


input_config = {
    'mode': 'selection',
    'options': [
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
        'component': 'dynamic_placeholder',
        'id': 'movie_details'
    },
    {
        'component': 'divider',
        'char': '=',
        'style': {
            'spacing_before': 1,
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
