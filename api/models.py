from typing import Optional
from pydantic import BaseModel, Field


class User (BaseModel):
    name: str 
    

    class Config:
        json_schema_extra = {
            "example":  {
                "name":"Mark Essein"
                }
            }
        


class UpdateUser(BaseModel):
    name: str
    

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Cruise Essein",
                
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

