import unittest
from unittest.mock import patch, mock_open
from ro.ubb.filmapp.repository.files_repository_clients import ClientsRepository
from ro.ubb.filmapp.domain.entities import Client


class TestClients(unittest.TestCase):
    def setUp(self):
        with patch("builtins.open", mock_open(read_data="[{\"id\": \"74\", \"name\": \"geo\", \"cnp\": 1}]")):
            self.__clients = ClientsRepository()
        self.__client = Client(1, "John", "Doe")

    def test_save(self):
        self.__clients.save(self.__client)
        self.assertEqual(self.__clients.get_all()[1], self.__client)

    def test_update(self):
        self.__clients.save(self.__client)
        self.__client.set_name("Jane")
        self.__client.set_cnp("Doe")
        self.__clients.update(self.__client)
        self.assertEqual(self.__clients.get_all()[1], self.__client)
        self.assertRaises(ValueError, self.__clients.update, Client(2, "Jane", "Doe"))

    def test_delete_by_id(self):
        self.__clients.save(self.__client)
        self.__clients.delete_by_id(1)
        self.assertEqual(len(self.__clients.get_all()), 1)
        self.assertRaises(ValueError, self.__clients.delete_by_id, 2)

    def test_search_by_id(self):
        self.__clients.save(self.__client)
        self.assertEqual(self.__clients.search_by_id(1), self.__client)
        self.assertRaises(ValueError, self.__clients.search_by_id, 2)

    def test_get_all(self):
        self.__clients.save(self.__client)
        self.assertEqual(self.__clients.get_all()[1], self.__client)