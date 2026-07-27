from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.6-flash')

chat_template = ChatPromptTemplate([
    ('system',"You are a professional fitness coach."),
    ('human','Create a {days}-day workout plan for {goal}.')
],input_variables=['days','goal'])

user_goal = input("enter the goal : ")
user_days = input("enter the number of days : ")


prompt = chat_template.invoke({
    'days':user_days,
    'goal':user_goal
})

result = model.invoke(prompt)
print(prompt)
print(result)