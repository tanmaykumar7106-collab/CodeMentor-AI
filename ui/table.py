import pandas as pd
import streamlit as st


def render_table(test_cases):
    df = pd.DataFrame(test_cases)

    column_names = {
        "id": "ID",
        "category": "Category",
        "scenario": "Test Scenario",
        "input": "Input",
        "expected_output": "Expected Output",
        "priority": "Priority"
    }

    df = df.rename(columns=column_names)

    st.subheader("Generated Test Cases")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=380
    )

    return df