from typing import Union
from pydantic import BaseModel

from database.mysql import _mysql_local_connection, _fetch_all, _fetch_one, _update_data, _delete_data, _insert_data

user_select_script = "SELECT * FROM ngta.user"
user_select_id_script = user_select_script +" WHERE id = {id}"
user_update_script = "UPDATE ngta.user SET user_name={uname}, user_email={uemail}, age={age}, active={active} where id={id}"
delete_user_script = "DELETE FROM ngta.user WHERE id={id}"
insert_user_script = "INSERT INTO ngta.user values({user_name},{user_email}, {age},{active}"


class User(BaseModel):
    name: str
    id: int
    active: Union[bool, None] = None
    age: int
    email: str


def fetch_all_user_data():
    connection = _mysql_local_connection()
    return _fetch_all(connection, user_select_script)


def fetch_one_user_data(user_id: int):
    connection = _mysql_local_connection()
    formatted_script = user_select_id_script.format(id= user_id)

    print(formatted_script)
    return _fetch_one(connection, formatted_script)


def update_user_data(user_id: int, user: User):
    connection = _mysql_local_connection()
    user_data = _fetch_one(connection, user_select_id_script.format(id=user_id))
    if user_data is None:
        raise ValueError('user not found update process will not be proceed')

    formatted_update_script = user_update_script.format(uname=user.name, uemail=user.email, age=user.age,
                                                        active=user.active, id=user_data.id)
    affected_row = _update_data(connection, formatted_update_script)
    return affected_row


def delete_user_data(userid):
    connection = _mysql_local_connection()
    affected_rows = _delete_data(connection, delete_user_script.format(id=userid))
    return affected_rows

def add_user_data(user: User):
    connection = _mysql_local_connection()
    affected_rows = _insert_data(connection,
                                 insert_user_script.format(user_name=user.name, user_email=user.email, age=user.age,
                                                           active=user.active))
    return affected_rows
