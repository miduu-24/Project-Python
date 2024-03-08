from ro.ubb.filmapp.tests_aplication.tests_repository_client import test_add_client_repository, test_update_client_repository, \
    test_delete_client_repository, test_search_client_repository
from ro.ubb.filmapp.tests_aplication.tests_repository_film import test_add_film_repository, test_update_film_repository, \
    test_delete_film_repository, test_search_film_repository
from ro.ubb.filmapp.tests_aplication.tests_repository_rent import test_rent_rent_repository, test_return_rent_repository, \
    test_return_films_and_clients, test_all_films
from ro.ubb.filmapp.tests_aplication.tests_service_client import test_add_client_service, test_update_client_service, \
    test_delete_client_service, test_search_client_repository
from ro.ubb.filmapp.tests_aplication.tests_service_film import test_add_film_service, test_update_film_service, \
    test_delete_film_service, test_search_film_service
from ro.ubb.filmapp.tests_aplication.tests_service_rent import test_rent_rent_service, test_return_rent_service, \
    test_alphabetic_clients, test_number_films, test_popular_films, test_clients_30


def test_all():
    test_add_client_repository()
    test_update_client_repository()
    test_delete_client_repository()
    test_search_client_repository()

    test_add_film_repository()
    test_update_film_repository()
    test_delete_film_repository()
    test_search_film_repository()

    test_rent_rent_repository()
    test_return_rent_repository()
    test_return_films_and_clients()
    test_all_films()

    test_add_client_service()
    test_update_client_service()
    test_delete_client_service()
    test_search_client_repository()

    test_add_film_service()
    test_update_film_service()
    test_delete_film_service()
    test_search_film_service()

    test_rent_rent_service()
    test_return_rent_service()
    test_alphabetic_clients()
    test_number_films()
    test_popular_films()
    test_clients_30()
