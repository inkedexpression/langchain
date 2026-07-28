from pydantic import BaseModel

class Employee(BaseModel):
    name:str
    salary:int

emp = Employee(
    name="Alex",
    salary=50000
)

print(emp.model_dump())
print(emp.model_dump_json())