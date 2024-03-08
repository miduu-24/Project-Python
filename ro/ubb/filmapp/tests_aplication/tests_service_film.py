from ro.ubb.filmapp.repository.reposity_films import FilmsRepository
from ro.ubb.filmapp.service.service_films import FilmService


def test_add_film_service():
    film_repository = FilmsRepository()
    film_service = FilmService(film_repository)

    film_service.add_f(1, 1, 1, 1)

    films = film_service.getAllFilms()
    assert len(films) == 1
    assert films[0].get_id() == 1


def test_update_film_service():
    film_repository = FilmsRepository()
    film_service = FilmService(film_repository)

    film_service.add_f(1, 1, 1, 1)
    film_service.update_f(1, 2, 2, 2)

    films = film_service.getAllFilms()
    assert films[0].get_title() == 2


def test_delete_film_service():
    film_repository = FilmsRepository()
    film_service = FilmService(film_repository)

    film_service.add_f(1, 1, 1, 1)
    film_service.delete_f(1)

    films = film_service.getAllFilms()
    assert len(films) == 0


def test_search_film_service():
    film_repository = FilmsRepository()
    film_service = FilmService(film_repository)

    film_service.add_f(1, 1, 1, 1)

    films = film_service.getAllFilms()
    assert film_repository.search_by_id(1).get_id() == 1
