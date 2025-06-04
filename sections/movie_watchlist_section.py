import math

from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_watchlist as movie_watchlist_screens


@app_context.screen_manager.register('movie_watchlist.display_watchlist_screen', stackable=True)
def display_watchlist_screen(context):
    page = context.get('page', 1)

    watchlist_client = app_context.clients.movie_watchlist_client
    watchlist = watchlist_client.list_movies()['result']

    total_pages = math.ceil(len(watchlist) / 20)

    start_index = (page - 1) * 20
    end_index = start_index + 20
    watchlist_page_items = watchlist[start_index:end_index]

    delete_movie_input_options = []
    for index, movie_data in enumerate(watchlist_page_items):
        input_option = {
            'kind': 'static',
            'input': f'del {index + 1}',
            'actions': [(watchlist_client.delete_movie, {'movie_id': movie_data['movie_id']})],
            'target': ('movie_watchlist.display_watchlist_screen', {})
        }
        delete_movie_input_options.append(input_option)
    
    ratings = app_context.clients.movie_rating_client.list_ratings()['result']
    rate_movie_input_options = []
    for index, movie_data in enumerate(watchlist_page_items):
        movie_id = movie_data['movie_id']
        is_rated = any(rating['movie_id'] == movie_id for rating in ratings)

        if not is_rated:
            input_option = {
                'kind': 'static',
                'input': f'rate {index + 1}',
                'actions': [(app_context.screen_manager.set_return_screen_state, {})],
                'target': ('movie_rating.rate_movie_screen', {
                    'movie_id': movie_id, 
                    'movie_details': movie_data['movie_details']
                })
            }
            rate_movie_input_options.append(input_option)

    dynamic_screen_components = {
        'movie_watchlist': [{
            'component': 'text',
            'text': format_watchlist_page(watchlist_page_items)
        }]
    }

    dynamic_input_options = {
        'dynamic_commands': [*delete_movie_input_options, *rate_movie_input_options]
    }

    return handle_screen(
        movie_watchlist_screens,
        'display_watchlist_screen',
        dynamic_screen_components,
        dynamic_input_options
    )

def format_watchlist_page(watchlist_page_items):
    ratings = app_context.clients.movie_rating_client.list_ratings()['result']
    watchlist_lines = []
    for index, item in enumerate(watchlist_page_items):
        movie_details = item.get('movie_details', {})
        title = movie_details.get('title')
        release_year = movie_details.get('release_year')

        movie_id = item['movie_id']
        is_rated = any(rating['movie_id'] == movie_id for rating in ratings)
        if is_rated:
            rating = next((rating['rating'] for rating in ratings if rating['movie_id'] == movie_id), None)
            rating = f' - {rating}/10'
        else:
            rating = ''

        watchlist_lines.append(f'{index + 1}. {title} ({release_year}){rating}')

    return '\n'.join(watchlist_lines)