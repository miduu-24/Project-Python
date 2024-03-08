import random


class RentFilms:
    def __init__(self):
        self.__rent_film = {}

    def rent(self, film, client):
        """
        Rent a film
        :param film: class
        :param client: class
        :return: None
        """
        id_key = random.randrange(0, 100)
        self.__rent_film[id_key] = [film.get_title(), client.get_name()]

    def returned(self, film, client):
        """
        Return a film
        :param film: class
        :param client: class
        :return: string or error
        """
        for i in self.__rent_film.keys():
            if self.__rent_film[i][0] == film.get_title():  # if the film is in the list of films
                if self.__rent_film[i][1] == client.get_name():  # if the client is in the list of clients
                    del self.__rent_film[i]  # delete the rent
                    return "Done!"
        raise ValueError(f"{client.get_name()} doesn't rent {film.get_title()}")

    def return_films_and_clients(self):
        """
        Return the list of films and one of clients
        :return: list, list
        """
        list_films, list_clients = [], []
        for i in self.__rent_film.keys():
            list_films.append(self.__rent_film[i][0])
            list_clients.append(self.__rent_film[i][1])
        return list_films, list_clients

    def all_films(self):
        """
        Return the list of films
        :return: list
        """
        list_films, useless = self.return_films_and_clients()  # useless = list of clients
        results = []
        for element in list_films:
            if element not in results:
                results.append(element)
        return results  # return the list of films with no duplicates

    def get_val(self):
        """
        Return a list of rents
        :return: list
        """
        return list(self.__rent_film.values())
