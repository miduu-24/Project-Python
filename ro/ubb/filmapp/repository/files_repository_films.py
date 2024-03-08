import json
from ro.ubb.filmapp.domain.entities import Film


class FilmsRepository:
    def __init__(self):
        """
        Initialize the repository from the file
        """
        self.__all_films = []
        with open("films.json", "r") as read:
            js = json.load(read)
        for i in js:
            film = Film(i["id"], i["title"], i["des"], i["sort"])
            self.__all_films.append(film)

    def file_save(self):
        """
        Save the repository in the file
        :return: None
        """
        with open("films.json", "w") as write:
            json.dump([x.as_dict() for x in self.__all_films], write)

    def find_by_id(self, id):
        """
        Find a film by id
        :param id: int
        :return: class or None
        """
        for pos in range(len(self.__all_films)):
            if self.__all_films[pos].get_id() == id:
                return self.__all_films[pos]
        return None

    def save(self, film):
        """
        Save a film in the file
        :param film: class
        :return: str
        """
        self.__all_films.append(film)
        self.file_save()
        return "Done!"

    def update(self, film):
        """
        Update a film in the file
        :param film: class
        :return: str or error
        """
        film_old = self.find_by_id(film.get_id())
        if film_old is None:
            raise ValueError("\nThere is no film with that id")
        film_old.set_title(film.get_title())
        film_old.set_des(film.get_des())
        film_old.set_sort(film.get_sort())
        self.file_save()
        return "Done!"

    def delete_by_id(self, id):
        """
        Delete a film by id
        :param id: int
        :return: str or error
        """
        film = self.find_by_id(id)
        if film is None:
            raise ValueError("\nThere is no film with that id")
        self.__all_films.remove(film)
        self.file_save()
        return "Done!"

    def search_by_id(self, id):
        """
        Search a film by id
        :param id: int
        :return: class or error
        """
        film = self.find_by_id(id)
        if film is None:
            raise ValueError("\nThere is no film with that id")
        return film

    def get_all(self):
        """
        Get all the films
        :return: list
        """
        return self.__all_films
