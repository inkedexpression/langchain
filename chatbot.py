"""
in this we have chat_history of user and AI conversation , but we have no idea whi has sent which message
so to solve this we have 3 type of message where the code is written in message.py

"""

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model= "gemini-3.6-flash")

# chat history
chat_history = []

while True:
    user_query = input("YOU : ")
    chat_history.append(user_query)
    if user_query.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result)
    print("AI : ",result)

print(chat_history)