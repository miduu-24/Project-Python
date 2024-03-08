from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository
from ro.ubb.filmapp.service.service_clients import ClientService


def test_add_client_service():
    client_repository = ClientsRepository()
    client_service = ClientService(client_repository)

    client_service.add_c(1, "ana", 1)

    clients = client_service.getAllClients()
    assert len(clients) == 1
    assert clients[0].get_id() == 1


def test_update_client_service():
    client_repository = ClientsRepository()
    client_service = ClientService(client_repository)

    client_service.add_c(1, 1, 1)
    client_service.update(1, "ana", 1)

    clients = client_service.getAllClients()
    assert clients[0].get_name() == "ana"


def test_delete_client_service():
    client_repository = ClientsRepository()
    client_service = ClientService(client_repository)

    client_service.add_c(1, "ana", 1)
    client_service.delete_c(1)

    clients = client_service.getAllClients()
    assert len(clients) == 0


def test_search_client_repository():
    client_repository = ClientsRepository()
    client_service = ClientService(client_repository)

    client_service.add_c(1, "ana", 1)
    assert client_service.search_c(1).get_id() == 1