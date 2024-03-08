import unittest
from ro.ubb.filmapp.repository.reposity_rents import RentFilms
from ro.ubb.filmapp.repository.reposity_films import FilmsRepository
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository
from ro.ubb.filmapp.service.service_films import FilmService
from ro.ubb.filmapp.service.service_clients import ClientService
from ro.ubb.filmapp.service.service_rents import RentService


class TestRentService(unittest.TestCase):
    def setUp(self):
        self.rent_res = RentFilms()
        self.film_res = FilmsRepository()
        self.client_res = ClientsRepository()
        self.film_serv = FilmService(self.film_res)
        self.client_serv = ClientService(self.client_res)
        self.rent_service = RentService(self.rent_res, self.film_res, self.client_res)

    def test_f_c_in_list(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.client_serv.add_c(1, "ana", 1)
        self.client_serv.add_c(2, "florin", 2)
        self.assertRaises(ValueError, self.rent_service.f_c_in_list, 1, 3)
        self.assertRaises(ValueError, self.rent_service.f_c_in_list, 2, 1)
        self.assertEqual(self.rent_service.f_c_in_list(1, 1), "Done!")

    def test_rent_rent_service(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.client_serv.add_c(2, "ana", 1)
        self.rent_service.add_r(1, 2)

        rents = self.rent_res.get_val()
        self.assertEqual(len(rents), 1)
        self.assertEqual(rents[0][0], 1)
        self.assertEqual(rents[0][1], "ana")

    def test_return_rent_service(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.client_serv.add_c(2, "ana", 1)
        self.rent_service.add_r(1, 2)
        self.rent_service.delete_r(1, 2)

        rents = self.rent_res.get_val()
        self.assertEqual(len(rents), 0)

    def test_alphabetic_clients(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.client_serv.add_c(2, "ana", 1)
        self.client_serv.add_c(1, "florin", 2)
        self.rent_service.add_r(1, 2)
        self.rent_service.add_r(1, 1)
        list_clients = self.rent_service.alphabetic_clients()
        self.assertEqual(list_clients, ["ana", "florin"])

    def test_number_films(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.client_serv.add_c(2, "ana", 1)
        self.client_serv.add_c(1, "florin", 2)
        self.rent_service.add_r(1, 2)
        self.rent_service.add_r(1, 1)
        list_films = self.rent_service.number_films()
        self.assertEqual(list_films, (["ana", "florin"], [1, 1]))

    def test_popular_films(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.film_serv.add_f(2, 1, 1, 1)
        self.client_serv.add_c(2, "ana", 1)
        self.client_serv.add_c(1, "florin", 2)
        self.rent_service.add_r(1, 2)
        self.rent_service.add_r(1, 1)
        self.rent_service.add_r(2, 1)
        list_films = self.rent_service.popular_films()
        self.assertEqual(list_films, [1])

    def test_clients_30(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.client_serv.add_c(2, "ana", 1)
        self.client_serv.add_c(1, "florin", 2)
        self.client_serv.add_c(3, "maria", 30)
        self.client_serv.add_c(4, "diana", 31)
        self.rent_service.add_r(1, 2)
        self.rent_service.add_r(1, 1)
        self.rent_service.add_r(1, 3)
        self.rent_service.add_r(1, 4)
        list_clients = self.rent_service.clients_30()
        self.assertEqual(list_clients, (["ana"], [1]))

    def test_getAll(self):
        self.film_serv.add_f(1, 1, 1, 1)
        self.client_serv.add_c(2, "ana", 1)
        self.rent_service.add_r(1, 2)
        self.assertEqual(self.rent_service.getAllRents(), [[1, "ana"]])
