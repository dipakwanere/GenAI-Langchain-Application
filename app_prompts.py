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

prompt = PromptTemplate(
    input_variables=["country", "paragraph", "language"],
    template="""You are a currency expert. You give information about the specific currency used in a specific country.
    Avoid giving infromation about the fictional places.
     If the country is fictional or non existent, answer:I don't know about this {country}.
    Answer in {paragraph} short paragraph in {language} language.""",
)

parser = StrOutputParser()

st.title("Currency Info Generator")

country = st.text_input("Enter Country")
paragraph = st.number_input("Number of Paragraphs", min_value=1, max_value=5, value=1)
language = st.text_input("Enter Language", value="English")

# Button
if st.button("Generate Currency Info"):
    if country.strip():
        response = llm.invoke(
            prompt.format(
                country=country,
                paragraph=paragraph,
                language=language,
            )
        )
        st.subheader("Result")
        st.write(parser.invoke(response))
    else:
        st.warning("Please enter a country name.")
