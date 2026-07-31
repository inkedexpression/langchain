from pydantic import BaseModel , Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)


class Education(BaseModel):
    degree : str
    institute : str
    year : int

class Experience(BaseModel):
    company : str
    role : str
    years : int

class Project(BaseModel):
    name : str
    coding_language : str

class Resume(BaseModel):
    name : str = Field(description="name of the candidate")
    skills : list[str] = Field(description="skills of the candidate , minimun 4 skills ")
    education : list[Education] = Field(description="the latest education the candidate pursued")
    experience : list[Experience] = Field(description="work experience of the candidate")
    projects : list[Project] = Field(description="projects done by the candidate")

parser = PydanticOutputParser(pydantic_object=Resume)

template = PromptTemplate(template="Generate a resume for a Python developer.\n {format_instruction}",input_variables=[],partial_variables={'format_instruction':parser.get_format_instructions()})

chain = template | model | parser

result = chain.invoke({})
print(result)

