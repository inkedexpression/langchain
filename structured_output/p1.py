from pydantic import BaseModel , EmailStr

class User(BaseModel):
    name : str
    age : int
    email : str
new_user = {'name':'dhanush','age':23 , 'email':'dhanush@gmail.com'}
student = User(**new_user)

print(student)