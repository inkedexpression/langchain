from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

# prompt template
template1 = PromptTemplate(template = "write a detailed report on {topic}." , input_variables=['topic'])

# summary
template2 = PromptTemplate(template = "write a 5 line summary on text {text}." , input_variable=['text'])

prompt1 = template1.invoke({'topic':'black hole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke(result1)
result2 = model.invoke(prompt2)

print(result2.text)
