from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


template = PromptTemplate(template = "Recommond a restaurant in {city} include : name , rating , cuisine , city ",input_variables=['city'])


prompt = template.invoke({'city':'mangalore'})
result = model.invoke(prompt)
print(result.content)