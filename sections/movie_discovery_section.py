from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_discovery as movie_discovery_screens
from config import MAX_SEARCH_RESULTS_PAGES


@app_context.screen_manager.register('movie_discovery.movie_discovery_screen', stackable=True)
def movie_discovery_screen(context):
    return handle_screen(movie_discovery_screens, 'movie_discovery_screen')

@app_context.screen_manager.register('movie_discovery.trending_movies_filter_screen', stackable=True)
def trending_movies_filter_screen(context):
    return handle_screen(movie_discovery_screens, 'trending_movies_filter_screen')

@app_context.screen_manager.register('movie_discovery.trending_movies_screen', stackable=True)
def search_results_screen(context):
    page = context.get('page', 1)

    raw_response = app_context.clients.movie_discovery_client.get_trending_movies()
    movie_results = raw_response['data']['results']
    total_pages = min(raw_response['data'].get('total_pages', 1), MAX_SEARCH_RESULTS_PAGES)

    movie_input_options = []
    for index, movie_data in enumerate(movie_results):
        input_option = {
            'kind': 'static',
            'input': f'{index + 1}',
            'target': ('movie_search.movie_details_screen', {'movie_id': movie_data['id']})
        }
        movie_input_options.append(input_option)

    shared_options = []

    if page > 1:
        shared_options.append({
            'kind': 'static',
            'input': 'p',
            'label': 'Previous page',
            'target': 'movie_discovery.trending_movies_screen'
        })
    
    if page < total_pages:
        shared_options.append({
            'kind': 'static',
            'input': 'n',
            'label': 'Next page',
            'target': 'movie_discovery.trending_movies_screen'
        })

    dynamic_screen_components = {
        'trending_movies': [
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

    return handle_screen(
        movie_discovery_screens,
        'trending_movies_screen',
        dynamic_screen_components,
        dynamic_input_options
    )


# if not reused, combine input option generating loop for movie numbers with this
def format_search_results(search_results):
    formatted_results = []
    for index, result in enumerate(search_results):
        release_date = result.get('release_date')
        release_year = release_date.split('-')[0] if release_date else 'Unknown'

        formatted_results.append(f'{index + 1}. {result['title']} ({release_year})')
    
    return '\n'.join(formatted_results)


@app_context.screen_manager.register('movie_discovery.movie_recommendations_screen', stackable=True)
def movie_recommendations_screen(context):
    page = context.get('page', 1)
    raw_response = app_context.clients.movie_discovery_client.get_recommendations(context['movie_id'])
    movie_results = raw_response['data']['results']
    total_pages = min(raw_response['data'].get('total_pages', 1), MAX_SEARCH_RESULTS_PAGES)

    movie_input_options = []
    for index, movie_data in enumerate(movie_results):
        input_option = {
            'kind': 'static',
            'input': f'{index + 1}',
            'target': ('movie_search.movie_details_screen', {'movie_id': movie_data['id']})
        }
        movie_input_options.append(input_option)

    shared_options = []

    if page > 1:
        shared_options.append({
            'kind': 'static',
            'input': 'p',
            'label': 'Previous page',
            'target': 'movie_discovery.trending_movies_screen'
        })
    
    if page < total_pages:
        shared_options.append({
            'kind': 'static',
            'input': 'n',
            'label': 'Next page',
            'target': 'movie_discovery.trending_movies_screen'
        })

    dynamic_screen_components = {
        'recommended_movies': [
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

    return handle_screen(
        movie_discovery_screens,
        'movie_recommendations_screen',
        dynamic_screen_components,
        dynamic_input_options
    )