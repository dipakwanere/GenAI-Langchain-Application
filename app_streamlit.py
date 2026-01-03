import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Please respond to the questions asked.",
        ),
        ("user", "Question:{question}"),
    ]
)

st.title("LangChain App Demo")
input_text = st.text_input("What questions do you have in mind?")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
