class ClientsRepository:
    def __init__(self):
        self.__all_clients = []

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
        Save a client in list
        :param client: class
        :return: string
        """
        self.__all_clients.append(client)

    def update(self, client):
        """
        Update a client for the list
        :param client: class
        :return: string or error
        """
        client_old = self.find_by_id(client.get_id())
        if client_old is None:
            raise ValueError("\nThere is no client with that id")
        client_old.set_name(client.get_name())
        client_old.set_cnp(client.get_cnp())
        return "Done!"

    def delete_by_id(self, id):
        """
        Delete a client with that id
        :param id: int
        :return: string or error
        """
        client = self.find_by_id(id)
        if client is None:
            raise ValueError("\nThere is no client with that id")
        self.__all_clients.remove(client)
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
        Return all clients
        :return: list
        """
        return self.__all_clients
