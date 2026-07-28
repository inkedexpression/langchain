from pydantic import BaseModel ,Field

class Student(BaseModel):

    name : str = Field(... , description="user name ")
    age : int = Field(gt=17)
    marks : int = Field(gt = 0 ,lt=100)

st1 = {'name':'dhanush','age':23,'marks':34}
new_st = Student(**st1)
print(new_st)
