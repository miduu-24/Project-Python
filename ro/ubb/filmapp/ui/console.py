from ro.ubb.filmapp.service.service_films import FilmService
from ro.ubb.filmapp.service.service_clients import ClientService
from ro.ubb.filmapp.service.service_rents import RentService
from ro.ubb.filmapp import Util
import random


def print_menu_main():
    """
    Prints the application menu
    :return: None
    """
    # the menu with the requests that the code can make
    print('\nSections:')
    print("\t1. Films")
    print("\t2. Clients")
    print("\t3. Rents")
    print("\t4. Rapports dto")
    print("\t5. Exit")


def print_menu_films():
    """
    Prints the film menu
    :return: None
    """
    # the menu with the requests that the code can make
    print("\nFilms Subsections:")
    print("\t1. Add")
    print("\t2. Update")
    print("\t3. Delete")
    print("\t4. Search")
    print("\t5. Print")
    print("\t6. Exit")


def print_menu_client():
    """
    Prints the client menu
    :return: None
    """
    # the menu with the requests that the code can make
    print("\nClients Subsections:")
    print("\t1. Add")
    print("\t2. Update")
    print("\t3. Delete")
    print("\t4. Search")
    print("\t5. Print")
    print("\t6. Exit")


def print_menu_rent():
    """
    Prints the rent menu
    :return: None
    """
    # the menu with the requests that the code can make
    print("\nRents Subsection:")
    print("\t1. Rent")
    print("\t2. Returned")
    print("\t3. Rapports")
    print("\t4. Print")
    print("\t5. Exit")


def print_menu_rapports():
    """
    Prints the rapport menu
    :return: None
    """
    # the menu with the requests that the code can make
    print("\nRapports Subsection:")
    print("\t1. Customers with rented movies sorted by name")
    print("\t2. Customers with rented movies ordered by the number of rented movies")
    print("\t3. The most rented movies.")
    print("\t4. 30% customers with most movies rented")
    print("\t5. Exit")


def print_menu_rapports_dto():
    print("\nRapports Subsection:")
    print("\t1. Customers with rented movies sorted by name")
    print("\t2. Customers with rented movies ordered by the number of rented movies")
    print("\t3. Exit")


