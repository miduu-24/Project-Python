import unittest
from ro.ubb.filmapp.domain.entities import Client
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository


class TestClientRepository(unittest.TestCase):
    def setUp(self):
        self.client_repository = ClientsRepository()
        self.client_1 = Client(1, "ana", 1)
        self.client_2 = Client(2, "maria", 2)
        self.client_repository.save(self.client_1)

    def test_find_by_id_client_repository(self):
        assert self.client_repository.find_by_id(1) == self.client_1
        assert self.client_repository.find_by_id(2) is None

    def test_add_client_repository(self):
        clients = self.client_repository.get_all()
        assert len(clients) == 1
        assert clients[0].get_id() == 1

    def test_update_client_repository(self):
        client_new_1 = Client(1, "florin", 2)
        self.client_repository.update(client_new_1)
        clients = self.client_repository.get_all()
        assert clients[0].get_name() == "florin"

        client_new_2 = Client(3, "florin", 2)
        self.assertRaises(ValueError, self.client_repository.update, client_new_2)

    def test_delete_client_repository(self):
        self.client_repository.delete_by_id(1)
        clients = self.client_repository.get_all()
        assert len(clients) == 0

        self.assertRaises(ValueError, self.client_repository.delete_by_id, 2)

    def test_search_client_repository(self):
        assert self.client_repository.search_by_id(1) == self.client_1
        self.assertRaises(ValueError, self.client_repository.search_by_id, 2)
