from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-7B-Instruct',task='text-generation')

model = ChatHuggingFace(llm=llm)

class Movie(BaseModel):
    title : str =  Field(description="Title of the movie")
    release_year : int =  Field(description="Relase year of the movie.")
    rating : float = Field(ge=0 , le=10 , description="Rating of the movie")

parser = PydanticOutputParser(pydantic_object=Movie)

template = PromptTemplate(template="Generate the title , release_year and rating of the {movie} \n {format_instruction} " , input_variables=['movie'] , partial_variables={'format_instruction':parser.get_format_instructions()})

prompt = template.invoke({'movie':'intersteller'})
result = model.invoke(prompt)
print(parser.parse(result.content))