from ro.ubb.filmapp.repository.reposity_films import FilmsRepository
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository
from ro.ubb.filmapp.repository.reposity_rents import RentFilms


class RentService:
    def __init__(self, rent_repository: RentFilms, films_repository: FilmsRepository,
                 clients_repository: ClientsRepository):
        self.__rent_repos = rent_repository
        self.__films_repos = films_repository
        self.__clients_repos = clients_repository

    def f_c_in_list(self, id_f, id_c):
        """
        Check if a film and a client are in the list of films and clients
        :param id_f: int
        :param id_c: int
        :return: str
        """
        id_f_comp = self.__films_repos.find_by_id(id_f)
        id_c_comp = self.__clients_repos.find_by_id(id_c)

        if id_f_comp is not None:
            if id_c_comp is not None:
                return "Done!"
            else:
                raise ValueError("\nThis customer doesn't have an account")
        else:
            raise ValueError("\nThis movie hasn't been added")

    def add_r(self, id_film, id_client):
        """
        Add a rent
        :param id_film: int
        :param id_client: int
        :return: None
        """
        film = self.__films_repos.find_by_id(id_film)  # find the film by id in the list of films
        client = self.__clients_repos.find_by_id(id_client)  # find the client by id in the list of clients
        self.__rent_repos.rent(film, client)  # add the rent

    def delete_r(self, id_film, id_client):
        """
        Delete a rent
        :param id_film: int
        :param id_client: int
        :return: str or error
        """
        film = self.__films_repos.find_by_id(id_film)  # find the film by id in the list of films
        client = self.__clients_repos.find_by_id(id_client)  # find the client by id in the list of clients
        return self.__rent_repos.returned(film, client)

    def alphabetic_clients(self):
        """
        Return a list of clients in alphabetic order
        :return: list
        """
        useless, list_clients = self.__rent_repos.return_films_and_clients()  # get the list of clients,
        # useless = list of films
        results = []  # list of clients after eliminating the duplicates
        for element in list_clients:
            if element not in results:
                results.append(element)  # add the client in the list of clients
        results.sort()  # sort the list of clients
        return results

    def number_films(self):
        """
        Return a list of clients sorted by the number of films rented and the number of films rented
        :return:
        """
        alphabetic = self.alphabetic_clients()  # get the list of clients in alphabetic order
        useless, list_clients = self.__rent_repos.return_films_and_clients()  # get the list of clients,
        # useless = list of films
        number_films = []  # list of the number of films rented by each client
        results = []  # list of clients after sorting them by the number of films rented
        for client in alphabetic:
            n = list_clients.count(client)  # count the number of films rented by a client,
            # count the number of times the client appears in the list of clients
            number_films.append(n)
        copy_number_films = number_films[:]  # copy the list of the number of films rented by each client

        while len(results) < len(number_films):
            number_max = max(number_films)  # get the maximum number of films rented by a client
            pos = number_films.index(number_max)  # get the position of the maximum number of films rented by a client
            results.append(alphabetic[pos])  # add the client from the position "pos"
            # from the list of clients in alphabetic order
            number_films[pos] = 0  # set the number of films rented by the client from the position "pos" to 0
        copy_number_films.sort(reverse=True)  # sort the list of the number of films rented by each client
        # in descending order
        return results, copy_number_films

    def popular_films(self):
        """
        Return a list of films sorted by the number of times they were rented and the number of times they were rented
        :return: list
        """
        list_films, useless = self.__rent_repos.return_films_and_clients()  # get the list of films,
        # useless = list of clients
        all_films = self.__rent_repos.all_films()  # get the list of all films
        number_clients = []  # list of the number of times each film was rented
        results = []
        for film in all_films:
            n = list_films.count(film)  # count the number of times a film was rented,
            # count the number of times the film appears in the list of films
            number_clients.append(n)

        while len(results) < len(number_clients):
            number_max = max(number_clients)  # get the maximum number of times a film was rented
            pos = number_clients.index(number_max)  # get the position of the maximum number of times a film was rented
            results.append(all_films[pos])  # add the film from the position "pos" from the list of all films
            number_clients[pos] = 0  # set the number of times the film from the position "pos" was rented to 0

        return results

    def clients_30(self):
        """
        Return a list 30% of clients who rented the most films
        :return: list, list
        """
        client_list, number_film = self.number_films()  # get the list of clients sorted by the number of films rented
        long = int((3 / 10) * len(client_list))  # 30% of the number of clients
        client_list_new, number_film_new = [], []
        for i in range(long):
            client_list_new.append(client_list[i])
            number_film_new.append(number_film[i])

        return client_list_new, number_film_new

    def getAllRents(self):
        """
        Return a list of rents
        :return: list
        """
        return self.__rent_repos.get_val()
