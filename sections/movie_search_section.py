from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_search as movie_search_screens


@app_context.screen_manager.register('movie_search.movie_search_screen', stackable=True)
def movie_search_screen(**kwargs):
    return handle_screen(movie_search_screens, 'movie_search_screen')

@app_context.screen_manager.register('movie_search.search_by_title_screen', stackable=False)
def search_by_title_screen(**kwargs):
    action, params = handle_screen(movie_search_screens, 'search_by_title_screen')
    params['search_type'] = 'title'
    return action, params

@app_context.screen_manager.register('movie_search.search_by_id_screen', stackable=False)
def search_by_id_screen(**kwargs):
    action, params = handle_screen(movie_search_screens, 'search_by_id_screen')
    params['search_type'] = 'id'
    return action, params

@app_context.screen_manager.register('movie_search.search_results_screen', stackable=True)
def search_results_screen(**kwargs):
    params = kwargs[0]
    search_type = params.get('search_type')
    page = params.get('page', 1)
    return handle_screen(movie_search_screens, 'search_results_screen')
