from mysql.connector import pooling, Error
from contextlib import contextmanager



class MySqlConnector:
    
    def __init__(self, config, pool_name, pull_size):

        try:
            self.connection_pool = pooling.MySQLConnectionPool(
                pool_name=pool_name,  
                pool_size=pull_size,         
                pool_reset_session=True,
                **config           
            )
            print('MySQL connected')

        except Error as e:
            raise ConnectionError(f"MySQL connection failed: {e}")


    @contextmanager
    def get_cursor(self):
        connection = None
        cursor = None

        try:
            connection = self.connection_pool.get_connection()
            cursor = connection.cursor(dictionary=True)
            yield cursor
            connection.commit()
        except Exception as e:
            if connection:
                connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def close(self):
        self.connection_pool =  None
        print('MySQL connection closed')
