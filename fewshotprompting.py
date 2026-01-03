# How to write a promt: It should be clear and informative.

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

# Define prompt example (input/output pairs)

examples = [
    {"review": "Terrible customer service.", "sentiment": "Negative"},
    {"review": "Amazing experience from start to end.", "sentiment": "Positive"},
    {"review": "It was okay, Nothing special.", "sentiment": "Neutral"},
]

# Define how each exmaple should be formated
example_prompt = PromptTemplate.from_template("Review:{review}\nSentiment:{sentiment}")

# Create few shot template

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Classify the sentiment of the following movie reviews. Use the format provided in the examples.",
    suffix="Review: {input}\nSentiment:",
    input_variables=["input"],
)

# create the chain

chain = few_shot_prompt | llm

# invoke the chains

new_review = "The plot was a complete mess abd very boring."
response = chain.invoke({"input": new_review})
print(response.content)