class Console:
    def __init__(self, film_serv: FilmService, client_serv: ClientService, rent_serv: RentService, rapports_serv):
        self.__film_serv = film_serv
        self.__client_serv = client_serv
        self.__rent_serv = rent_serv
        self.__rapports_serv = rapports_serv

    def menu_main(self):
        """
            Runs the application menu
            :return: None
            """
        section = {
            1: self.opt_films,
            2: self.opt_clients,
            3: self.opt_rents,
            4: self.opt_rapports_dto,
            5: exit  # exit the program
        }

        while True:
            print_menu_main()
            option = Util.read_int("Option: ")
            try:
                section[option]()
            except KeyError as ke:
                print("\n This option is not yet input", ke, "\n")

    # ------------------ films menu ------------------

    def opt_films(self):
        """
        Runs the film menu
        :return: None
        """
        subsection = {
            1: self.ui_add_f,
            2: self.ui_update_f,
            3: self.ui_delete_f,
            4: self.ui_search_f,
            5: self.ui_print_f
        }
        print_menu_films()
        while True:
            option = Util.read_int("Films Option: ")
            print(" ")
            try:
                if option == 6:
                    break # exit the subsection, return to the main menu
                subsection[option]()
            except KeyError as ke:
                print("\n This option is not yet input: ", ke, "\n")
            except ValueError as val:
                print(val)

    def ui_add_f(self):
        """
        Adds a film - interface
        :return: None
        """
        id = str(random.randrange(0, 100)) # generate a random id
        title = input("Film's title: ")
        des = input("Film's description: ")
        sort = input("Film's type: ")
        self.__film_serv.add_f(id, title, des, sort)
        print(" ")

    def ui_update_f(self):
        """
        Updates a film - interface
        :return: None
        """
        id = input("Id: ")
        new_title = input("New Film's title: ")
        new_des = input("New Film's description: ")
        new_sort = input("New Film's type: ")
        print(self.__film_serv.update_f(id, new_title, new_des, new_sort))
        print(" ")

    def ui_delete_f(self):
        """
        Deletes a film - interface
        :return: None
        """
        id = input("Id: ")
        print(self.__film_serv.delete_f(id))
        print(" ")

    def ui_search_f(self):
        """
        Searches a film - interface
        :return: None
        """
        id = input("Id: ")
        print(self.__film_serv.search_f(id))
        print(" ")

    def ui_print_f(self):
        """
        Prints all the films - interface
        :return: None
        """
        print(*self.__film_serv.getAllFilms(), sep="\n")
        print(" ")

    # ------------------ clients menu ------------------
    def opt_clients(self):
        """
        Runs the client menu
        :return: None
        """
        subsection = {
            1: self.ui_add_c,
            2: self.ui_update_c,
            3: self.ui_delete_c,
            4: self.ui_search_c,
            5: self.ui_print_c
        }
        print_menu_client()
        while True:
            option = Util.read_int("Clients Option: ")
            print(" ")
            try:
                if option == 6:
                    break # exit the subsection, return to the main menu
                subsection[option]()
            except KeyError as ke:
                print("\n This option is not yet input: ", ke, "\n")
            except ValueError as val:
                print(val)

    def ui_add_c(self):
        """
        Adds a client - interface
        :return: None
        """
        id = str(random.randrange(0, 100)) # generate a random id
        name = input("Client's name: ")
        cnp = Util.cnp("Client's cnp: ")
        self.__client_serv.add_c(id, name, cnp)
        print(" ")

    def ui_update_c(self):
        """
        Updates a client - interface
        :return: None
        """
        id = input("Id: ")
        new_name = input("New Client's name: ")
        new_cnp = Util.cnp("New Client's cnp: ")
        print(self.__client_serv.update(id, new_name, new_cnp))
        print(" ")

    def ui_delete_c(self):
        """
        Deletes a client - interface
        :return: None
        """
        id = input("Id: ")
        print(self.__client_serv.delete_c(id))
        print(" ")

    def ui_search_c(self):
        """
        Searches a client - interface
        :return: None
        """
        id = input("Id: ")
        print(self.__client_serv.search_c(id))
        print(" ")

    def ui_print_c(self):
        """
        Prints all the clients - interface
        :return: None
        """
        print(*self.__client_serv.getAllClients(), sep="\n")
        print(" ")

    # ------------------ rents menu --------------------
    def opt_rents(self):
        """
        Runs the rent menu
        :return: None
        """
        subsection = {
            1: self.ui_add_r,
            2: self.ui_delete_r,
            3: self.ui_rapports,
            4: self.ui_print_r,
        }
        print_menu_rent()
        while True:
            option = Util.read_int("Rents Option: ")
            print(" ")
            try:
                if option == 5:
                    break # exit the subsection, return to the main menu
                subsection[option]()
            except KeyError as ke:
                print("\n This option is not yet input: ", ke, "\n")
            except ValueError as val:
                print(val)

    def ui_add_r(self):
        """
        Adds a rent - interface
        :return: None
        """
        id_f = input("Film's id: ")
        id_c = input("Client's id: ")
        x = self.__rent_serv.f_c_in_list(id_f, id_c) # checks if the film and client are in the list
        if x == "Done!":
            self.__rent_serv.add_r(id_f, id_c)
            print(x)
        else:
            print(x)
        print(" ")

    def ui_delete_r(self):
        """
        Deletes a rent - interface
        :return: None
        """
        id_f = input("Film's id: ")
        id_c = input("Client's id: ")
        x = self.__rent_serv.f_c_in_list(id_f, id_c) # checks if the film and client are in the list
        if x == "Done!":
            print(self.__rent_serv.delete_r(id_f, id_c))
        else:
            print(x)
        print(" ")

    def ui_rapports(self):
        """
        Prints the rapports - interface
        :return: None
        """
        subsection = {
            1: self.ui_sort_alphabetic,
            2: self.ui_sort_number,
            3: self.ui_most_popular_films,
            4: self.ui_30_clients,
        }
        while True:
            print_menu_rapports()
            option = Util.read_int("Rapports Option: ")
            print(" ")
            try:
                if option == 5:
                    break # back to the rent menu
                subsection[option]()
            except KeyError as ke:
                print("\n This option is not yet input: ", ke, "\n")
            except ValueError as val:
                print(val)

    def ui_sort_alphabetic(self):
        """
        Prints the clients sorted alphabetically - interface
        :return: None
        """
        print(*self.__rent_serv.alphabetic_clients(), sep=" ")
        print(" ")

    def ui_sort_number(self):
        """
        Prints the clients sorted by the number of rented films - interface
        :return: None
        """
        client_list, useless = self.__rent_serv.number_films()
        print(*client_list, sep=" ")
        print(" ")

    def ui_most_popular_films(self):
        """
        Prints the most popular films - interface
        :return: None
        """
        print(*self.__rent_serv.popular_films(), sep=" ")
        print(" ")

    def ui_30_clients(self):
        """
        Prints 30% of the clients with the most rented films - interface
        :return: None
        """
        client_list, number_film = self.__rent_serv.clients_30()
        if not client_list:
            print("There are not enough customers. ") # if there are not enough clients
        else:
            for i in range(len(client_list)):
                client = client_list[i]
                number = number_film[i]
                print(client, "rent ", number, "films")

    def ui_print_r(self):
        """
        Prints all the rents - interface
        :return: None
        """
        for elements in self.__rent_serv.getAllRents():
            print(*elements, sep=" rent by: ")
        print(" ")

    # ------------------ rapports menu --------------------
    def opt_rapports_dto(self):
        subsection = {
            1: self.ui_sort_alphabetic_dto,
            2: self.ui_sort_number_dto,
        }
        while True:
            print_menu_rapports_dto()
            option = Util.read_int("Rapports Option: ")
            print(" ")
            try:
                if option == 3:
                    break # back to the main menu
                subsection[option]()
            except KeyError as ke:
                print("\n This option is not yet input: ", ke, "\n")
            except ValueError as val:
                print(val)

    def ui_sort_alphabetic_dto(self):
        """
        Prints the clients sorted alphabetically - interface
        :return: None
        """
        print(*self.__rapports_serv.alphabetic_clients(), sep=" ")

    def ui_sort_number_dto(self):
        """
        Prints the clients sorted by the number of rented films - interface
        :return: None
        """
        print(*self.__rapports_serv.number_films(), sep=" ")