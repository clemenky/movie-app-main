import input_utils


class MovieWatchlist:
    def __init__(self, clients):
        self.clients = clients

    def add_movie(self, movie_id, title, year):
        self.clients.movie_watchlist.add_movie(movie_id, title, year)
    
    def delete_movie(self, movie_id):
        self.clients.movie_watchlist.delete_movie(movie_id)