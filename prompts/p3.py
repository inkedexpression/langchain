from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-3.6-flash')

template = PromptTemplate(template = """
Summarize the {article} in {number} words
""",input_variables = ['article','number'])

user_artical = input("enter the article : ")
user_number = input("enter the number of words needed : ")

prompt = template.invoke({
    'article':user_artical,
    'number' : user_number
})

result = model.invoke(prompt.to_string())
print(result)

