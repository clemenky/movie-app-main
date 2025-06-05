from clients.base_zmq_client import BaseZmqClient


class MovieDiscoveryClient(BaseZmqClient):
    def get_trending_movies(self, sort_by="popularity", genres=None, time_range="week", page=1, start_year=None, end_year=None):
        params = {
            'sort_by': sort_by,
            'genres': genres or [],
            'time_range': time_range,
            'page': page
        }
        if time_range == 'custom':
            if start_year is not None:
                params['start_year'] = start_year
            if end_year is not None:
                params['end_year'] = end_year

        return self._send_request({
            'type': 'query',
            'endpoint': 'trending-movies',
            'params': params
        })
    
    def get_recommendations(self, movie_id, page=1):
        return self._send_request({
            'type': 'query',
            'endpoint': 'movie-recommendations',
            'params': {
                'movie_id': movie_id,
                'page': page
            }
        })
