from importlib import import_module
from types import SimpleNamespace
import os



def get_repositories(connector):

    repositories = SimpleNamespace()
    db_type = os.getenv('DB_TYPE')

    if db_type == "mysql":
        repositories_module = import_module("db.repositories.mysql.users")
        repositories.users = repositories_module.MySqlUserRepo(connector)

    elif db_type == "mongo":
        repositories_module = import_module("db.repositories.mongo.users")
        repositories.users = repositories_module.RepoUserMongo(connector)

    else:
        raise ValueError(f"Unsupported DB_TYPE: {db_type}")

    return repositories
