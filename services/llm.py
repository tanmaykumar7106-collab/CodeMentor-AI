import streamlit as st
from ollama import Client


def generate_response(prompt):
    try:
        client = Client(
            host="https://ollama.com",
            headers={
                "Authorization": f"Bearer {st.secrets['53ccde5d1a7c4a1db001f9ceac869af3.QSFlHRz46vvJld4WKibftwEO']}"
            }
        )

        response = client.generate(
            model=st.secrets.get("OLLAMA_MODEL", "qwen3.5:397b"),
            prompt=prompt,
            stream=False
        )

        return response["response"].strip()

    except Exception as error:
        return f"Error: {type(error).__name__}: {error}"
