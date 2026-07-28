# nested model

from pydantic import  BaseModel

class Address(BaseModel):
    city : str
    area : str
    pin : int

class Person(BaseModel):
    name : str
    age : int
    address : Address


cx = {'address': {'city':'bangalore','area':'gbpalya','pin':565005 }, 'name':'dhanush','age':23}
result = Person(**cx)
print(result)