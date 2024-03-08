class Film:
    def __init__(self, id, title, des, sort):
        self.__id = id
        self.__title = title
        self.__des = des
        self.__sort = sort

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_des(self):
        return self.__des

    def get_sort(self):
        return self.__sort

    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def set_des(self, des):
        self.__des = des

    def set_sort(self, sort):
        self.__sort = sort

    def __str__(self):
        return "Film:\n\tId: " + str(self.__id) \
               + "\n\tTitle: " + str(self.__title) \
               + "\n\tDescription: " + str(self.__des) \
               + "\n\tSort:  " + str(self.__sort)

    def as_dict(self):
        """
        Returns a dictionary representation of the object
        :return: dict
        """
        return {"id": self.__id,
                "title": self.__title,
                "des": self.__des,
                "sort": self.__sort
                }


class Client:
    def __init__(self, id, name, cnp):
        self.__id = id
        self.__name = name
        self.__cnp = cnp

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_cnp(self):
        return self.__cnp

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def __str__(self):
        return "Client:\n\tId: " + str(self.__id) \
               + "\n\tName: " + str(self.__name) \
               + "\n\tCNP: " + str(self.__cnp)

    def as_dict(self):
        """
        Returns a dictionary representation of the object
        :return: dict
        """
        return {"id": self.__id,
                "name": self.__name,
                "cnp": self.__cnp,
                }
