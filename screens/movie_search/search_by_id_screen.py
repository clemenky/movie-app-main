from globals import MOVIE_SEARCH_ICONS


input_config = {
    'mode': 'text',
    'options': [
        {
            'kind': 'text',
            'validate': lambda x: x.strip() != '',
            'target': ('movie_search.movie_details_screen', {}),
            'target_param': 'movie_id'
        }
    ]
}

screen_components = [
    {
        'component': 'title',
        'icon': MOVIE_SEARCH_ICONS['search_by_id'],
        'text': 'Search by TMDB ID',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'text',
        'text': 'Enter TMDB ID:'
    }
]
