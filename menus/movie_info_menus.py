movie_search_menu_params = {
    'title': '🔍 Movie Search',
    'prompt': 'Enter how you want to search:',
    'options': [
        {
            'input': '1',
            'text': 'Search by title',
            'function': 'movie_info.search_by_title'
        },
        {
            'input': '2',
            'text': 'Search by TMDB ID',
            'function': 'movie_info.search_by_id'
        },
        {
            'input': 'b',
            'text': 'Back',
            'function': 'home.service_selection'
        }
    ]
}

search_by_title_menu_params = {
    'prompt': 'Enter movie title:',
    'text_input': {
        'validate': lambda x: x != '',
        'function': lambda x: movie_info.process_search_by_title(x)
    }
}