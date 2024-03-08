import random
import json


class RentFilms:
    def __init__(self):
        """
        Initialize the class from the file
        """
        with open("rents.json", "r") as read:
            self.__rent_film = json.load(read)

    def file_save(self):
        """
        Save in the file
        :return: None
        """
        with open("rents.json", "w") as write:
            json.dump(self.__rent_film, write)

    def rent(self, film, client):
        """
        Rent a film - add to the file
        :param film: class Film
        :param client: class Client
        :return: None
        """
        id_key = random.randrange(0, 100)
        self.__rent_film[id_key] = [film.get_title(), client.get_name()]
        self.file_save()

    def returned(self, film, client):
        """
        Return a film - delete from the file
        :param film: class Film
        :param client: class Client
        :return: str or error
        """
        for i in self.__rent_film.keys():
            if self.__rent_film[i][0] == film.get_title():
                if self.__rent_film[i][1] == client.get_name():
                    del self.__rent_film[i]
                    self.file_save()
                    return "Done!"
        raise ValueError(f"{client.get_name()} doesn't rent {film.get_title()}")

    def return_films_and_clients(self):
        """
        Return the films and clients
        :return: list, list
        """
        list_films, list_clients = [], []
        for i in self.__rent_film.keys():
            list_films.append(self.__rent_film[i][0])
            list_clients.append(self.__rent_film[i][1])
        return list_films, list_clients

    def all_films(self):
        """
        Return all the films
        :return: list
        """
        list_films, useless = self.return_films_and_clients()
        results = []
        for element in list_films:
            if element not in results:
                results.append(element)
        return results

    def get_val(self):
        """
        Return the dictionary been a list
        :return:
        """
        return list(self.__rent_film.values())
