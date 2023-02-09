class TMDBMovie:
    def __init__(self, id_movie, title,
                 popularity=None,
                 poster_path=None,
                 release_date=None,
                 overview=None,
                 vote_avarage=None
                 ):
        self.id = id_movie
        self.title = title
        self.popularity = popularity
        self.poster_path = poster_path
        self.release_date = release_date
        self.overview = overview
        self.vote_avarage = vote_avarage
