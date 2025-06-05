from globals import MOVIE_DISCOVERY_ICONS


persistent_menu_options = [
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


input_config = {
    'mode': 'selection',
    'options': [
        {
            'kind': 'dynamic_placeholder',
            'id': 'dynamic_commands'
        },
        *persistent_menu_options
    ]
}

screen_components = [
    {
        'component': 'title',
        'icon': MOVIE_DISCOVERY_ICONS['movie_recommendations'],
        'text': 'Recommended Movies',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'dynamic_placeholder',
        'id': 'recommended_movies'
    },
    {
        'component': 'divider',
        'char': '=',
        'style': {
            'spacing_after': 1
        }
    },
    {
        'component': 'text',
        'text': 'Enter an option:',
        'style': {
            'spacing_after': 1
        }
    },
    {
        'component': 'dynamic_placeholder',
        'id': 'dynamic_menu_options'
    },
    {
        'component': 'menu',
        'options': persistent_menu_options,
        'style': {
            'option_format': 'square_brackets',
            'spacing_after': 1
        }
    }
]