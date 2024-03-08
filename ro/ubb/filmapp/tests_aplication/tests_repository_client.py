from ro.ubb.filmapp.domain.entities import Client
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository


def test_add_client_repository():
    client_repository = ClientsRepository()
    client = Client(1, "ana", 1)

    client_repository.save(client)

    clients = client_repository.get_all()
    assert len(clients) == 1
    assert clients[0].get_id() == 1


def test_update_client_repository():
    client_repository = ClientsRepository()
    client = Client(1, 1, 1)
    client_new_1 = Client(1, "ana", 2)

    client_repository.save(client)
    client_repository.update(client_new_1)

    clients = client_repository.get_all()
    assert clients[0].get_name() == "ana"


def test_delete_client_repository():
    client_repository = ClientsRepository()
    client = Client(1, 1, 1)

    client_repository.save(client)
    client_repository.delete_by_id(1)

    clients = client_repository.get_all()
    assert len(clients) == 0


def test_search_client_repository():
    client_repository = ClientsRepository()
    client = Client(1, 1, 1)

    client_repository.save(client)
    assert client_repository.search_by_id(1) == client