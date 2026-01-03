import os
from dotenv import load_dotenv

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnablePassthrough

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)


# Prompt 1: Generate Title
title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are an expert journalist.
    Come up with one interesting and catchy title for the following topic:
    Topic: {topic}
    Answer with exactly one title.
    """,
)

# Prompt 2: Write Essay
essay_prompt = PromptTemplate(
    input_variables=["title", "emotion"],
    template="""
    You are an expert non-fiction writer.

    Write a short essay (100–120 words) for the following title:
    {title}

    Make the essay engaging and make the reader feel the following emotion:
    {emotion}

    Format the output strictly as a JSON object with exactly these keys:
    "title", "emotion", "essay"
    """,
)

# Chains
# First chain: Topic -> Title
title_chain = title_prompt | llm | StrOutputParser()

# Overall chain: Title + Emotion -> Essay (JSON)
overall_chain = (
    {"title": title_chain, "emotion": RunnablePassthrough()}
    | essay_prompt
    | llm
    | JsonOutputParser()
)

# Streamlit UI

st.title("AI Essay Writer")
topic = st.text_input("Enter the topic")
emotion = st.text_input("Enter the emotion (e.g., hope, sadness, excitement)")

if topic and emotion:
    response = overall_chain.invoke({"topic": topic, "emotion": emotion})
    st.subheader("Generated Essay")
    st.json(response)
