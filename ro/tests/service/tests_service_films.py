import unittest
from ro.ubb.filmapp.domain.entities import Film
from ro.ubb.filmapp.repository.reposity_films import FilmsRepository
from ro.ubb.filmapp.service.service_films import FilmService

class TestServiceFilms(unittest.TestCase):
    def setUp(self):
        self.__repo = FilmsRepository()
        self.__service = FilmService(self.__repo)

    def test_save(self):
        self.assertEqual(self.__service.add_f(1, "title", "des", "sort"), None)

    def test_update(self):
        self.__service.add_f(1, "title", "des", "sort")
        self.assertEqual(self.__service.update_f(1, "title2", "des", "sort"), "Done!")

    def test_delete_by_id(self):
        self.__service.add_f(1, "title", "des", "sort")
        self.assertEqual(self.__service.delete_f(1), "Done!")

    def test_search_by_id(self):
        self.__service.add_f(1, "title", "des", "sort")
        f = self.__service.search_f(1)
        self.assertEqual(f.get_id(), 1)
        self.assertEqual(f.get_title(), "title")
        self.assertEqual(f.get_des(), "des")
        self.assertEqual(f.get_sort(), "sort")

    def test_get_all(self):
        self.__service.add_f(1, "title", "des", "sort")
        f = self.__service.getAllFilms()
        self.assertEqual(f[0].get_id(), 1)
        self.assertEqual(f[0].get_title(), "title")
        self.assertEqual(f[0].get_des(), "des")
        self.assertEqual(f[0].get_sort(), "sort")
