from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.6-flash")

while True:
    user_query = input("Enter your query : ")

    if user_query.lower() == "exit":
        break

    result = model.invoke(user_query)
    print(result)