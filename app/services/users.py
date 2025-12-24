from db.manager import DBManager

class UsersService:

    @staticmethod
    def get_all():
        repo = DBManager.get_repositories()
      
        return repo.users.get_all()
    @staticmethod
    def create(user):
        
        repo = DBManager.get_repositories()
        return repo.users.create(user)

    @staticmethod
    def delete(user_id):

        repo = DBManager.get_repositories()

        count = repo.users.delete(user_id)
        if count == 0:
            raise ValueError("User not found")
        return count

    @staticmethod 
    def update(user_id, user):

        repo = DBManager.get_repositories()

        count = repo.users.update(user_id, user)
        if count == 0:
            raise ValueError("User not found")
        
        return count
    
    
