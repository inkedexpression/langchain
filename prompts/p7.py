from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.6-flash')

chat_template = ChatPromptTemplate([
    ('system','You are an expert math teacher.'),
    MessagesPlaceholder(variable_name='chat_history')
])

chat_history = []

while True:
     user_query = input("enter the question : ")

     if user_query.lower() == 'exit':
         break
     chat_history.append(HumanMessage(user_query))
     prompt = chat_template.invoke({'chat_history':chat_history , 'query':user_query})
     result = model.invoke(prompt)
     chat_history.append(AIMessage(result.content))
     print(result)

print(chat_history)
