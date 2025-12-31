from contextlib import contextmanager
from pymongo import MongoClient
from pymongo.errors import (
    ServerSelectionTimeoutError,
    ConnectionFailure,
    PyMongoError,
)

class MongoConnectionError(RuntimeError):
    """Raised when MongoDB connection fails."""


class MongoOperationError(RuntimeError):
    """Raised when a MongoDB operation fails."""


class MongoConnector:
    def __init__(self, hostname, port, database):
        self.database = database

        try:
            self.client = MongoClient(
                hostname,
                port,
                serverSelectionTimeoutMS=3000
            )

            self.client.admin.command("ping")

        except (ServerSelectionTimeoutError, ConnectionFailure) as e:
            raise MongoConnectionError(
                f"Cannot connect to MongoDB at {hostname}:{port}"
            ) from e

        except PyMongoError as e:
            raise MongoConnectionError(
                "Unexpected MongoDB error during connection"
            ) from e
        

    @contextmanager
    def get_connector(self):
        try:
            yield self.client[self.database]

        except PyMongoError as e:

            raise MongoOperationError(
                f"MongoDB operation failed: {e}"
            ) from e

    def close(self):
        self.client.close()