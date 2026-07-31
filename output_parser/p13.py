
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from pydantic import BaseModel , Field
from dotenv import  load_dotenv



#llm calling
load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")
model = ChatHuggingFace(llm=llm)

#BaseModel classes
class Employee(BaseModel):
    name : str = Field(description="name of the employee")
    age : int = Field(gt=0 , description="age of the employee")
    designation:str = Field(description="designation of the employee")
    salary : int = Field(gt=0 , description="salary of the employee")

class Department(BaseModel):
    department_name : str = Field(description="name of the department")
    employees : list[Employee] = Field(description="list of employees")

class Company(BaseModel):
    company_name : str  = Field(description="name of the company")
    location : str = Field(description="location of the company")
    departments : list[Department] = Field(description="list of departments")

parser = PydanticOutputParser(pydantic_object=Company)

template = PromptTemplate(template="Generate details for {company} with three departments. \n {format_instruction}",input_variables=['company'],partial_variables = {'format_instruction':parser.get_format_instructions()})

chain = template | model | parser

result = chain.invoke({'company':'spacex'})
print(result)










