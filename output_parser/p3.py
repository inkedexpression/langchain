from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = HuggingFaceEndpoint(repo_id = "Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(template = "Generate {country} , include country , capital and population \n {format_instruction}",input_variables=['country'],partial_variables={'format_instruction':parser.get_format_instructions()})

prompt = template.invoke({'country':'india'})
result = model.invoke(prompt)
print(parser.parse(result.content))
