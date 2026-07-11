import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "granite3.1-dense:2b"


def generate_response(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()
        return response.json().get("response", "").strip()

    except requests.exceptions.ConnectionError:
        return "Error: Ollama is not running."

    except requests.exceptions.Timeout:
        return "Error: The model took too long to respond."

    except requests.exceptions.RequestException as error:
        return f"Error: {error}"