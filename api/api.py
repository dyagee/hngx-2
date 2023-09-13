#author: Agee Aondo
#Year: 2023
#import all the upduired modules

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
#from fastapi.encoders import jsonable_encoder
from api.crud import*
from api.docs import (summary,description,title, version,contact,docs)
from api.models import ResponseModel,User,UpdateUser


app = FastAPI(title=title,summary=summary,docs_url=docs,version=version,contact=contact,description=description)


@app.post("/api", response_description="user data added into the database")
def add_user_data(user:User):
    person = user.model_dump(exclude_unset=True)
    print(person)
    person = person["name"]
    print(person)

    new_user = add_user(person)
    return ResponseModel(new_user, "user added successfully.")

@app.get("/api/{user_id}", response_description="user data retrieved")
def get_user_data(user_id:str):
    user = retrieve_user(user_id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/{user_id}")
def update_user_data(user_id: str, new_name: UpdateUser ):
    update_info = new_name.model_dump(exclude_unset=True)
    update_info =update_info["name"]
    updated_user =  update_user(user_id, update_info)
    if updated_user:
        return ResponseModel(
            "user with user_ID: {} update is successful".format(user_id),
            "user name updated successfully",
        )
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/{user_id}", response_description="user data deleted from the database")
def delete_user(user_id: str):
    deleted_user =  user_delete(user_id)
    if deleted_user:
        return ResponseModel(
            "user with user_ID: {} removed".format(user_id), "user deleted successfully"
        )
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app")   
    