from Profiles.Profile import Profile

class GameData:
    def __init__(self) -> None:
        self.__profile: Profile = None
        self.__level: int = None
        self.__score: int = None

    def set_profile(self, profile: Profile) -> None:
        self.__profile = profile

    def set_level(self, level: int) -> None:
        self.__level = level

    def set_score(self, score: int) -> None:
        self.__score = score

    @property
    def profile(self) -> Profile:
        return self.__profile

    @property
    def level(self) -> int:
        return self.__level

    @property
    def score(self) -> int:
        return self.__score

    