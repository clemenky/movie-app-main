from globals import UI_ICONS


input_config = {
    'mode': 'text',
    'options': [
        {
            'kind': 'text',
            'validate': lambda x: x.strip() != '',
            'target': ('return', {}),
            'target_param': 'rating'
        }
    ]
}

screen_components = [
    {
        'component': 'title',
        'icon': UI_ICONS['movie_ratings'],
        'text': 'Rate Movie',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'text',
        'text': 'Rate movie (1-10):'
    }
]
