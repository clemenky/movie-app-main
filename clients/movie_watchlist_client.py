from clients.base_zmq_client import BaseZmqClient


class MovieWatchlistClient(BaseZmqClient):
    def add_movie(self, params):
        return self._send_request({
            'type': 'query',
            'endpoint': 'add_movie',
            'params': {
                'movie_id': params['movie_id'],
                'movie_details': params['movie_details']
            }
        })
    
    def delete_movie(self, params):
        return self._send_request({
            'type': 'query',
            'endpoint': 'delete_movie',
            'params': {
                'movie_id': params['movie_id']
            }
        })
    
    def list_movies(self):
        return self._send_request({
            'type': 'query',
            'endpoint': 'list_movies',
            'params': {}
        })
