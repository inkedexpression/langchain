from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import  load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")
model = ChatHuggingFace(llm=llm)

class Student(BaseModel):
    name : str = Field(description="Name of the student ")
    age : int = Field(description="Age of the student")
    cgpa : float = Field(ge=0 , le=10 , description="CGPA of the student.")
    branch : str = Field(description="branch of the student")

parser = PydanticOutputParser(pydantic_object=Student)

template = PromptTemplate(template = "generate the details of an AIML student \n {format_instruction}",input_variables=[],partial_variables={'format_instruction':parser.get_format_instructions()})

chain = template | model | parser
result = chain.invoke({})
print(result)