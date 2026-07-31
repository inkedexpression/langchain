# Create a Product model:
# * name
# * price
# * category
# * stock
# Prompt:
# Invent a laptop and generate its details.

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from pydantic import BaseModel , Field
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",task="text-generation")

model = ChatHuggingFace(llm=llm)

class Product(BaseModel):
    name : str = Field(description="name of the product")
    price : float = Field(description="price of the product")
    category : str = Field(description="catergory of the product")
    stock : int = Field(description="number of stock of the product")

parser = PydanticOutputParser(pydantic_object=Product)

template = PromptTemplate(template="Invent a laptop and generate its details. \n {format_instruction} ",input_variables=[],partial_variables={'format_instruction':parser.get_format_instructions()})

chain = template | model | parser

result = chain.invoke({})
print(result)