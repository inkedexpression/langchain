from  langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.6-flash')

template = PromptTemplate(template="""
You are a movie critic.
Review the movie {movie} which belongs to the {genre} genre.""",input_variables=['movie','genre'])

user_query_movie = input("enter the name of movie : ")
user_query_genre = input("enter the genre of the movie : ")

prompt = template.invoke({
    'movie':user_query_movie,
    'genre':user_query_genre
})
result = model.invoke(prompt)
print(result)