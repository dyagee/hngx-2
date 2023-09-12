#author: Agee Aondo
#Year: 2023
#import all the required modules

from markupsafe import escape
from api.database import col
import os

#generate random id_hex
def random_hex_string(length=6):
    return os.urandom(length).hex()


# Add a new user into to the database
def add_user(user_name: str) -> dict:
    id = random_hex_string()
    
    user_data = {
        "id":id,
        "name":escape(user_name)
    }

    user = col.insert_one(user_data)
    new_user = col.find_one({"_id": user.inserted_id},{"_id":False})
    return new_user


# Retrieve a user with a matching ID
def retrieve_user(id: str) -> dict:
    id = escape(id)
    user = col.find_one({"id": id},{"_id":False})
    return user


# Update a user with a matching ID
def update_user(id: str, data: str):
    # Return false if an empty request body is sent.
    if data == "":
        return False
    id = escape(id)
    user = col.find_one({"id":id},{"_id":False})
    if user is not None:
        data = escape(data)
        updated_user = col.update_one(
            {"id": id}, {"$set":{"name":data} }
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
def user_delete(id: str):
    id = escape(id)
    user = col.find_one({"id":id},{"_id":False})
    if user:
        col.delete_one({"id":id})
        return True