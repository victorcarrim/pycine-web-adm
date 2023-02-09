import requests

key = '0892fa1a45e447f677743ea0775237e3'


class RequestApi:

    @staticmethod
    def get_movie_popular_by_genre(genre: int):
        endpoint = f'https://api.themoviedb.org/3/discover/movie/?api_key={key}&certification_country=US&certification=R&sort_by=vote_count.desc&with_genres={genre}'
        r = requests.get(endpoint)
        data = r.json()
        results = data['results']
        return results

    @staticmethod
    def get_id_person(person: str):
        endpoint = f'https://api.themoviedb.org/3/search/person?api_key={key}&query={person}'
        r = (requests.get(endpoint)).json()
        result = r['results']
        print(len(result))
        if len(result) == 0:
            id_person = 0
            return id_person
        person = result[0]
        id_person = person['id']
        return id_person

    @staticmethod
    def get_information_person(id_person: int):
        endpoint = f'https://api.themoviedb.org/3/person/{id_person}?api_key={key}'
        r = (requests.get(endpoint)).json()
        return r

    @staticmethod
    def get_popular_movies():
        endpoint = f'https://api.themoviedb.org/3/movie/popular?api_key={key}'
        r = (requests.get(endpoint)).json()
        result = r['results']
        return result

    @staticmethod
    def get_movie_by_id(movie_id: int):
        endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={key}'
        result = (requests.get(endpoint)).json()
        return result
