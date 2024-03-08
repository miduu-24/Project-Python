import unittest
from ro.ubb.filmapp.domain.entities import Film
from ro.ubb.filmapp.repository.reposity_films import FilmsRepository


class Test_Films_Repository(unittest.TestCase):
    def setUp(self) -> None:
        self.film_1 = Film(1, "Titanic", "Film Titanic", "Drama")
        self.film_2 = Film(1, "Despicable Me", "Film Despicable Me", "Comedy")
        self.film_3 = Film(2, "The Lion King", "Film The Lion King", "Drama")
        self.film_repository = FilmsRepository()

    def test_find_film_repository(self):
        self.film_repository.save(self.film_1)
        assert self.film_repository.find_by_id(1) == self.film_1
        assert self.film_repository.find_by_id(2) is None

    def test_add_film_repository(self):
        self.film_repository.save(self.film_1)
        films = self.film_repository.get_all()
        assert len(films) == 1
        assert films[0].get_id() == 1

    def test_update_film_repository(self):
        self.film_repository.save(self.film_1)
        self.film_repository.update(self.film_2)
        films = self.film_repository.get_all()
        assert films[0].get_title() == "Despicable Me"

        self.assertRaises(ValueError, self.film_repository.update, self.film_3)

    def test_delete_film_repository(self):
        self.film_repository.save(self.film_1)
        self.film_repository.delete_by_id(1)
        films = self.film_repository.get_all()
        assert len(films) == 0
        self.assertRaises(ValueError, self.film_repository.delete_by_id, 1)

    def test_search_film_repository(self):
        self.film_repository.save(self.film_1)
        assert self.film_repository.search_by_id(1) == self.film_1
        self.assertRaises(ValueError, self.film_repository.search_by_id, 2)