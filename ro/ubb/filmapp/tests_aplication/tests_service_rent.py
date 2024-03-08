from ro.ubb.filmapp.repository.reposity_rents import RentFilms
from ro.ubb.filmapp.repository.reposity_films import FilmsRepository
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository
from ro.ubb.filmapp.service.service_films import FilmService
from ro.ubb.filmapp.service.service_clients import ClientService
from ro.ubb.filmapp.service.service_rents import RentService


def test_rent_rent_service():
    rent_res = RentFilms()
    film_res = FilmsRepository()
    client_res = ClientsRepository()
    film_serv = FilmService(film_res)
    client_serv = ClientService(client_res)
    rent_service = RentService(rent_res, film_res, client_res)

    film_serv.add_f(1, 1, 1, 1)
    client_serv.add_c(2, "ana", 1)
    rent_service.add_r(1, 2)

    rents = rent_res.get_val()
    assert len(rents) == 1
    assert rents[0][0] == 1
    assert rents[0][1] == "ana"


def test_return_rent_service():
    rent_res = RentFilms()
    film_res = FilmsRepository()
    client_res = ClientsRepository()
    film_serv = FilmService(film_res)
    client_serv = ClientService(client_res)
    rent_service = RentService(rent_res, film_res, client_res)

    film_serv.add_f(1, 1, 1, 1)
    client_serv.add_c(2, "ana", 1)
    rent_service.add_r(1, 2)
    rent_service.delete_r(1, 2)

    rents = rent_res.get_val()
    assert len(rents) == 0


def test_alphabetic_clients():
    rent_res = RentFilms()
    film_res = FilmsRepository()
    client_res = ClientsRepository()
    film_serv = FilmService(film_res)
    client_serv = ClientService(client_res)
    rent_service = RentService(rent_res, film_res, client_res)

    film_serv.add_f(1, 1, 1, 1)
    client_serv.add_c(2, "ana", 1)
    client_serv.add_c(1, "florin", 2)
    rent_service.add_r(1, 2)
    rent_service.add_r(1, 1)
    list_clients = rent_service.alphabetic_clients()
    assert list_clients == ["ana", "florin"]


def test_number_films():
    rent_res = RentFilms()
    film_res = FilmsRepository()
    client_res = ClientsRepository()
    film_serv = FilmService(film_res)
    client_serv = ClientService(client_res)
    rent_service = RentService(rent_res, film_res, client_res)

    film_serv.add_f(1, 1, 1, 1)
    client_serv.add_c(2, "ana", 1)
    client_serv.add_c(1, "florin", 2)
    rent_service.add_r(1, 2)
    rent_service.add_r(1, 1)
    rent_service.add_r(1, 1)

    list_clients, list_number = rent_service.number_films()
    assert list_clients == ["florin", "ana"]
    assert list_number == [2, 1]


def test_popular_films():
    rent_res = RentFilms()
    film_res = FilmsRepository()
    client_res = ClientsRepository()
    film_serv = FilmService(film_res)
    client_serv = ClientService(client_res)
    rent_service = RentService(rent_res, film_res, client_res)

    film_serv.add_f(1, 1, 1, 1)
    film_serv.add_f(2, 2, 2, 2)
    client_serv.add_c(1, "ana", 1)
    rent_service.add_r(1, 1)
    rent_service.add_r(1, 1)
    rent_service.add_r(2, 1)

    assert rent_service.popular_films() == [1, 2]


def test_clients_30():
    rent_res = RentFilms()
    film_res = FilmsRepository()
    client_res = ClientsRepository()
    film_serv = FilmService(film_res)
    client_serv = ClientService(client_res)
    rent_service = RentService(rent_res, film_res, client_res)

    film_serv.add_f(1, 1, 1, 1)
    client_serv.add_c(1, "ana", 1)
    client_serv.add_c(2, "geo", 2)
    client_serv.add_c(3, "dan", 3)
    client_serv.add_c(4, "paul", 4)
    rent_service.add_r(1, 3)
    rent_service.add_r(1, 1)
    rent_service.add_r(1, 3)
    rent_service.add_r(1, 2)
    rent_service.add_r(1, 4)

    list_clients, list_number = rent_service.clients_30()
    assert list_clients == ["dan"]
