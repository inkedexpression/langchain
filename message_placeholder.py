from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model  = GoogleGenerativeAI(model='gemini-3.6-flash')

chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('chat_history.txt','r') as f:
    chat_history.extend(f.readlines())

    prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'where is my refund'})
    print(model.invoke(prompt))
