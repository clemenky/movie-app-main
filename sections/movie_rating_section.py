from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_rating as movie_rating_screens


@app_context.screen_manager.register('movie_rating.movie_ratings_screen', stackable=True)
def movie_ratings_screen(context):
    rating_client = app_context.clients.movie_rating_client
    ratings = rating_client.list_ratings()['result']

    movie_recommendation_input_options = []
    for index, movie_data in enumerate(ratings):
        input_option = {
            'kind': 'static',
            'input': f'recc {index + 1}',
            'target': ('', {})
        }
        movie_recommendation_input_options.append(input_option)

    dynamic_screen_components = {
        'movie_ratings': [{
            'component': 'text',
            'text': format_ratings_page(ratings)
        }]
    }

    dynamic_input_options = {
        'dynamic_commands': [*movie_recommendation_input_options]
    }

    return handle_screen(
        movie_rating_screens,
        'movie_ratings_screen',
        dynamic_screen_components,
        dynamic_input_options
    )

def format_ratings_page(ratings):
    ratings_lines = []
    for index, item in enumerate(ratings):
        print(ratings)
        movie_details = item.get('movie_details', {})
        title = movie_details.get('title')

        movie_id = item['movie_id']
        is_rated = any(rating['movie_id'] == movie_id for rating in ratings)
        if is_rated:
            rating = next((rating['rating'] for rating in ratings if rating['movie_id'] == movie_id), None)
            rating = f' - {rating}/10'
        else:
            rating = ''

        ratings_lines.append(f'{index + 1}. {title}{rating}')
        print(ratings_lines)

    return '\n'.join(ratings_lines)

@app_context.screen_manager.register('movie_rating.rate_movie_screen', stackable=False)
def rate_movie_screen(context):
    next_screen_key, next_screen_params = handle_screen(movie_rating_screens, 'rate_movie_screen')
    params = context
    params['rating'] = next_screen_params['rating']
    app_context.clients.movie_rating_client.rate_movie(params)
    del next_screen_params['rating']
    return next_screen_key, next_screen_params

