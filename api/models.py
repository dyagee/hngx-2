from typing import Optional
from pydantic import BaseModel, Field


class User (BaseModel):
    name: str = Field(...)
    

    class Config:
        json_schema_extra = {
            "example":  {
                "name":"Mark Essein"
                }
            }
        


class UpdateUser(BaseModel):
    name: Optional[str]
    

    class Config:
        json_schema_extra = {
            "example": {
                "edited_name": "John Cruise",
                
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

