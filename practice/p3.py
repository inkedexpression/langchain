from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2')

documents = [
    "Apple is a fruit.",
    "Lion is a wild animal.",
    "Python is a programming language.",
    "Earth revolves around the Sun.",
    "Virat Kohli is a cricketer."
]

query = "Apple is a fruit."

embed_doc = [model.embed_query(doc) for doc in documents]
embed_query = model.embed_query(query)

scores = cosine_similarity([embed_query],embed_doc)[0]
index,score = sorted(list(enumerate(scores)),key= lambda x:x[1])[-1]

print(query)
print(score)
print(documents[index])