title = "HNGX Task2"
summary="The is the documentation for API creation in task2 of HNGX 2023 internship"
version="0.0.1"
docs="/documentation"
contact={
        "Author": "Agee Aondo",
        "url": "https://linktr.ee/dyagee",
        "email": "ageeaondo45@gmail.com",
    }

description = """
## Summary

This API helps you do awesome stuff, like create a user in the database and perform various `RUD` operations using the methods below:.


You will be able to:


* **add_user_data(name:str)**
* **get_user_data(id:str)**
* **update_user_data(id:str,new_name:str)**
* **delete_user(id:str)**


## CREATE: Adding a new person.  =>/api

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



## READ: Fetching details of a person.  => /api/user_id

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



## UPDATE: Modifying details of an existing person => /api/user_id

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



## DELETE: Removing a person => /api/user_id

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


## Example on Localhost:

You can test the ``API`` endpoints with  ``Postman`` or any similar services; to test it on localhost,

Create a python file name it *test.py* and add the code below


```python
import requests
import json

url = "https://hngx-2-alpha.vercel.app/api/d13b7e876571"

def formatted_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get(f"{url}")
if response.status_code == 200:
    print("sucessfully fetched the data")
    formatted_print(response.json())
else:
    print(f"There's a {response.status_code} error with your request")
  
```
Run the test.py file in any code editor of your choice, you should receive the response accordingly.

The above example was done for a GET request, you can carry rest of the operations in a similar fashion.


### **Note:** if the operation was not successful, a corresponding error message would be sent back to the client.


## Miscellaneous

Your data is safe with us, every entry data is screened against markup injections.
To ensure all interactions with the database are secure and free from common vulnerabilities (e.g., SQL injections) we use markupsafe.


```python
from markupsafe import escape
name = escape(name)
col.insert_one({"name":name})
```

---

"""