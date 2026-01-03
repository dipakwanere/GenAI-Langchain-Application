import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# LangChainDeprecationWarning: LLMChain is deprecated
from langchain_classic.chains import LLMChain

# so use the following runnable
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)

# Define the prompt template with a COT Instruction
cot_prompt = PromptTemplate(
    input_variables=["question"],
    template="""Question:{question}
    Let's solve this problem step-by-step to ensure we get the right answer.
    Thought:""",
)

## Creating a chain
parser = StrOutputParser()
chain = cot_prompt | llm | parser
# chain = LLMChain(llm=llm, prompt=cot_prompt)

# sample questions
question = "If a store has 10 apples, sells 4 and receives 5 more, How many apples does it have?"

# Run the chain
response = chain.invoke(question)
# print(response["text"])   # this is for old LLMChain
print(response)
