from io import StringIO

import pandas as pd
import streamlit as st
from streamlit_ace import st_ace

from prompts.prompt import build_test_case_prompt
from services.llm import generate_response


LANGUAGES = {
    "Python": "python",
    "Java": "java",
    "C++": "c_cpp",
    "JavaScript": "javascript"
}


def markdown_to_df(text):
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip().startswith("|")
    ]

    if len(lines) < 3:
        return None

    table = "\n".join(lines)
    df = pd.read_csv(
        StringIO(table),
        sep="|",
        engine="python"
    )

    df = df.dropna(axis=1, how="all")
    df.columns = df.columns.str.strip()

    separator_rows = df.apply(
        lambda row: row.astype(str)
        .str.replace("-", "", regex=False)
        .str.strip()
        .eq("")
        .all(),
        axis=1
    )

    return df[~separator_rows].map(
        lambda value: value.strip() if isinstance(value, str) else value
    )


def render():
    st.subheader("Test Case Generator")
    st.caption(
        "Paste your source code and generate functional, boundary, edge and negative test cases."
    )

    col1, col2 = st.columns(2)

    language = col1.selectbox(
        "Programming Language",
        LANGUAGES
    )

    coverage = col2.selectbox(
        "Coverage Level",
        ["Basic", "Standard", "Comprehensive"]
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
        key="test_editor"
    )

    if st.button(
        "Generate Test Cases",
        use_container_width=True
    ):
        if not code or not code.strip():
            st.warning("Please enter some code.")
        else:
            with st.spinner("Generating test cases..."):
                prompt = build_test_case_prompt(
                    code,
                    language,
                    coverage
                )

                st.session_state.test_response = generate_response(
                    prompt
                )

    response = st.session_state.get("test_response")

    if not response:
        return

    if response.startswith("Error:"):
        st.error(response)
        return

    st.success("Test cases generated successfully.")

    df = markdown_to_df(response)

    if df is None or df.empty:
        st.warning(
            "The table could not be formatted, so the original AI response is shown."
        )
        st.markdown(response)
        return

    st.subheader("Generated Test Cases")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=380
    )

    st.subheader("Summary")

    categories = df.get(
        "Category",
        pd.Series(dtype=str)
    ).astype(str).str.lower()

    metrics = {
        "Total Tests": len(df),
        "Functional": categories.str.contains(
            "functional"
        ).sum(),
        "Boundary": categories.str.contains(
            "boundary"
        ).sum(),
        "Edge Cases": categories.str.contains(
            "edge"
        ).sum(),
        "Negative": categories.str.contains(
            "negative"
        ).sum()
    }

    columns = st.columns(5)

    for column, (label, value) in zip(
        columns,
        metrics.items()
    ):
        column.metric(label, int(value))

    st.subheader("Analytics")

    if not categories.empty:
        st.bar_chart(categories.value_counts())

    st.subheader("Export")

    col1, col2 = st.columns(2)

    col1.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "test_cases.csv",
        "text/csv",
        use_container_width=True
    )

    col2.download_button(
        "Download Markdown",
        response,
        "test_cases.md",
        "text/markdown",
        use_container_width=True
    )