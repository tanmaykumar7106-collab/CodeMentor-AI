import streamlit as st

def generate_response(prompt):
    st.write("Secrets available:", list(st.secrets.keys()))

    try:
        key = st.secrets["OLLAMA_API_KEY"]
        return f"API key loaded successfully (length: {len(key)})"
    except Exception as e:
        return f"Error: {e}"
