from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm_model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)

# creating a prompt

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

parser = StrOutputParser()

# Chains

chain = prompt_template | llm_model | parser

# app defination
app = FastAPI(
    title="LangServe Server API",
    version="0.0.1",
    description="A simple API using Langchain runnable interfaces",
)

# IMPORTANT: path name
add_routes(app, chain, path="/chain", enable_streaming=False)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
