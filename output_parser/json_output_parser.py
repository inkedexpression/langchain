from langchain_core.prompts import  PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct" , task="text-generation")
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template1 = PromptTemplate(template="give me the the name age and city of emma d'arcy \n {format_instruction}" , input_variable=[] , partial_variables={'format_instruction':parser.get_format_instructions()})

prompt = template1.format()
result = model.invoke(prompt)

print(parser.parse(result.content))