from clients.movie_search_client import MovieSearchClient
from clients.movie_discovery_client import MovieDiscoveryClient
from clients.movie_watchlist_client import MovieWatchlistClient
from clients.movie_rating_client import MovieRatingClient


class ClientManager:
    def __init__(self):
        self.movie_search_client = MovieSearchClient('tcp://localhost:5555')
        self.movie_discovery_client = MovieDiscoveryClient('tcp://localhost:5556')
        self.movie_watchlist_client = MovieWatchlistClient('tcp://localhost:5557')
        self.movie_rating_client = MovieRatingClient('tcp://localhost:5558')

    def close_all(self):
        self.movie_search_client.close()
        self.movie_watchlist_client.close()
