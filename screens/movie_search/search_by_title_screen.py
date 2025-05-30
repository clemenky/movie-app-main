from globals import MOVIE_SEARCH_ICONS


text_input_option = {
    'type': 'text',
    'validate': lambda x: x != '',
    'action': 'movie_search.search_results_screen'
}

input_options = [*text_input_option]

screen = [
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
        'content': 'Enter movie title:'
    }
]
