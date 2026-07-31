from xml.sax import parse

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)

class Movie(BaseModel):
    title : str = Field(description="Title of the movie")
    release_year : int = Field(description="year of release")
    rating : float = Field(description="rating of the movie")
    genres : list[str] = Field(description="list of genre og the movie")

class Actors(BaseModel):
    name : str = Field(description="actors and actress name")
    age : int = Field(description="age of the actress and actor")

class MovieDetails(BaseModel):
    movie : Movie
    actors : list[Actors]

parser = PydanticOutputParser(pydantic_object = MovieDetails)

template = PromptTemplate(template="Generate details of the movie {movie} \n {format_instruction}",input_variables=['movie'],partial_variables = {'format_instruction':parser.get_format_instructions()})

chain = template | model | parser

result = chain.invoke({'movie':'john wick'})
print(result)