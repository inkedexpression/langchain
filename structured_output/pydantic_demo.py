from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    name : str
    age:Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 0 , lt = 10 , default=5 , description = "decimal value representing the cgpa of student")

new_student = {'name':'Dhanush' , 'age':'23' ,'email':'abc@gmail.com'}

s1 = Student(**new_student)
print(s1)