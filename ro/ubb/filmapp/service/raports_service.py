from ro.ubb.filmapp.domain.dto import RentDTOAssembler
from ro.ubb.filmapp.repository.files_repository_rents import RentFilms
from ro.ubb.filmapp.repository.files_repository_clients import ClientsRepository
from ro.ubb.filmapp.repository.files_repository_films import FilmsRepository


class RapportsService:
    def __init__(self):
        self.__rent_repos = RentFilms()
        self.__films_repos = FilmsRepository()
        self.__clients_repos = ClientsRepository()

    def __create_rent_dto(self):
        rent_dto = []
        for client in self.__clients_repos.get_all():
            films = self.__get_client_films(client)
            dto = RentDTOAssembler.create_rent_dto(client, films)
            rent_dto.append(dto)
        return rent_dto

    def __get_client_films(self, client):
        list_rents = self.__rent_repos.get_val()
        client_rent = list(filter(lambda rent_client: rent_client[1] == client.get_name(), list_rents))
        films = []
        for rent in client_rent:
            films.append(rent[0])
        return films

    def alphabetic_clients(self):
        """
        Return a list of clients in alphabetic order
        :return: list
        """
        rent_dto = self.__create_rent_dto()
        alphabetic = sorted(rent_dto, key=lambda rent_: rent_.name_client)
        return alphabetic

    def number_films(self):
        """
        Return a list of clients in order of the number of films
        :return: list
        """
        rent_dto = self.__create_rent_dto()
        number_films = sorted(rent_dto, key=lambda rent_: rent_.nr_film, reverse=True)
        return number_films
