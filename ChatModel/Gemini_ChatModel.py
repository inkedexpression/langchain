from httplib2.auth import token
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

ChatModel = GoogleGenerativeAI(model = "gemini-3.6-flash")

result = ChatModel.invoke("what is the meaning of gandu")

print(result)