from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.6-flash')

chat_template = ChatPromptTemplate([
    ('system','You are a travel guide.'),
    ('human','Plan a {days}-day trip to {place}.')
])

user_days = input("enter the number of days : ")
user_place = input("enter name of the place : ")

prompt = chat_template.invoke({
    'days':user_days,
    'place':user_place
})

result = model.invoke(prompt)
print(result)