from ro.ubb.filmapp.domain.entities import Film, Client
from ro.ubb.filmapp.repository.reposity_rents import RentFilms


def test_rent_rent_repository():
    rent_res = RentFilms()
    client = Client(1, "ana", 1)
    film = Film(1, 1, 1, 1)

    rent_res.rent(film, client)

    rents = rent_res.get_val()
    assert len(rents) == 1
    assert rents[0][0] == 1
    assert rents[0][1] == "ana"


def test_return_rent_repository():
    rent_res = RentFilms()
    client = Client(1, "ana", 1)
    film = Film(1, 1, 1, 1)

    rent_res.rent(film, client)
    rent_res.returned(film, client)

    rents = rent_res.get_val()
    assert len(rents) == 0

def test_return_films_and_clients():
    rent_res = RentFilms()
    client = Client(1, "ana", 1)
    film = Film(1, 1, 1, 1)

    rent_res.rent(film, client)
    films, clients = rent_res.return_films_and_clients()
    assert films == [1]
    assert clients == ["ana"]


def test_all_films():
    rent_res = RentFilms()
    client = Client(1, "ana", 1)
    film = Film(1, 1, 1, 1)
    film_2 = Film(1, 1, 2, 2)

    rent_res.rent(film, client)
    rent_res.rent(film_2, client)

    films = rent_res.all_films()
    assert films == [1]
