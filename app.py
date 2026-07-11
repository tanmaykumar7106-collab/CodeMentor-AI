import streamlit as st
from  streamlit_option_menu import option_menu
from features.code_analyzer import render as code_analyzer
from features.problem_solver import render as problem_solver
from features.test_generator import render as test_generator
from ui.dashboard import render_dashboard, render_footer


st.set_page_config(
    page_title="CodeMentor AI",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

render_dashboard()

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="brand-icon">CM</div>
            <div>
                <h2>CodeMentor AI</h2>
                <p>Learn. Test. Improve.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    mode = option_menu(
        menu_title=None,
        options=[
            "Test Generator",
            "Code Analyzer",
            "Problem Solver"
        ],
        icons=[
            "clipboard-check",
            "code-square",
            "lightbulb"
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "6px",
                "background-color": "transparent"
            },
            "icon": {
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "15px",
                "padding": "12px 14px",
                "border-radius": "9px",
                "margin": "5px 0"
            },
            "nav-link-selected": {
                "background-color": "#2563eb"
            }
        }
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="model-card">
            <span class="status-dot"></span>
            <div>
                <strong>IBM Granite</strong>
                <p>Local model connected</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("Version 1.0")

if mode == "Test Generator":
    test_generator()
elif mode == "Code Analyzer":
    code_analyzer()
else:
    problem_solver()

render_footer()