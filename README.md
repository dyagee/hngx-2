# hngx-2

This repo is for the 2023 ``HNGX internship`` stage 2 API project.

**The REST API** is  capable of CRUD operations on a "person" resource, interfacing with ``Mongodb`` database. The API can dynamically handle parameters, such as adding or retrieving a person by name


--- 

Check  `openapi` docs on all the available endpoints  [here.](https://hngx-2-alpha.vercel.app/documentation)

You can also check  the  `postman` documentation  [here.](https://documenter.getpostman.com/view/27619807/2s9YC4VYjc)

--- 


## Created with:

![Framework](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)  

![Database](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)


![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFD43B)


## Also tested with: 

![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)


---

## Usage/Examples

```python
import requests
import json


def formatted_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

city = input("Enter city: ")
price = input("Enter price: ")
url = f"https://hngx-2-alpha.vercel.app/api/d13b7e876571"

response = requests.get(f"{url}")
if response.status_code == 200:
    print("sucessfully fetched the data")
    formatted_print(response.json())
else:
    print(f"There's a {response.status_code} error with your request")

```  

Code Editor Preferred: 

![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white) 

---





## API Reference

## Adding a new person:

Make a POST request with person's name as body data, the API auto-generates a unique `uuid` for each new person 

**Usage:** 

```http
curl -X 'POST' \
  'https://hngx-2-alpha.vercel.app/api' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Mark Essein"
}'
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. *name of user to be created* |



  
  **Response Body:**

  {
  "data": [
    {
      "id": "d13b7e876571",
      "name": "Mark Essein"
    }
  ],
  "code": 200,
  "message": "user added successfully."
}



## Fetching details of a person:

Send a GET request specifying the user `id` in order to fetch the user details

**Usage:**


```http
curl -X 'GET' \
  'https://hngx-2-alpha.vercel.app/api/d13b7e876571' \
  -H 'accept: application/json'
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. *Id of user to fetch* |


**Response Body:**

{
  "data": [
    {
      "id": "d13b7e876571",
      "name": "Mark Essein"
    }
  ],
  "code": 200,
  "message": "user data retrieved successfully"
}



## Modifying details of an existing person:

Create a PUT request to API along with the user's unique `ID` and the `name` to update.

**Usage:**

```http
curl -X 'PUT' \
  'https://hngx-2-alpha.vercel.app/api/d13b7e876571' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "John Cruise Essein"
}'
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. *Id of user to update*|
| `new_name` | `string` | **Required**. *The updated name *|


**Response Body:**

{
  "data": [
    "user with ID: d13b7e876571 update is successful"
  ],
  "code": 200,
  "message": "user name updated successfully"
}



## Deleting a person:

Create a DELETE request with the user's `ID` a parameter to permanently delete the user from the `database`.

**Usage:**


```http
curl -X 'DELETE' \
  'https://hngx-2-alpha.vercel.app/api/d13b7e876571' \
  -H 'accept: application/json'
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. *Id of user to delete*|

  
**Response Body:**

{
  "data": [
    "user with ID: d13b7e876571 removed"
  ],
  "code": 200,
  "message": "user deleted successfully"
}



---


## Roadmap

- Add more fields

- Include Auth token system

- Deploy v2 to alternative cloud platform



## Feedback

If you have any feedback, please reach out to us at ageeaondo45@gmail.com

---

## Acknowledgements

 - [FastAPI websie ](https://fastapi.tiangolo.com/tutorial)
 
