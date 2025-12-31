from bson.objectid import ObjectId


from models.users import UserIn, UserOut


class RepoUserMongo:

    def __init__(self, connector):
        self.connector = connector

        with self.connector.get_connector() as db:
            db.users.create_index("phone_number", unique=True)

        

    def get_all(self):
        with self.connector.get_connector() as db:

            all_rows = db.users.find()

            return [
                    UserOut(
                        id=str(row["_id"]),
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        phone_number=row["phone_number"]
                    )
                    for row in all_rows
                ]

        
    def delete(self, _id):
        with self.connector.get_connector() as db:

            query_filter = {"_id": ObjectId(_id) }

            res = db.users.delete_one(query_filter)
            return res.deleted_count


    def create(self, user :UserIn):
        with self.connector.get_connector() as db:

            res = db.users.insert_one(user.model_dump())
            return str(res.inserted_id)
        

    def update(self, _id, user: UserIn):
        with self.connector.get_connector() as db:
            query = {'_id': ObjectId(_id)}
            values = {"$set": user.model_dump()}

            res = db.users.update_one(query, values)

            return res.modified_count
