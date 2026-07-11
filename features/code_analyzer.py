import streamlit as st
from streamlit_ace import st_ace

from prompts.review import build_review_prompt
from services.llm import generate_response


LANGUAGES = {
    "Python": "python",
    "Java": "java",
    "C++": "c_cpp",
    "JavaScript": "javascript"
}


def render():
    st.subheader("Code Analyzer")
    st.caption(
        "Understand your code, identify issues and receive practical improvement suggestions."
    )

    language = st.selectbox(
        "Programming Language",
        LANGUAGES,
        key="analyzer_language"
    )

    code = st_ace(
        placeholder="Paste your code here...",
        language=LANGUAGES[language],
        theme="tomorrow_night",
        keybinding="vscode",
        show_gutter=True,
        show_print_margin=False,
        auto_update=True,
        wrap=True,
        height=350,
        key="analyzer_editor"
    )

    if st.button(
        "Analyze Code",
        use_container_width=True
    ):
        if not code or not code.strip():
            st.warning("Please enter some code.")
        else:
            with st.spinner("Analyzing your code..."):
                prompt = build_review_prompt(code, language)
                st.session_state.code_review = generate_response(prompt)

    response = st.session_state.get("code_review")

    if not response:
        return

    if response.startswith("Error:"):
        st.error(response)
    else:
        st.success("Code analysis completed.")
        st.markdown(response)

        st.download_button(
            "Download Review",
            response,
            "code_review.md",
            "text/markdown",
            use_container_width=True
        )