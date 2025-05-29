from clients.base_zmq_client import BaseZmqClient


class MovieWatchlistClient(BaseZmqClient):
    def add_movie(self, movie_id, title, year):
        return self._send_request({
            'type': 'query',
            'endpoint': 'add_movie',
            'params': {
                'movie_id': movie_id,
                'movie_title': title,
                'movie_year': year
            }
        })
    
    def delete_movie(self, movie_id):
        return self._send_request({
            'type': 'query',
            'endpoint': 'delete_movie',
            'params': {
                'movie_id': movie_id
            }
        })
    
    def list_movies(self):
        return self._send_request({
            'type': 'query',
            'endpoint': 'list_movies',
            'params': {}
        })
