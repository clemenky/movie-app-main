from globals import UI_ICONS


persistent_menu_options = [
    {
        'kind': 'display_only',
        'input': 'rate <n>',
        'label': 'Add rating for item n',
        'target': ('movie_watchlist.display_watchlist_screen', {})
    },
    {
        'kind': 'display_only',
        'input': 'del <n>',
        'label': 'Delete item n from watchlist',
        'target': ('movie_watchlist.display_watchlist_screen', {})
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
        'icon': UI_ICONS['movie_watchlist'],
        'text': 'Movie Watchlist',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'dynamic_placeholder',
        'id': 'movie_watchlist'
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
