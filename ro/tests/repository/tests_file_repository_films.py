import unittest
from unittest.mock import patch, mock_open
from ro.ubb.filmapp.repository.files_repository_films import FilmsRepository
from ro.ubb.filmapp.domain.entities import Film


class TestFilmsRepository(unittest.TestCase):
    def setUp(self):
        with patch("builtins.open", mock_open(read_data = "[{\"id\": 40, \"title\": \"1\", \"des\": \"11\", "
                                                          "\"sort\": \"ceva\"}]")):
            self.__repo = FilmsRepository()

    def test_find_by_id(self):
        film = Film(1, "title", "des", "sort")
        self.__repo.save(film)
        self.assertEqual(self.__repo.find_by_id(1), film)
        self.assertEqual(self.__repo.find_by_id(2), None)

    def test_save(self):
        film = Film(1, "title", "des", "sort")
        self.__repo.save(film)
        self.assertEqual(self.__repo.get_all()[1], film)

    def test_update(self):
        film = Film(1, "title", "des", "sort")
        self.__repo.save(film)
        film.set_title("title2")
        self.__repo.update(film)
        self.assertEqual(self.__repo.get_all()[1], film)
        self.assertRaises(ValueError, self.__repo.update, Film(2, "title", "des", "sort"))

    def test_delete_by_id(self):
        film = Film(1, "title", "des", "sort")
        self.__repo.save(film)
        self.__repo.delete_by_id(1)
        self.assertEqual(len(self.__repo.get_all()), 1)
        self.assertRaises(ValueError, self.__repo.delete_by_id, 2)

    def test_search_by_id(self):
        film = Film(1, "title", "des", "sort")
        self.__repo.save(film)
        self.assertEqual(self.__repo.search_by_id(1), film)
        self.assertRaises(ValueError, self.__repo.search_by_id, 2)

    def test_get_all(self):
        film = Film(1, "title", "des", "sort")
        self.__repo.save(film)
        self.assertEqual(self.__repo.get_all()[1], film)
