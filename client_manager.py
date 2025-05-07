from clients.movie_info_client import MovieInfoClient
from clients.movie_watchlist_client import MovieWatchlistClient


class ClientManager:
    def __init__(self):
        self.movie_info = MovieInfoClient('tcp://localhost:5555')
        self.movie_watchlist = MovieWatchlistClient('tcp://localhost:5556')

    
    def close_all(self):
        self.movie_info.close()
