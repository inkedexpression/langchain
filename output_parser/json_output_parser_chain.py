from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id='Qwen/Qwen2.5-7B-Instruct' , task="text-generation")
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template1 = PromptTemplate(template="write all the name of saga in one piece anime \n {format_instruction}" ,partial_variables={'format_instruction':parser.get_format_instructions()} )

chain = template1 | model | parser
result = chain.invoke({})
print(result)
