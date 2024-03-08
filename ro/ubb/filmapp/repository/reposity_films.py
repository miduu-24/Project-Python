class FilmsRepository:
    def __init__(self):
        self.__all_films = []

    def find_by_id(self, id):
        """
        Return the film with id: id
        :param id: int
        :return: class or None
        """
        for pos in range(len(self.__all_films)):
            if self.__all_films[pos].get_id() == id:
                return self.__all_films[pos]
        return None

    def save(self, film):
        """
        Save a film in list
        :param film: class
        :return: None
        """
        self.__all_films.append(film)

    def update(self, film):
        """
        Update a film for the list
        :param film: class
        :return: string or error
        """
        film_old = self.find_by_id(film.get_id())
        if film_old is None:
            raise ValueError("\nThere is no film with that id")
        film_old.set_title(film.get_title())
        film_old.set_des(film.get_des())
        film_old.set_sort(film.get_sort())
        return "Done!"

    def delete_by_id(self, id):
        """
        Delete a film with that id
        :param id: int
        :return: string or error
        """
        film = self.find_by_id(id)
        if film is None:
            raise ValueError("\nThere is no film with that id")
        self.__all_films.remove(film)
        return "Done!"

    def search_by_id(self, id):
        """
        Search by id a film
        :param id: int
        :return: class or error
        """
        film = self.find_by_id(id)
        if film is None:
            raise ValueError("\nThere is no film with that id")
        return film

    def get_all(self):
        """
        Return all films
        :return: list
        """
        return self.__all_films
