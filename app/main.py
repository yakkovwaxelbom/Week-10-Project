from fastapi import FastAPI
from dotenv import load_dotenv


from routes import connection
from db.manager import DBManager


app = FastAPI()

app.include_router(connection.router)

@app.on_event('startup')
def event_startup():
    load_dotenv()
    DBManager.init_db()



if __name__ == "__main__":

    import uvicorn


    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)




# db = DBManager()

# u1 = UserIn(
#     first_name='1',
#     last_name='1',
#     phone_number='38'
# )

# u2 = UserIn(
#     first_name='1',
#     last_name='1',
#     phone_number='324353545'
# )
# print(type(db.repositories))
# db.repositories.users.create(u1)
# all = db.repositories.users.get_all()

# print(all[-1])
# db.repositories.users.update(all[-1].id, u2)
# all = db.repositories.users.get_all()
# print(all[-1])

# res = db.repositories.users.delete(all[-1].id)
# print(res)
# db.repositories.users.delete('100')


# from fastapi import FastAPI
# import uvicorn

# from routes import connection
# from db.base import BaseDB

# app = FastAPI()

# app.include_router(connection.router)

# db = BaseDB('')

# @app.on_event("startup")
# def on_startup():
#     db.init_db()


# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)