from globals import UI_ICONS, MOVIE_SEARCH_ICONS


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
        'component': 'text',
        'text': 'Select an option:'
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
    },
    {
        'component': 'divider',
        'char': '='
    }
]
