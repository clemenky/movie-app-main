from clients.base_zmq_client import BaseZmqClient


class MovieRatingClient(BaseZmqClient):
    def rate_movie(self, params):
        return self._send_request({
            'type': 'query',
            'endpoint': 'rate_movie',
            'params': {
                'movie_id': params['movie_id'],
                'rating': params['rating'],
                'movie_details': params['movie_details']
            }
        })
    
    def get_rating(self, params):
        return self._send_request({
            'type': 'query',
            'endpoint': 'get_rating',
            'params': {
                'movie_id': params['movie_id']
            }
        })
    
    def list_ratings(self):
        return self._send_request({
            'type': 'query',
            'endpoint': 'list_ratings',
            'params': {}
        })
