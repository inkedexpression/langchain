from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from pydantic import BaseModel , ValidationError
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)
parser1 = StrOutputParser()

class News(BaseModel):
    title : str
    summary : str
    category : str

parser2 = PydanticOutputParser(pydantic_object=News)

template1 = PromptTemplate(template="Generate a Detailed news artical on {topic}",input_variables=['topic'])
template2 = PromptTemplate(template="summarize the given artical {text}",input_variables=['text'])
template3 = PromptTemplate(template="convert the given {text} into json \n {format_instruction}",input_variables=['text'],partial_variables={'format_instruction':parser2.get_format_instructions()})

chain = template1 | model | parser1 | template2 | model | parser1 | template3 | model | parser2

result = chain.invoke({'topic':'LLM'})
print(result)