from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct" , task="text-=generation")

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(template = "Generate an 200 words artical on python")
template2 = PromptTemplate(template = "write an 3 bullet point summary on {text}" , input_variables=['text'])

parser = StrOutputParser()

chain = template1 | model |parser | template2 | model | parser

result = chain.invoke({})
print(result)