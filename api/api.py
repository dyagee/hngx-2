#author: Agee Aondo
#Year: 2023
#import all the upduired modules

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
#from fastapi.encoders import jsonable_encoder
from api.crud import*
from api.docs import (summary,description,title, version,contact,docs)
from api.models import ResponseModel


app = FastAPI(title=title,summary=summary,docs_url=docs,version=version,contact=contact,description=description)


@app.post("/api", response_description="user data added into the database")
def add_user_data(user: str):
    new_user = add_user(user)
    return ResponseModel(new_user, "user added successfully.")

@app.get("/api/{id}", response_description="user data retrieved")
def get_user_data(id:str):
    user = retrieve_user(id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/{id}")
def update_user_data(id: str, new_name: str ):
    #upd = {k: v for k, v in upd.model_dump().items() if v is not None}
    updated_user =  update_user(id, new_name)
    if updated_user:
        return ResponseModel(
            "user with ID: {} update is successful".format(id),
            "user name updated successfully",
        )
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/{id}", response_description="user data deleted from the database")
def delete_user(id: str):
    deleted_user =  user_delete(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app")   
    