from Profiles.Profile import Profile

class GameData:
    def __init__(self) -> None:
        self.__profile: Profile = None
        self.__level: int = None
        self.__score: int = None
        self.__enemys_destroied: int = None
        self.__ship_life: int = None

    def set_enemys_destroied(self, num: int) -> None:
        self.__enemys_destroied = num

    def set_profile(self, profile: Profile) -> None:
        self.__profile = profile

    def set_level(self, level: int) -> None:
        self.__level = level

    def set_score(self, score: int) -> None:
        self.__score = score

    def set_ship_life(self, life: int) -> None:
        self.__ship_life = life

    @property
    def profile(self) -> Profile:
        return self.__profile

    @property
    def enemys_destroied(self) -> int:
        return self.__enemys_destroied

    @property
    def level(self) -> int:
        return self.__level

    @property
    def score(self) -> int:
        return self.__score

    @property 
    def ship_life(self):
        return self.__ship_life
        