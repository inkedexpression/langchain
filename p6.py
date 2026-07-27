from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.6-flash')

chat_template = ChatPromptTemplate([
    ('system','you are an python experet'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = [HumanMessage(content='Hi'),
AIMessage(content='Hello!'),

HumanMessage(content='What is Python?'),
AIMessage(content='Python is a programming language.')
]

while True:
    user_query = input("enter your query : ")
    chat_history.append(HumanMessage(user_query))
    if user_query.lower() == 'exit':
        break

    prompt = chat_template.invoke({'chat_history':chat_history,'query':user_query})
    result = model.invoke(prompt)
    chat_history.append(AIMessage(result))
    print(result)
print(chat_history)
