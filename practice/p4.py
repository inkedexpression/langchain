from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2")

documents = [
    "Apple is a fruit.",
    "Lion is a wild animal.",
    "Python is a programming language.",
    "Earth revolves around the Sun.",
    "Virat Kohli is a cricketer."
]

query = "lion"

doc_embed = [model.embed_query(doc) for doc in documents]
query_embed = model.embed_query(query)

scores = cosine_similarity([query_embed],doc_embed)[0]
top3 = sorted(enumerate(scores),key=lambda x:x[1],reverse=True)[:3]
for index , score in top3:
    print(score,documents[index])