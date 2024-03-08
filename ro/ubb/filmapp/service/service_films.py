from ro.ubb.filmapp.domain.entities import Film
from ro.ubb.filmapp.repository.reposity_films import FilmsRepository


class FilmService:
    def __init__(self, films_repository: FilmsRepository):
        self.__films_repos = films_repository

    def add_f(self, id, title, des, sort):
        """
        Add a film
        :param id: int
        :param title: str
        :param des: str
        :param sort: str
        :return: None
        """
        film = Film(id, title, des, sort)
        self.__films_repos.save(film)

    def update_f(self, id, new_title, new_des, new_sort):
        """
        Update a film
        :param id: int
        :param new_title: str
        :param new_des: str
        :param new_sort: str
        :return: str
        """
        film = Film(id, new_title, new_des, new_sort)
        return self.__films_repos.update(film)

    def delete_f(self, id):
        """
        Delete a film
        :param id: int
        :return: str
        """
        return self.__films_repos.delete_by_id(id)

    def search_f(self, id):
        """
        Search a film by id
        :param id: int
        :return: film or error
        """
        return self.__films_repos.search_by_id(id)

    def getAllFilms(self):
        """
        Get all the films
        :return: list
        """
        return self.__films_repos.get_all()
