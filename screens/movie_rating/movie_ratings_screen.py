from globals import UI_ICONS


persistent_menu_options = [
    {
        'kind': 'display_only',
        'input': 'rate <n>',
        'label': 'Change rating of movie n',
        'target': ('', {})
    },
    {
        'kind': 'display_only',
        'input': 'del <n>',
        'label': 'Delete rating of movie n from ratings list',
        'target': ('', {})
    },
    {
        'kind': 'display_only',
        'input': 'recs <n>',
        'label': 'Get movie recommendations for movie n',
        'target': ('', {})
    },
    {
        'kind': 'static',
        'input': 'h',
        'label': 'Home',
        'target': ('home', {})
    },
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
        'icon': UI_ICONS['movie_ratings'],
        'text': 'Movie Ratings',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'dynamic_placeholder',
        'id': 'movie_ratings'
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
        'options': persistent_menu_options,
        'style': {
            'option_format': 'square_brackets',
            'spacing_after': 1
        }
    },
    {
        'component': 'divider',
        'char': '='
    },
]
