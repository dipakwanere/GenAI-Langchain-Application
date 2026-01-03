import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)

# Giving the topic as a user input and model should give an essay on that topic.
title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are an expert Journalist.
    You need to come up with an interesting title for the following topic:{topic}
    Answer exactly with one title
    """,
)

essay_prompt = PromptTemplate(
    input_variables=["title"],
    template="""You are expert non-fiction writer.
    You need to write a short essay of 100 to 120 words for the following title:{topic}
    """,
)

# Chaining the first and second chains
first_chain = title_prompt | llm | StrOutputParser()
second_chain = essay_prompt | llm
overall_chain = first_chain | second_chain

st.title("Esssay Writer")
topic = st.text_input("Enter the topic")

if topic:
    response = overall_chain.invoke({"topic": topic})
    st.write(response.content)
