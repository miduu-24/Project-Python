import unittest
from ro.ubb.filmapp.domain.entities import Client
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository
from ro.ubb.filmapp.service.service_clients import ClientService


class TestServiceClients(unittest.TestCase):
    def setUp(self):
        self.__repo = ClientsRepository()
        self.__service = ClientService(self.__repo)

    def test_save(self):
        self.assertEqual(self.__service.add_c(1, "ana", 1), None)

    def test_update(self):
        self.__service.add_c(1, "ana", 1)
        self.assertEqual(self.__service.update(1, "ana2", 1), "Done!")

    def test_delete_by_id(self):
        self.__service.add_c(1, "ana", 1)
        self.assertEqual(self.__service.delete_c(1), "Done!")

    def test_search_by_id(self):
        self.__service.add_c(1, "ana", 1)
        c = self.__service.search_c(1)
        self.assertEqual(c.get_id(), 1)
        self.assertEqual(c.get_name(), "ana")
        self.assertEqual(c.get_cnp(), 1)

    def test_get_all(self):
        self.__service.add_c(1, "ana", 1)
        c = self.__service.getAllClients()
        self.assertEqual(c[0].get_id(), 1)
        self.assertEqual(c[0].get_name(), "ana")
        self.assertEqual(c[0].get_cnp(), 1)
