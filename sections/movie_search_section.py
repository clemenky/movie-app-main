from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_search as movie_search_screens


@app_context.screen_manager.register('movie_search.movie_search_screen', stackable=True)
def movie_search_screen(**kwargs):
    return handle_screen(movie_search_screens, 'movie_search_screen')


@app_context.screen_manager.register('movie_search.search_by_title_screen', stackable=True)
def search_by_title_screen(**kwargs):
    return handle_screen(movie_search_screens, 'search_by_title_screen')


@app_context.screen_manager.register('movie_search.search_by_id_screen', stackable=True)
def search_by_id_screen(**kwargs):
    return handle_screen(movie_search_screens, 'search_by_id_screen')
