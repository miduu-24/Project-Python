from dataclasses import dataclass


@dataclass
class RentDto:
    name_client: str
    nr_film: int


class RentDTOAssembler:
    @staticmethod
    def create_rent_dto(client, films):
        name_client = client.get_name()
        nr_film = len(films)
        return RentDto(name_client, nr_film)
