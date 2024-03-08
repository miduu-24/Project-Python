from ro.ubb.filmapp.ui.console import Console
from ro.ubb.filmapp.service.service_films import FilmService
from ro.ubb.filmapp.service.service_clients import ClientService
from ro.ubb.filmapp.service.service_rents import RentService
from ro.ubb.filmapp.repository.reposity_films import FilmsRepository
from ro.ubb.filmapp.repository.reposity_clients import ClientsRepository
from ro.ubb.filmapp.repository.files_repository_films import FilmsRepository as files_f
from ro.ubb.filmapp.repository.files_repository_clients import ClientsRepository as files_c
from ro.ubb.filmapp.repository.files_repository_rents import RentFilms as files_r
from ro.ubb.filmapp.repository.reposity_rents import RentFilms
from ro.ubb.filmapp.tests_aplication.tests_all import test_all
from ro.ubb.filmapp.service.raports_service import RapportsService


def main():
    test_all()
    print("1. In memory")
    print("2. Files")
    option = int(input("Option: "))

    if option == 1:  # in memory
        films_repos, clients_repos, rents_repos = FilmsRepository(), ClientsRepository(), RentFilms()
        film_serv, client_serv, rent_serv, rapports_serv = FilmService(films_repos), ClientService(clients_repos), \
            RentService(rents_repos, films_repos, clients_repos), RapportsService()

        console = Console(film_serv, client_serv, rent_serv, rapports_serv)
        console.menu_main()

    elif option == 2:  # files
        films_repos, clients_repos, rents_repos = files_f(), files_c(), files_r()
        film_serv, client_serv, rent_serv, rapports_serv = FilmService(films_repos), ClientService(clients_repos), \
            RentService(rents_repos, films_repos, clients_repos), RapportsService()

        console = Console(film_serv, client_serv, rent_serv, rapports_serv)
        console.menu_main()


main()
