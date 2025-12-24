from fastapi import APIRouter, Depends, HTTPException
from typing import List


from models.users import UserIn, UserOut
from services.users import UsersService

router = APIRouter()
service = UsersService()

@router.get('/contacts', response_model=List[UserOut], status_code=200)
def all_users():
    try:
        return service.get_all()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@router.post('/contacts', status_code=201)
def create_user(user: UserIn):
    try:
        user_id = service.create(user)
        return {"msg": "User created successfully", "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@router.put('/contacts/{user_id}', status_code=200)
def update_user(user_id: str, user: UserIn):
    try:
        service.update(user_id, user)
        return {"msg": "User updated successfully", "id": user_id}

    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@router.delete('/contacts/{user_id}', status_code=200)
def delete_user(user_id: str):
    try:
        service.delete(user_id)
        return {"msg": "User deleted successfully", "id": user_id}

    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
