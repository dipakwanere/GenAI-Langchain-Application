# How to write a promt: It should be clear and informative.

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)

# Define zero shot prompt template
zero_shot_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that classifies the sentiment of given text as positive,negative or neutral.",
        ),
        ("human", "Classify the sentiment of this text:{text}"),
    ]
)

# parser = StrOutputParser()

chain = zero_shot_prompt | llm

response = chain.invoke({"text": "I had an amazing day at the beach!"})
print(response.content)
