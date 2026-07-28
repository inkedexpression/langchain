from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

documents = [
    "Python is a high-level programming language used for web development, data science, automation, and artificial intelligence.",

    "Machine learning is a branch of artificial intelligence that enables computers to learn from data without being explicitly programmed.",

    "The Sun is the center of the Solar System and provides light and energy to all the planets.",

    "Jasprit Bumrah is an Indian fast bowler famous for his yorkers and unique bowling action.",

    "Virat Kohli is an Indian cricketer known for his aggressive batting style and exceptional consistency.",

    "MS Dhoni is a former Indian cricket captain renowned for his calm leadership and finishing abilities.",

    "The Great Wall of China is one of the longest man-made structures in the world.",

    "The Eiffel Tower is a famous landmark in Paris and one of the most visited monuments in the world.",

    "Earth is the third planet from the Sun and the only known planet to support life.",

    "The Pacific Ocean is the largest and deepest ocean on Earth.",

    "The human heart pumps blood throughout the body and is a vital organ of the circulatory system.",

    "Basketball is a sport played between two teams of five players, where the objective is to score by shooting the ball through a hoop.",

    "Lionel Messi is an Argentine footballer widely regarded as one of the greatest players in football history.",

    "Mount Everest is the highest mountain above sea level and is located in the Himalayas.",

    "Photosynthesis is the process by which green plants convert sunlight, water, and carbon dioxide into food and oxygen.",

    "The Amazon rainforest is the world's largest tropical rainforest and is home to incredible biodiversity.",

    "The Taj Mahal is a white marble mausoleum in Agra built by Emperor Shah Jahan in memory of his wife Mumtaz Mahal.",

    "The Internet is a global network that allows billions of devices to communicate and share information.",

    "Java is an object-oriented programming language widely used for enterprise applications and Android development.",

    "Artificial Intelligence focuses on creating systems that can perform tasks requiring human intelligence, such as reasoning and decision making."
]

doc_embed = [model.embed_query(doc) for doc in documents]
# t%is doc_embed is out of the loop bcz when time i asked question the loop will embed this doc once again which will
# increase the call of API
try:
    while True:
        user_query = input("Enter the query ('exit' to quite) : ")
        if user_query.lower() == 'exit':
            break

        query_embed = model.embed_query(user_query)

        score = cosine_similarity([query_embed],doc_embed)[0]
        top5 = sorted(enumerate(score),key=lambda x:x[1],reverse=True)[:5]
        for index , score in top5:
            print(score)
            print(documents[index])
            print('-'*50)

except Exception as e:
    print(e)