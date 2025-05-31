from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_search as movie_search_screens
from config import MAX_SEARCH_RESULTS_PAGES


@app_context.screen_manager.register('movie_search.movie_search_screen', stackable=True)
def movie_search_screen(params):
    return handle_screen(movie_search_screens, 'movie_search_screen')

@app_context.screen_manager.register('movie_search.search_by_title_screen', stackable=False)
def search_by_title_screen(params):
    action, params = handle_screen(movie_search_screens, 'search_by_title_screen')
    params['search_type'] = 'title'
    return action, params

@app_context.screen_manager.register('movie_search.search_by_id_screen', stackable=False)
def search_by_id_screen(params):
    action, params = handle_screen(movie_search_screens, 'search_by_id_screen')
    params['search_type'] = 'id'
    return action, params

# REMOVE SEARCH TYPE AND MAKE SURE SEARCH BY ID DOESNT POINT HERE, SHOULD GO DIRECTLY TO DISPLAYING MOVIE NOT SEARCH RESULTS
@app_context.screen_manager.register('movie_search.search_results_screen', stackable=True)
def search_results_screen(params):
    print(params)
    search_query = params.get('query')
    page = params.get('page', 1)

    full_results = app_context.clients.movie_search_client.search_by_title(search_query, page)
    search_results = full_results['result']['results']
    total_pages = min(full_results['result'].get('total_pages', 1), MAX_SEARCH_RESULTS_PAGES)

    shared_options = []

    if page > 1:
        shared_options.append({
            'kind': 'static',
            'input': 'p',
            'label': 'Previous page',
            'action': ''
        })
    
    if page < total_pages:
        shared_options.append({
            'kind': 'static',
            'input': 'n',
            'label': 'Next page',
            'action': ''
        })

    dynamic_screen_components = {
        'search_results': [
            {
                'component': 'text',
                'text': f'Displaying search results for "{search_query}" ({page}/{total_pages})',
                'style': {
                    'spacing_after': 1
                }
            },
            {
                'component': 'text',
                'text': format_search_results(search_results),
                'style': {
                    'spacing_after': 1
                }
            }
        ],
        'dynamic_menu_options': [
            {
                'component': 'menu',
                'options': shared_options,
                'style': {
                    'option_format': 'square_brackets'
                }
            }
        ]
    }
    
    dynamic_input_options = {
        'dynamic_commands': [*shared_options]
    }

    

    return handle_screen(movie_search_screens, 'search_results_screen', dynamic_screen_components, dynamic_input_options)


def format_search_results(search_results):
    formatted_results = []
    for index, result in enumerate(search_results):
        release_date = result.get('release_date')
        release_year = release_date.split('-')[0] if release_date else 'Unknown'

        formatted_results.append(f'{index + 1}. {result['title']} ({release_year})')
    
    return '\n'.join(formatted_results)
