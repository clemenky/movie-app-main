from globals import MOVIE_SEARCH_ICONS


input_config = {
    'mode': 'text',
    'options': [
        {
            'kind': 'text',
            'validate': lambda x: x.strip() != '',
            'target': ('movie_search.search_results_screen', {}),
            'target_param': 'search_query'
        }
    ]
}

screen_components = [
    {
        'component': 'title',
        'icon': MOVIE_SEARCH_ICONS['search_by_title'],
        'text': 'Search by Title',
        'style': {
            'icon': True,
            'spacing_after': 1
        }
    },
    {
        'component': 'text',
        'text': 'Enter movie title:'
    }
]
