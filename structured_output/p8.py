from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import  BaseModel ,Field
from typing import Literal

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Movie(BaseModel):
    movie_name : str
    rating:float = Field(ge=0 , le=10)
    review:str


r = model.with_structured_output(Movie)
s1 = r.invoke("Interstellar")
print(s1)
print(s1.model_dump())