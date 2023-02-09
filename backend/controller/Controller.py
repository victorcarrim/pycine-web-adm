from models.Person import Person
from models.Movie import TMDBMovie
from routes.RequestApi import RequestApi


class Controller:

    @staticmethod
    def get_information(id_person: int):
        print(id_person)
        results = RequestApi.get_information_person(id_person)
        print(results)

    @staticmethod
    def get_image_path(poster_path):
        return f"https://image.tmdb.org/t/p/w185{poster_path}"

    @staticmethod
    def get_person(person: str):
        results = RequestApi.get_id_person(person)
        if results == 0:
            person = False
            return person
        person_information = RequestApi.get_information_person(results)
        person = Person(
            person_information['id'],
            person_information['name'],
            person_information['birthday'],
            person_information['deathday'],
            person_information['place_of_birth'],
            person_information['popularity'],
            person_information['gender'],
            person_information['known_for_department'],
            Controller.get_image_path(person_information['profile_path']),
            person_information['biography'],
            person_information['homepage']
        )
        return person

    @staticmethod
    def get_popular_movies():
        movies = RequestApi.get_popular_movies()
        movies_list = []
        for movie in movies:
            movie_reformat = TMDBMovie(
                movie['id'],
                movie['title'],
                movie['popularity'],
                Controller.get_image_path(movie['poster_path']),
                movie['release_date'],
                movie['overview'],
                movie['vote_average']
            )
            movies_list.append(movie_reformat)
        return movies_list

    @staticmethod
    def get_movie_by_id(movie_id: int):
        movie = RequestApi.get_movie_by_id(movie_id)
        movie_reformat = TMDBMovie(
            movie['id'],
            movie['title'],
            movie['popularity'],
            Controller.get_image_path(movie['poster_path']),
            movie['release_date'],
            movie['overview'],
            movie['vote_average']
        )
        return movie_reformat
