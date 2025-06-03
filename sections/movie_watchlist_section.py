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

    dynamic_screen_components = {
        'movie_watchlist': [{
            'component': 'text',
            'text': format_watchlist_page(watchlist_page_items),
        }]
    }

    return handle_screen(movie_watchlist_screens, 'display_watchlist_screen', dynamic_screen_components)

def format_watchlist_page(watchlist_page_items):
    print(watchlist_page_items)
    watchlist_lines = []
    for index, item in enumerate(watchlist_page_items):
        movie_details = item.get('movie_details', {})
        title = movie_details.get('title')
        release_year = movie_details.get('release_year')

        watchlist_lines.append(f'{index + 1}. {title} ({release_year})')

    return '\n'.join(watchlist_lines)