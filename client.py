import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/chain/invoke"


def get_groq_response(input_text):
    payload = {"input": {"language": "French", "text": input_text}}

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()["output"]

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except KeyError:
        return f"Unexpected response format: {response.json()}"


# Streamlit app
st.title("LLM Application using LangChain + Groq")

input_text = st.text_input("Enter the text to convert to French")

if input_text:
    st.write(get_groq_response(input_text))
