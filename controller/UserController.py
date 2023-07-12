from fastapi import \
    APIRouter

from database.user_operations import *

router = APIRouter(prefix="/user",
                   tags=["user"],
                   responses={404: {"description": "Not found"}})


@router.get("/all-user-data")
def fetchAllUsers():
    return fetch_all_user_data()


@router.get("/find-one/{userid}")
def fetch_one_user(userid: str):
    return fetch_one_user_data(userid)


@router.put("/update/{user_id}")
def update_user(user_id: int, user: User):
    return update_user_data(user_id, user)


@router.post("/add-user")
def add_user(user: User):
    return add_user_data(user)


@router.delete("/delete/{user_id}")
def delete_user(user_id: int):
    return delete_user_data(user_id)
