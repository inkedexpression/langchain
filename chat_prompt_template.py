from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.6-flash')

chat_template =  ChatPromptTemplate([
    ('system','you are an {domain} expert'),
    ('human','explain me about {topic} in simple term')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'spin balling'})
print(model.invoke(prompt))