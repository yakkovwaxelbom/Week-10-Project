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



# if __name__ == "__main__":

#     import uvicorn

#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
