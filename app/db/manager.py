from db.connectors import get_connector
from db.repositories import get_repositories

class DBManager:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        self.__connector = get_connector()
        self.repositories = get_repositories(self.__connector) 

    
    @staticmethod
    def get_repositories():
        return DBManager.__instance.repositories
    
    @staticmethod
    def init_db():
        DBManager()

        
    def close(self):
        self.__connector.close()


