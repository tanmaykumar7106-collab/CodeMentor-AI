import streamlit as st
from ollama import Client


def generate_response(prompt):
    try:
        api_key = st.secrets["OLLAMA_API_KEY"]
        model = st.secrets.get("OLLAMA_MODEL", "qwen3.5:397b")

        client = Client(
            host="https://ollama.com",
            headers={
                "Authorization": f"Bearer {api_key}"
            }
        )

        response = client.generate(
            model=model,
            prompt=prompt,
            stream=False
        )

        return response["response"].strip()

    except Exception as error:
        return f"Error: {type(error).__name__}: {error}"
