from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    name: str


class MovieModel(BaseModel):
    movie_id: int


class UserCreate(UserModel):
    password: str


class MovieSave(MovieModel):
    pass


class Movie(MovieSave):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class User(UserModel):
    id: int
    is_active: bool
    items: list[Movie] = []

    class Config:
        orm_mode = True
