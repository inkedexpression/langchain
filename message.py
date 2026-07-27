from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.6-flash")

chat_history = [
    SystemMessage(content="you are an helpful assistant")
]

while True:
    user_query = input("YOU: ")
    chat_history.append(HumanMessage(user_query))
    if user_query.lower() == 'exit':
        break
    result = model.invoke(user_query)
    chat_history.append(AIMessage(result))
    print("AI: ",result)

print(chat_history)