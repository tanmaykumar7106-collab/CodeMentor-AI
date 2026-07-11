import os

import requests
import streamlit as st


LOCAL_URL = "http://localhost:11434/api/generate"
CLOUD_URL = "https://ollama.com/api/generate"


def get_setting(name, default=None):
    """Read from Streamlit secrets first, then environment variables."""
    try:
        return st.secrets.get(name, os.getenv(name, default))
    except FileNotFoundError:
        return os.getenv(name, default)


def generate_response(prompt):
    api_key = get_setting("OLLAMA_API_KEY")
    url = get_setting(
        "OLLAMA_URL",
        CLOUD_URL if api_key else LOCAL_URL
    )

    model = get_setting(
        "OLLAMA_MODEL",
        "qwen3-coder-next" if api_key else "granite3.1-dense:2b"
    )

    headers = (
        {"Authorization": f"Bearer {api_key}"}
        if api_key
        else {}
    )

    try:
        response = requests.post(
            url,
            headers=headers,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()

        result = response.json().get("response", "").strip()

        return result or "Error: The model returned an empty response."

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the AI service."

    except requests.exceptions.Timeout:
        return "Error: The AI model took too long to respond."

    except requests.exceptions.HTTPError:
        return (
            f"Error: AI service returned status "
            f"{response.status_code}: {response.text}"
        )

    except requests.exceptions.RequestException as error:
        return f"Error: {error}"