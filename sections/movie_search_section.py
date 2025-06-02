import pycountry

from core.global_context import app_context
from core.screen_handler import handle_screen
import screens.movie_search as movie_search_screens
from config import MAX_SEARCH_RESULTS_PAGES
from globals import MOVIE_SEARCH_ICONS


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
    search_query = context.get('search_query')
    page = context.get('page', 1)

    raw_response = app_context.clients.movie_search_client.search_by_title(search_query, page)
    movie_results = raw_response['result']['results']
    total_pages = min(raw_response['result'].get('total_pages', 1), MAX_SEARCH_RESULTS_PAGES)

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
    raw_response = app_context.clients.movie_search_client.get_movie_details(movie_id)
    movie_details = raw_response['result']
    movie_details = parse_movie_details(raw_response)
    dynamic_screen_components = {
        'movie_details': get_movie_details_components(movie_details)
    }
    return handle_screen(movie_search_screens, 'movie_details_screen', dynamic_screen_components=dynamic_screen_components)


def parse_movie_details(raw_response):
    movie_data = raw_response['result']

    # either sets to value or None or array or empty array
    movie_details = {
        'title': movie_data.get('title'),
        'release_year': get_release_year(movie_data),
        'content_rating': get_content_rating(movie_data),
        'genres': get_genres(movie_data),
        'runtime': get_runtime(movie_data),  # { 'hours': hours, 'minutes': minutes }
        'audience_rating': get_audience_rating(movie_data),
        'description': movie_data.get('overview'),
        'director': get_director(movie_data),
        'cast': get_cast(movie_data),
        'language': get_language(movie_data)
    }

    return movie_details

def get_release_year(movie_data):
    release_date = movie_data.get('release_date')
    if release_date:
        return release_date.split('-')[0]
    return None

def get_content_rating(movie_data):
    for country_release_data in movie_data.get('release_dates', {}).get('results', []):
        if country_release_data.get('iso_3166_1') == 'US':
            for release in country_release_data.get('release_dates', []):
                certification = release.get('certification', '').strip()
                if certification:
                    return f'Rating: {certification}'
    
    return None

def get_genres(movie_data):
    genres = []
    genres_list = movie_data.get('genres', [])
    for genre in genres_list:
        genre_name = genre.get('name')
        if genre_name:
            genres.append(genre_name)
    
    return genres

def get_runtime(movie_data):
    runtime = movie_data.get('runtime')
    if runtime:
        return {
            'hours': runtime // 60,
            'minutes': runtime % 60
        }
    return None

def get_audience_rating(movie_data):
    audience_rating = movie_data.get('vote_average')
    if not audience_rating:
        return None
    return round(float(audience_rating) * 10)

def get_director(movie_data):
    crew = movie_data.get('credits', {}).get('crew', [])

    for crew_member in crew:
        if crew_member.get('job') == 'Director':
            return crew_member.get('name')
    
    return None

def get_cast(movie_data):
    actor_limit = 3
    cast = []
    credits = movie_data.get('credits', {})
    for actor in credits.get('cast', []):
        if actor.get('known_for_department') == 'Acting':
            name = actor.get('name')
            if name:
                cast.append(name)
            if len(cast) == actor_limit:
                break
    return cast or None

def get_language(movie_data):
    language_code = movie_data.get('original_language')
    if not language_code:
        return None

    language_obj = pycountry.languages.get(alpha_2=language_code)
    if language_obj and hasattr(language_obj, 'name'):
        return language_obj.name
    
    return language_code.upper()

def get_movie_details_components(movie_details):
    title = movie_details.get('title') or 'Title not found'
    release_year = movie_details.get('release_year') or 'Release year not found'
    content_rating = movie_details.get('content_rating') or 'Not Rated'
    genres = movie_details.get('genres') or []
    runtime = movie_details.get('runtime') or {}
    hours = runtime.get('hours')
    minutes = runtime.get('minutes')
    audience_rating = movie_details.get('audience_rating')
    description = movie_details.get('description') or 'Description not found'
    director = movie_details.get('director')
    cast = movie_details.get('cast') or []
    language = movie_details.get('language') or 'Unknown'

    # Title line: title, release year
    title_line = f'{title} ({release_year})'

    # Meta line: content rating, genres, runtime
    meta_line = f'{content_rating} | '
    if genres:
        genre_label = 'Genre' if len(genres) == 1 else 'Genres'
        meta_line += f'{genre_label}: {", ".join(genres)}'
    else:
        meta_line += f'Genres: Not found'

    meta_line += ' | '
    if hours is not None and minutes is not None:
        meta_line += f'Runtime: {hours}h {minutes}m'
    else:
        meta_line += 'Runtime: Not found'
    
    # Rating line
    if audience_rating:
        rating_line = f'{audience_rating}% TMDB Rating'
    else:
        rating_line = 'Audience rating not found'
    
    # Description line
    description_line = description

    # Extra meta line: director, cast, language
    extra_lines = []
    if director:
        extra_lines.append(f'Director: {director}')
    if cast:
        extra_lines.append(f'Cast: {", ".join(cast)}')
    if language:
        extra_lines.append(f'Language: {language}')
    extra_meta_line = '\n'.join(extra_lines)

    body_text = '\n'.join([
        meta_line,
        rating_line,
        '',
        description_line,
        '',
        extra_meta_line
    ])
    
    components = [
        {
            'component': 'title',
            'icon': MOVIE_SEARCH_ICONS['movie_details'],
            'text': title_line,
            'style': {
                'icon': True
            }
        },
        {
            'component': 'text',
            'text': body_text
        }
    ]

    return components
