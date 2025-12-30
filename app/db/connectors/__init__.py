from importlib import import_module
import os

def get_connector():

    db_type = os.getenv('DB_TYPE')

    if db_type == "mysql":

        db_config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME'),
            'port': int(os.getenv('DB_PORT'))
        }

        connector_module = import_module("db.connectors.mysql")
        connector = connector_module.MySqlConnector(db_config, pool_name='', pull_size=5
        )

    elif db_type == "mongo":

        host = os.getenv('DB_HOST')
        port = int(os.getenv('DB_PORT'))
        database = os.getenv('DB_NAME')

        connector_module = import_module("db.connectors.mongo")
        connector = connector_module.MongoConnector(host, port, database)

    else:
        raise ValueError(f"Unsupported DB_TYPE: {db_type}")

    return connector