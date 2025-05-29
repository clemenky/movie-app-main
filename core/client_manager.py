from clients.movie_search_client import MovieSearchClient
from clients.movie_watchlist_client import MovieWatchlistClient


class ClientManager:
    def __init__(self):
        self.movie_search_client = MovieSearchClient('tcp://localhost:5555')
        self.movie_watchlist_client = MovieWatchlistClient('tcp://localhost:5556')

    def close_all(self):
        self.movie_search_client.close()
        self.movie_watchlist_client.close()
