import streamlit as st


def render_dashboard():
    st.markdown(
        """
        <style>
        :root {
            --bg: #070b14;
            --surface: #0f172a;
            --surface-2: #111c31;
            --border: #23314d;
            --primary: #2563eb;
            --primary-soft: rgba(37, 99, 235, 0.16);
            --text: #f8fafc;
            --muted: #94a3b8;
            --success: #22c55e;
        }

        .stApp {
            background:
                radial-gradient(
                    circle at top right,
                    rgba(37, 99, 235, 0.12),
                    transparent 30%
                ),
                var(--bg);
            color: var(--text);
        }

        .block-container {
            max-width: 1280px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        [data-testid="stSidebar"] {
            background-color: #0b1220;
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 1.3rem;
        }

        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
        }

        .brand-icon {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #2563eb, #7c3aed);
            color: white;
            font-weight: 800;
            font-size: 14px;
            box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);
        }

        .sidebar-brand h2 {
            font-size: 18px;
            margin: 0;
            color: white;
        }

        .sidebar-brand p {
            margin: 2px 0 0;
            color: var(--muted);
            font-size: 12px;
        }

        .model-card {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 13px;
            border-radius: 10px;
            border: 1px solid var(--border);
            background-color: var(--surface);
        }

        .model-card p {
            margin: 2px 0 0;
            font-size: 12px;
            color: var(--muted);
        }

        .status-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background-color: var(--success);
            box-shadow: 0 0 10px rgba(34, 197, 94, 0.8);
        }

        .hero {
            position: relative;
            overflow: hidden;
            padding: 32px;
            border-radius: 18px;
            border: 1px solid var(--border);
            background:
                linear-gradient(
                    135deg,
                    rgba(37, 99, 235, 0.16),
                    rgba(124, 58, 237, 0.08)
                ),
                var(--surface);
            margin-bottom: 28px;
        }

        .hero::after {
            content: "";
            position: absolute;
            top: -70px;
            right: -70px;
            width: 190px;
            height: 190px;
            border-radius: 50%;
            background: rgba(37, 99, 235, 0.14);
            filter: blur(10px);
        }

        .hero-badge {
            display: inline-block;
            padding: 6px 10px;
            margin-bottom: 13px;
            border-radius: 999px;
            background-color: var(--primary-soft);
            color: #93c5fd;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.04em;
        }

        .hero h1 {
            font-size: 38px;
            margin: 0;
            color: white;
        }

        .hero p {
            max-width: 680px;
            margin: 10px 0 0;
            color: #b8c4d8;
            font-size: 16px;
            line-height: 1.7;
        }

        h1, h2, h3 {
            color: white;
        }

        [data-testid="stMetric"] {
            background:
                linear-gradient(
                    180deg,
                    rgba(255,255,255,0.02),
                    rgba(255,255,255,0)
                ),
                var(--surface);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.16);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted);
        }

        [data-testid="stMetricValue"] {
            color: white;
        }

        .stButton > button {
            min-height: 46px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: white;
            font-weight: 700;
            box-shadow: 0 8px 20px rgba(37, 99, 235, 0.25);
            transition: 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-1px);
            color: white;
            box-shadow: 0 10px 28px rgba(37, 99, 235, 0.38);
        }

        div[data-testid="stDownloadButton"] button {
            min-height: 44px;
            width: 100%;
            border-radius: 10px;
            border: 1px solid var(--border);
            background-color: var(--surface);
            color: white;
        }

        div[data-testid="stDownloadButton"] button:hover {
            border-color: #3b82f6;
            color: white;
        }

        [data-testid="stDataFrame"] {
            border: 1px solid var(--border);
            border-radius: 12px;
            overflow: hidden;
        }

        [data-baseweb="select"] > div,
        [data-baseweb="textarea"] > div {
            background-color: var(--surface);
            border-color: var(--border);
        }

        .stAlert {
            border-radius: 10px;
            border: 1px solid var(--border);
        }

        hr {
            border-color: var(--border);
        }

        .footer {
            margin-top: 45px;
            padding-top: 20px;
            border-top: 1px solid var(--border);
            text-align: center;
            color: var(--muted);
            font-size: 13px;
        }
        </style>

        <div class="hero">
            <span class="hero-badge">IBM GRANITE POWERED</span>
            <h1>CodeMentor AI</h1>
            <p>
                Generate software test cases, analyze source code and solve
                coding problems through guided AI assistance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_footer():
    st.markdown(
        """
        <div class="footer">
            CodeMentor AI · Built with IBM Granite, Python and Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )