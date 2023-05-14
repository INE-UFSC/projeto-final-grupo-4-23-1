class ResultData:
    def __init__(self) -> None:
        self.__alive_time = 0
        self.__score = 0
        
    def get_alive_time(self):
        return self.__alive_time

    def set_alive_time(self, v):
        self.__alive_time = v
    
    def reset_alive_time(self):
        self.__alive_time = 0
    
    def get_score(self):
        return self.__score
    
    def set_score(self, v):
        self.__score = v