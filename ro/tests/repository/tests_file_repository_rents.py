import unittest
from unittest.mock import patch, mock_open
from ro.ubb.filmapp.domain.entities import Film, Client
from ro.ubb.filmapp.repository.files_repository_rents import RentFilms
from ro.ubb.filmapp.repository.files_repository_films import FilmsRepository
from ro.ubb.filmapp.repository.files_repository_clients import ClientsRepository


class Test_Rents_Repository(unittest.TestCase):
    def setUp(self):
        with patch("builtins.open", mock_open(read_data="{}")):
            self.rent = RentFilms()
        with patch("builtins.open", mock_open(read_data="[]")):
            self.film = FilmsRepository()
        with patch("builtins.open", mock_open(read_data="[]")):
            self.client = ClientsRepository()
        self.film_1 = Film(1, "Film1", "Comedy", "2010")
        self.film.save(self.film_1)
        self.film_2 = Film(1, "Film1", "Drama", "2011")
        self.film.save(self.film_2)
        self.client_1 = Client(1, "Client1", 1)
        self.client.save(self.client_1)

    def test_rent(self):
        self.rent.rent(self.film_1, self.client_1)
        self.assertEqual(len(self.rent.get_val()), 1)

    def test_return(self):
        self.rent.rent(self.film_1, self.client_1)
        self.rent.returned(self.film_1, self.client_1)
        self.assertEqual(len(self.rent.get_val()), 0)
        self.assertRaises(ValueError, self.rent.returned, self.film_2, self.client_1)

    def test_all_films(self):
        self.rent.rent(self.film_1, self.client_1)
        self.rent.rent(self.film_2, self.client_1)
        self.assertEqual(self.rent.all_films(), ["Film1"])

    def test_return_films_and_clients(self):
        self.rent.rent(self.film_1, self.client_1)
        self.assertEqual(self.rent.return_films_and_clients(), (["Film1"], ["Client1"]))