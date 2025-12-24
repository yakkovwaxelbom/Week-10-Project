from models.users import UserIn, UserOut

class MySqlUserRepo:
    def __init__(self, connector):
        self.__connector = connector

    def create(self, user :UserIn):
        query = "INSERT INTO users (first_name, last_name, phone_number) " \
                    "VALUES (%s, %s, %s);" 
        values = (
                user.first_name,
                user.last_name,
                user.phone_number
            )
        
        with self.__connector.get_cursor() as cursor:
            cursor.execute(query, values)

            return cursor.lastrowid

    
    def get_all(self):
        query = "SELECT * FROM users;" 

        with self.__connector.get_cursor() as cursor:
            cursor.execute(query)

            all_rows = cursor.fetchall()

            return [UserOut(**row) for row in all_rows]
        
    def delete(self, id):
        query = "DELETE FROM users WHERE id = %s;" 

        value = (id,)

        with self.__connector.get_cursor() as cursor:
            cursor.execute(query, value)
            
            return cursor.rowcount


    def update(self, id, user: UserIn):
        query = '''UPDATE users
                SET first_name = %s, last_name = %s, phone_number = %s
                WHERE id = %s;'''

        values = (
                user.first_name,
                user.last_name,
                user.phone_number,
                id
            )
        with self.__connector.get_cursor() as cursor:
            cursor.execute(query, values)

            return cursor.rowcount
        