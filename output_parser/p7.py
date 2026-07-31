from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="name of the employee")
    Emp_id : int = Field(description="employee  id of the employee")
    department : str = Field(description="Department of the employee")
    age : int = Field(description="age of the employee")

class Details(BaseModel):
    people : list[Person]


parser = PydanticOutputParser(pydantic_object=Details)

template = PromptTemplate(template="generate name , age , department and employee id of 5 employee \n {format_instruction}",input_variables=[],partial_variables={'format_instruction':parser.get_format_instructions()})

chain = template | model | parser

result = chain.invoke({})
print(result)