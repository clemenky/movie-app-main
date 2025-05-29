from clients.base_zmq_client import BaseZmqClient


class MovieSearchClient(BaseZmqClient):
    def search_by_title(self, title, page):
        print('Fetching results from TMDB...')
        return self._send_request({
            'type': 'query',
            'endpoint': 'search_by_title',
            'params': {
                'title': title,
                'page': page
            }
        })
    
    def get_movie_details(self, movie_id):
        print('Fetching results from TMDB...')
        return self._send_request({
            'type': 'query',
            'endpoint': 'get_movie_details',
            'params': {
                'movie_id': movie_id
            }
        })
        
        
