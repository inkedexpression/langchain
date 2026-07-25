from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

result = embedding.embed_documents(documents)

print(result)