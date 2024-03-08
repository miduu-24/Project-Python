from ro.ubb.filmapp.domain.entities import Client
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository


class ClientService:
    def __init__(self, clients_repository: ClientsRepository):
        self.__clients_repos = clients_repository

    def add_c(self, id, name, cnp):
        """
        Add a client
        :param id: int
        :param name: str
        :param cnp: int
        :return: None
        """
        client = Client(id, name, cnp)
        self.__clients_repos.save(client)

    def update(self, id, new_name, new_cnp):
        """
        Update a client
        :param id: int
        :param new_name: str
        :param new_cnp: int
        :return: str
        """
        client = Client(id, new_name, new_cnp)
        return self.__clients_repos.update(client)

    def delete_c(self, id):
        """
        Delete a client
        :param id: int
        :return: str
        """
        return self.__clients_repos.delete_by_id(id)

    def search_c(self, id):
        """
        Search a client by id
        :param id: int
        :return: client or error
        """
        return self.__clients_repos.search_by_id(id)

    def getAllClients(self):
        """
        Get all the clients
        :return: list
        """
        return self.__clients_repos.get_all()
