from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

chat_template = ChatPromptTemplate([
    ('system','You are a {expert} expert.'),
    MessagesPlaceholder(variable_name='chat_history'),
])

chat_history = []
st.header("AI Consultant")

user_expert = st.selectbox("Select the Expert Domain",["Cricket","Cooking"," Programming","Finance"])

user_query = st.text_input("Enter your Question : ")


if st.button("Assist"):

    chat_history.append(HumanMessage(content=user_expert))
    chat_history.append(HumanMessage(content=user_query))
    chain = chat_template | model
    result = chain.invoke({
        'expert':user_expert,
        'chat_history':chat_history
    })
    chat_history.append(result)
    st.write(result.text())
