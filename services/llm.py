import streamlit as st
from ollama import Client


def generate_response(prompt):
    try:
        api_key = st.secrets"53ccde5d1a7c4a1db001f9ceac869af3.QSFlHRz46vvJld4WKibftwEO"
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

    except KeyError:
        return "Error: OLLAMA_API_KEY is missing from Streamlit secrets."

    except Exception as error:
        return f"Error: {type(error).__name__}: {error}"
