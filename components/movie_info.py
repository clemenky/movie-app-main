import input_utils
import pycountry


class MovieInfo:
    def __init__(self, clients):
        self.clients = clients

    def movie_search_screen(self):
        params = {
            'title': '🔍 Movie Search',
            'prompt': 'Enter how you want to search:',
            'options': [
                {
                    'input': '1',
                    'text': 'Search by title',
                    'function': 'movie_info.search_by_title_screen'
                },
                {
                    'input': '2',
                    'text': 'Search by TMDB ID',
                    'function': 'movie_info.search_by_id_screen'
                },
                {
                    'input': 'b',
                    'text': 'Back',
                    'function': 'back'
                }
            ]
        }

        return input_utils.handle_input(params)
    
    def search_by_title_screen(self):
        params = {
            'prompt': 'Enter movie title:',
            'text_input': {
                'function': 'movie_info.search_by_title_results_screen',
                'param_name': 'title',
                'validate': lambda x: x != ''
            }
        }
        return input_utils.handle_input(params)
    
    def search_by_title_results_screen(self, title, page=1):
        data = self.clients.movie_info.search_by_title(title, page)
        results = data['result']['results']
        total_pages = min(data['result'].get('total_pages', 1), 10)

        params = {
            'prompt': 'Select movie by number or choose:',
            'options': [
                {
                    'input': 'b',
                    'text': 'Back',
                    'function': 'back'
                },
                {
                    'input': 'h',
                    'text': 'Home',
                    'function': 'home'
                }
            ]
        }

        print(f'Search results for "{title}" ({page}/{total_pages}):')
        for index, result in enumerate(results):
            if result['release_date']:
                release_year = result['release_date'].split('-')[0]
            else:
                release_year = 'Unknown'

            print(f'{index + 1}. {result['title']} ({release_year})')

            params['options'].append({
                'input': str(index + 1),
                'function': 'movie_info.show_movie_info_screen',
                'params': {'movie_id': results[index]['id']},
                'hidden': True
            })
        
        print('')

        if page > 1:
            params['options'].append({
                'input': 'p',
                'text': 'Previous Page',
                'function': 'movie_info.search_by_title_results_screen',
                'params': {'title': title, 'page': page - 1}
            })

        if page < total_pages:
            params['options'].append({
                'input': 'n',
                'text': 'Next Page',
                'function': 'movie_info.search_by_title_results_screen',
                'params': {'title': title, 'page': page + 1}
            })
        
        return input_utils.handle_input(params)
    
    def show_movie_info_screen(self, movie_id):
        data = self.clients.movie_info.get_movie_details(movie_id)
        result = data['result']

        title = result['title']
        release_date = result['release_date']
        genres = [genre['name'] for genre in result['genres']]
        runtime = result['runtime']
        vote_average = result['vote_average']
        overview = result['overview']
        original_language = result['original_language']

        lang = pycountry.languages.get(alpha_2=original_language)
        formatted_language = lang.name if lang else original_language.upper()

        formatted_content_rating = 'Not Rated'
        for country_info in result['release_dates'].get('results', []):
            if country_info.get('iso_3166_1') == 'US':
                for release in country_info.get('release_dates', []):
                    certification = release.get('certification', '').strip()
                    if certification:
                        formatted_content_rating = f'Rating: {certification}'
        
        cast = [actor['name'] for actor in result['credits']['cast'] if actor['known_for_department'] == 'Acting'][:3] or None

        director = None
        for crew_member in result['credits']['crew']:
            if crew_member['job'] == 'Director':
                director = crew_member['name']
                break

        release_year = release_date.split('-')[0]
        hours = runtime // 60
        minutes = runtime % 60
        vote_average_percent = round(float(vote_average) * 10)
        divider = '-' * 50

        formatted_output = f'{divider}\n{title} ({release_year})\n{divider}\n'
        formatted_output += f'{formatted_content_rating} | Genre: {', '.join(genres)} | Runtime: {hours}h {minutes}m\n'
        formatted_output += f'{vote_average_percent}% TMDB Rating\n\n'
        formatted_output += f'{overview}\n\n'
        formatted_output += f'Director: {director}\nCast: {', '.join(cast)}\nLanguage: {formatted_language}\n'

        print(formatted_output)

        params = {
            'prompt': 'Choose an action:',
            'options': [
                {
                    'input': 'b',
                    'text': 'Back',
                    'function': 'back'
                },
                {
                    'input': 'h',
                    'text': 'Home',
                    'function': 'home'
                }
            ]
        }

        response = self.clients.movie_watchlist.list_movies()
        watchlist = response['result']

        in_watchlist = any(movie['id'] == movie_id for movie in watchlist)

        if in_watchlist:
            params['title'] = 'ℹ️ This movie is in your watchlist.'
            params['options'].insert(0, {
                'input': '1',
                'text': 'Remove from watchlist',
                'function': 'movie_info.show_movie_info_screen',
                'action': 'movie_watchlist.delete_movie',
                'action_params': {'movie_id': movie_id},
                'params': {'movie_id': movie_id},
                'confirmation': 'Are you sure you want to remove this movie from your watchlist?'
            })
        else:
            params['options'].insert(0, {
                'input': '1',
                'text': 'Add to watchlist',
                'function': 'movie_info.show_movie_info_screen',
                'action': 'movie_watchlist.add_movie',
                'action_params': {'movie_id': movie_id, 'movie_title': title, 'movie_year': release_year},
                'params': {'movie_id': movie_id}
            })

        output = input_utils.handle_input(params)
        next_screen, output_params = output
        if next_screen == 'movie_info.show_movie_info_screen':
            if in_watchlist:
                self.clients.movie_watchlist.delete_movie(movie_id)
            else:
                self.clients.movie_watchlist.add_movie(movie_id, title, release_year)
        return output
    
    def search_by_id_screen(self):
        params = {
            'prompt': 'Enter TMDB ID:',
            'text_input': {
                'function': 'movie_info.show_movie_info_screen',
                'param_name': 'movie_id',
                'validate': lambda x: x != ''
            }
        }
        return input_utils.handle_input(params)
