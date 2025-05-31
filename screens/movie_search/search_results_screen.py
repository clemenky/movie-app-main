from globals import MOVIE_SEARCH_ICONS


persistent_menu_options = [
    {
        'kind': 'static',
        'input': 'b',
        'label': 'Back',
        'action': 'back'
    },
    {
        'kind': 'static',
        'input': 'h',
        'label': 'Home',
        'action': 'home'
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
        'icon': MOVIE_SEARCH_ICONS['search_results'],
        'text': 'Search Results',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'dynamic_placeholder',
        'id': 'search_results'
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