from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.6-flash")

try:
    while True:
        user_query = input("enter your query : ")


        if user_query.lower() == 'exit':
            break

        expert = input("Enter the type of instructor :")
        number_of_words = input("enter the number of words for the answer : ")
        if not number_of_words.isdigit():
            print("enter a valid number ")
            continue



        result = model.invoke(f"You are an {expert} and explain {user_query} in {number_of_words} words")
        print(result)
except Exception as e:
    print(e)
