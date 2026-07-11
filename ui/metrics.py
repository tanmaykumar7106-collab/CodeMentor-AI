import streamlit as st


def render_metrics(test_cases):
    categories = [
        str(case.get("category", "")).lower()
        for case in test_cases
    ]

    values = {
        "Total Tests": len(test_cases),
        "Functional": sum("functional" in item for item in categories),
        "Boundary": sum("boundary" in item for item in categories),
        "Edge Cases": sum("edge" in item for item in categories),
        "Negative": sum("negative" in item for item in categories)
    }

    columns = st.columns(len(values))

    for column, (label, value) in zip(columns, values.items()):
        column.metric(label, value)