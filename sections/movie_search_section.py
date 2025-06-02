from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_search as movie_search_screens
from config import MAX_SEARCH_RESULTS_PAGES


@app_context.screen_manager.register('movie_search.movie_search_screen', stackable=True)
def movie_search_screen(context):
    return handle_screen(movie_search_screens, 'movie_search_screen')

@app_context.screen_manager.register('movie_search.search_by_title_screen', stackable=False)
def search_by_title_screen(context):
    return handle_screen(movie_search_screens, 'search_by_title_screen')

@app_context.screen_manager.register('movie_search.search_by_id_screen', stackable=False)
def search_by_id_screen(context):
    return handle_screen(movie_search_screens, 'search_by_id_screen')

# REMOVE SEARCH TYPE AND MAKE SURE SEARCH BY ID DOESNT POINT HERE, SHOULD GO DIRECTLY TO DISPLAYING MOVIE NOT SEARCH RESULTS
@app_context.screen_manager.register('movie_search.search_results_screen', stackable=True)
def search_results_screen(context):
    print(context)
    search_query = context.get('search_query')
    page = context.get('page', 1)

    search_response = app_context.clients.movie_search_client.search_by_title(search_query, page)
    movie_results = search_response['result']['results']
    total_pages = min(search_response['result'].get('total_pages', 1), MAX_SEARCH_RESULTS_PAGES)

    movie_input_options = []
    for index, result in enumerate(movie_results):
        input_option = {
            'kind': 'static',
            'input': f'{index + 1}',
            'target': ('movie_search.movie_details_screen', {'movie_id': result['id']})
        }
        movie_input_options.append(input_option)

    shared_options = []

    if page > 1:
        shared_options.append({
            'kind': 'static',
            'input': 'p',
            'label': 'Previous page',
            'target': 'movie_search.search_results_screen'
        })
    
    if page < total_pages:
        shared_options.append({
            'kind': 'static',
            'input': 'n',
            'label': 'Next page',
            'target': 'movie_search.search_results_screen'
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
                'text': format_search_results(movie_results),
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
        'dynamic_commands': [*shared_options, *movie_input_options]
    }

    

    return handle_screen(movie_search_screens, 'search_results_screen', dynamic_screen_components, dynamic_input_options)


# if not reused, combine input option generating for movie numbers with this
def format_search_results(search_results):
    formatted_results = []
    for index, result in enumerate(search_results):
        release_date = result.get('release_date')
        release_year = release_date.split('-')[0] if release_date else 'Unknown'

        formatted_results.append(f'{index + 1}. {result['title']} ({release_year})')
    
    return '\n'.join(formatted_results)



@app_context.screen_manager.register('movie_search.movie_details_screen', stackable=True)
def movie_details_screen(context):
    movie_id = context.get('movie_id')
    movie_details_response = app_context.clients.movie_search_client.get_movie_details(movie_id)
    movie_details = movie_details_response['result']
    get_movie_details_str(movie_details)
    return handle_screen(movie_search_screens, 'movie_details_screen')



def get_movie_details_str(movie_details):
    details_str = ''
