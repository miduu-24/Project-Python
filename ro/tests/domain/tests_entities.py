import unittest
from ro.ubb.filmapp.domain.entities import Film, Client


class Test_Films(unittest.TestCase):
    def setUp(self) -> None:
        self.film = Film(1, "Titanic", "Film Titanic", "Drama")  # film to be tested

    def test_get_id(self):
        self.assertTrue(self.film.get_id() == 1, "The id of the client should be 1")  # test get_id()

    def test_get_title(self):
        self.assertTrue(self.film.get_title() == "Titanic", "The title of the film should be Titanic")  # test
        # get_title()

    def test_get_des(self):
        self.assertTrue(self.film.get_des() == "Film Titanic", "The description of the film should be Film Titanic")
        # test get_des()

    def test_get_sort(self):
        self.assertTrue(self.film.get_sort() == "Drama", "The sort of the film should be Drama")  # test get_sort()

    def test_set_id(self):
        self.film.set_id(2)
        self.assertTrue(self.film.get_id() == 2, "The id of the film should be 2")

    def test_str(self):
        self.assertTrue(str(self.film) == "Film:\n\tId: 1"
                                          "\n\tTitle: Titanic"
                                          "\n\tDescription: Film Titanic"
                                          "\n\tSort:  Drama",
                        "The string representation of the film should be 'Film:"
                        "\n\tId: 1"
                        "\n\tTitle: Titanic"
                        "\n\tDescription: Film Titanic"
                        "\n\tSort:  Drama'")

    def test_as_dict(self):
        self.assertTrue(self.film.as_dict() == {"id": 1,
                                                "title": "Titanic",
                                                "des": "Film Titanic",
                                                "sort": "Drama"},
                        "The dict representation of the film should be "
                        "{'id': 1, 'title': 'Titanic', 'des': 'Film Titanic', 'sort': 'Drama'}")


class Test_Clients(unittest.TestCase):
    def setUp(self):
        self.client = Client(1, "John", 1)  # client to be tested

    def test_id(self):
        self.assertTrue(self.client.get_id() == 1, "The id of the client should be 1")  # test get_id()

    def test_name(self):
        self.assertTrue(self.client.get_name() == "John", "The name of the client should be John")  # test get_name()

    def test_cnp(self):
        self.assertTrue(self.client.get_cnp() == 1, "The cnp of the client should be 1")  # test get_cnp()

    def test_set_id(self):
        self.client.set_id(2)
        self.assertTrue(self.client.get_id() == 2, "The id of the client should be 2")

    def test_str(self):
        self.assertTrue(str(self.client) == "Client:\n\tId: 1"
                                            "\n\tName: John"
                                            "\n\tCNP: 1",
                        "The string representation of the client should be 'Client:\n\tId: 1\n\tName: John\n\tCNP: 1'")

    def test_as_dict(self):
        self.assertTrue(self.client.as_dict() == {"id": 1, "name": "John", "cnp": 1},
                        "The dict representation of the client should be {'id': 1, 'name': 'John', 'cnp': 1}")