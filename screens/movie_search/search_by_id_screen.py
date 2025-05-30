from globals import MOVIE_SEARCH_ICONS


input_config = {
    'mode': 'text',
    'options': [
        {
            'param': 'query',
            'validate': lambda x: x.strip() != '',
            'action': 'movie_search.search_results_screen'
        }
    ]
}

screen = [
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
