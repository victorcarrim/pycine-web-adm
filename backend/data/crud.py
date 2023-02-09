from sqlalchemy.orm import Session
from models import models
from data import schemas


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, id_user: int):
    db.query(models.User).filter(models.User.id == id_user).delete()
    db.commit()
    return


def update_user(db: Session, user: schemas.UserCreate, user_id):
    db.query(models.User).filter(models.User.id == user_id).update(user.dict())
    db.commit()
    return


def get_user(db: Session, id_user: int):
    return db.query(models.User).filter(models.User.id == id_user).first()


def save_movie_user(db: Session, movie_id: int, user_id: int):
    db_movie = models.Movie(movie_id=movie_id, owner_id=user_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movies_user(db: Session, id_user: int):
    return db.query(models.Movie).filter(models.Movie.owner_id == id_user).all()


def delete_movie(db: Session, movie_id: int):
    db.query(models.Movie).filter(models.Movie.id == movie_id).delete()
    db.commit()
    return
