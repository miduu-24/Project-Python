import json
from ro.ubb.filmapp.domain.entities import Client


class ClientsRepository:
    def __init__(self):
        """
        Initialize the list of clients from file
        """
        self.__all_clients = []
        with open("clients.json", "r") as read:
            js = json.load(read)
        for i in js:
            client = Client(i["id"], i["name"], i["cnp"])
            self.__all_clients.append(client)

    def file_save(self):
        """
        Save the list of clients in file
        :return: None
        """
        with open("clients.json", "w") as write:
            json.dump([x.as_dict() for x in self.__all_clients], write)

    def find_by_id(self, id):
        """
        Return the client with id: id
        :param id: int
        :return: client or none
        """
        for pos in range(len(self.__all_clients)):
            if self.__all_clients[pos].get_id() == id:
                return self.__all_clients[pos]
        return None

    def save(self, client):
        """
        Save a client in file
        :param client: class
        :return: string
        """
        self.__all_clients.append(client)
        self.file_save()  # save the list in file

    def update(self, client):
        """
        Update a client for the list from file
        :param client: class
        :return: string or error
        """
        client_old = self.find_by_id(client.get_id())
        if client_old is None:
            raise ValueError("\nThere is no client with that id")
        client_old.set_name(client.get_name())
        client_old.set_cnp(client.get_cnp())
        self.file_save()  # save the list in file
        return "Done!"

    def delete_by_id(self, id):
        """
        Delete a client with that id from the list and file
        :param id: int
        :return: string or error
        """
        client = self.find_by_id(id)
        if client is None:
            raise ValueError("\nThere is no client with that id")
        self.__all_clients.remove(client)
        self.file_save()  # save the list in file
        return "Done!"

    def search_by_id(self, id):
        """
        Search by id a client
        :param id: int
        :return: client:class or error
        """
        client = self.find_by_id(id)
        if client is None:
            raise ValueError("\nThere is no client with that id")
        return client

    def get_all(self):
        """
        Return the list of clients
        :return: list
        """
        return self.__all_clients
