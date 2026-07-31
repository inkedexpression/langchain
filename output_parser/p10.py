from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from pydantic import BaseModel , Field
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)


class Question(BaseModel):
    question : str = Field(description="question with question number")
    option : list[str] = Field(description="4 option for the question")
    answer : str = Field(description="answer for the question")

class Quiz(BaseModel):
    question : list[Question]

parser = PydanticOutputParser(pydantic_object=Quiz)

template = PromptTemplate(template="Generate 5 Python MCQs.\n {format_instruction}",input_variables=[],partial_variables={'format_instruction':parser.get_format_instructions()})


chain = template | model | parser

result = chain.invoke({})
print(result)