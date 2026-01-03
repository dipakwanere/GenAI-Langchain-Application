import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)
# Import ChatGroq from the Groq integration package
from langchain_groq import ChatGroq

app = FastAPI(title="Generative AI with LangChain + Groq API")


# Pydantic schema for the generate request
class GenerationRequest(BaseModel):
    prompt: str
    max_tokens: int | None = None


# Templates directory
templates = Jinja2Templates(directory="templates")


@app.post("/generate")
async def generate_text(request: GenerationRequest):
    try:
        # Invoke the model with a basic conversation list
        messages = [
            ("system", "You are a helpful assistant."),
            ("human", request.prompt),
        ]
        ai_msg = llm.invoke(messages)
        return {"generated_text": ai_msg.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("web_html.html", {"request": request})
