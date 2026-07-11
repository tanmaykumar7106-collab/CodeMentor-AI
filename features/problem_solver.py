import streamlit as st

from prompts.problem import build_problem_prompt
from services.llm import generate_response


def render():
    st.subheader("Problem Solver")
    st.caption(
        "Get hints, approaches or complete solutions for coding and DSA problems."
    )

    col1, col2 = st.columns(2)

    language = col1.selectbox(
        "Programming Language",
        ["Python", "Java", "C++", "JavaScript"],
        key="solver_language"
    )

    help_level = col2.selectbox(
        "Help Level",
        [
            "Hint Only",
            "Approach",
            "Complete Solution"
        ]
    )

    problem = st.text_area(
        "Problem Statement",
        height=300,
        placeholder="Paste the coding problem here..."
    )

    if st.button(
        "Solve Problem",
        use_container_width=True
    ):
        if not problem.strip():
            st.warning("Please enter a coding problem.")
        else:
            with st.spinner("Analyzing the problem..."):
                prompt = build_problem_prompt(
                    problem,
                    language,
                    help_level
                )

                st.session_state.problem_solution = generate_response(prompt)

    response = st.session_state.get("problem_solution")

    if not response:
        return

    if response.startswith("Error:"):
        st.error(response)
    else:
        st.success("Problem analysis completed.")
        st.markdown(response)

        st.download_button(
            "Download Solution",
            response,
            "problem_solution.md",
            "text/markdown",
            use_container_width=True
        )