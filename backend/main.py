from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from flask import Response
from starlette import status

from controller.Controller import Controller
from data.schemas import UserCreate, MovieSave
from data.database import SessionLocal, engine
from sqlalchemy.orm import Session
from data import crud
from models import models

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def hello():
    return {"message": "Seja bem vindo"}


@app.get("/person/{person}")
async def get_person(person: str):
    person_information = Controller.get_person(person)
    if person_information is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return person_information


@app.post("/user/create", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Email already registered"
        )
    new_user = crud.create_user(db=db, user=user)
    return new_user


@app.get("/user/getall")
def get_all_user(db: Session = Depends(get_db)):
    db_user = crud.get_users(db)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Users not foud"
        )
    return db_user


@app.get("/user/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id_user=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@app.get("/user/{email_user}")
def read_user_by_email(email_user: str, db: Session = Depends(get_db)):
    # print(user_id)
    db_user = crud.get_user_by_email(db, email=email_user)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@app.delete("/user/{id_user}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id_user: int, db: Session = Depends(get_db)):
    user_data = crud.get_user(db, id_user=id_user)
    if user_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'delete with id: {id_user} does not exist')
    crud.delete_user(db, id_user=id_user)
    return Response(status=status.HTTP_204_NO_CONTENT)


@app.put("/user/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    user_data = crud.get_user(db, id_user=user_id)
    if user_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'delete with id: {user_id} does not exist')
    crud.update_user(db, user=user, user_id=user_id)

    return crud.get_user(db, id_user=user_id)


@app.post("/users/{user_id}/{movie_id}")
def create_movie_for_user(
        user_id: int, movie_id: int, db: Session = Depends(get_db)
):
    return crud.save_movie_user(db=db, movie_id=movie_id, user_id=user_id)


@app.get("/movies")
def get_movies():
    movies = Controller.get_popular_movies()
    print(movies)
    return movies


@app.get("/movies/{user_id}")
def read_movies_user(user_id: int, db: Session = Depends(get_db)):
    movies = crud.get_movies_user(db, id_user=user_id)
    return movies


@app.get("/movies/get-movie-by-id/{movie_id}")
def get_movie_by_id(movie_id: int):
    movie = Controller.get_movie_by_id(movie_id)
    return movie


@app.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie_user(movie_id: int, db: Session = Depends(get_db)):
    crud.delete_movie_user(db, movie_id=movie_id)
    return Response(status=status.HTTP_204_NO_CONTENT)

## source env/bin/activate
# uvicorn main:app --reload
