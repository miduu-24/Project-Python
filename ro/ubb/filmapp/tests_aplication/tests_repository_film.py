from ro.ubb.filmapp.domain.entities import Film
from ro.ubb.filmapp.repository.reposity_films import FilmsRepository


def test_add_film_repository():
    film_repository = FilmsRepository()
    film = Film(1, 1, 1, 1)

    film_repository.save(film)

    films = film_repository.get_all()
    assert len(films) == 1
    assert films[0].get_id() == 1


def test_update_film_repository():
    film_repository = FilmsRepository()
    film = Film(1, 1, 1, 1)
    film_new_1 = Film(1, "ana", 2, 2)

    film_repository.save(film)
    film_repository.update(film_new_1)

    films = film_repository.get_all()
    assert films[0].get_title() == "ana"


def test_delete_film_repository():
    film_repository = FilmsRepository()
    film = Film(1, 1, 1, 1)

    film_repository.save(film)
    film_repository.delete_by_id(1)

    films = film_repository.get_all()
    assert len(films) == 0


def test_search_film_repository():
    film_repository = FilmsRepository()
    film = Film(1, 1, 1, 1)

    film_repository.save(film)
    assert film_repository.search_by_id(1) == film
