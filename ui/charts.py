import matplotlib.pyplot as plt
import streamlit as st


def render_chart(df):
    if df.empty or "Category" not in df.columns:
        return

    counts = df["Category"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 4))

    fig.patch.set_facecolor("#0b0f19")
    ax.set_facecolor("#111827")

    bars = ax.bar(
        counts.index,
        counts.values,
        color="#3b82f6"
    )

    ax.set_title(
        "Test Case Distribution",
        color="white",
        pad=15
    )

    ax.set_ylabel("Number of Tests", color="#cbd5e1")
    ax.tick_params(colors="#cbd5e1")
    ax.grid(axis="y", linestyle="--", alpha=0.2)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_color("#2d3748")
    ax.spines["left"].set_color("#2d3748")

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            int(bar.get_height()),
            ha="center",
            va="bottom",
            color="white"
        )

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)