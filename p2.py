from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.6-flash')

template = PromptTemplate(template="""
Translate {text} to {language}
""",input_variables=['text','language'])

user_text = input("enter the text to be translated : ")
user_language = input("enter the Language : ")

prompt = template.invoke({
    'text':user_text,
    'language':user_language
})

result = model.invoke(prompt.to_string())
print(result)