import streamlit as st
import matplotlib.pyplot as plt
from backend import classify_news, generate_real_version  

# --- Page Config ---
st.set_page_config(page_title="AI News Detector", page_icon="📰", layout="wide")

# --- Session State Initialization ---
if "analyze_clicked" not in st.session_state:
    st.session_state.analyze_clicked = False
if "confidence" not in st.session_state:
    st.session_state.confidence = 0.0
if "is_fake" not in st.session_state:
    st.session_state.is_fake = True
if "generated" not in st.session_state:
    st.session_state.generated = False
if "real_version" not in st.session_state:
    st.session_state.real_version = ""
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# --- Layout: Pie Chart (left) and Input/Output (right) ---
col1, col2 = st.columns([1, 2])

# --- LEFT SIDE: Confidence Chart + Generate Button ---
with col1:
    st.markdown("Credibility Index")

    if st.session_state.generated:
        label = "REAL"
        color = "#27ae60"
        confidence = st.session_state.confidence
    elif st.session_state.analyze_clicked:
        label = "FAKE" if st.session_state.is_fake else "REAL"
        color = "#e74c3c" if st.session_state.is_fake else "#27ae60"
        confidence = st.session_state.confidence
    else:
        label = ""
        color = "#bdc3c7"
        confidence = 0.0

    fig, ax = plt.subplots(figsize=(2.5, 2.5), facecolor="white")
    ax.set_facecolor("white")

    wedges, texts = ax.pie(
        [confidence, 1 - confidence],
        labels=[f"{label} ({confidence * 100:.1f}%)" if label else "", ""],
        colors=[color, "#ecf0f1"],
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.5, "edgecolor": "white"},
        textprops={'fontsize': 10}
    )
    ax.set(aspect="equal")
    center_circle = plt.Circle((0, 0), 0.25, color='white', alpha=0.3)
    ax.add_artist(center_circle)
    plt.tight_layout()
    st.pyplot(fig, clear_figure=True)

    if st.session_state.analyze_clicked and st.session_state.is_fake and not st.session_state.generated:
        st.markdown("###")
        if st.button("🛠️ Get the Real News", key="generate_btn"):
            st.session_state.real_version = generate_real_version(st.session_state.input_text)
            st.session_state.generated = True
            st.rerun()

# --- RIGHT SIDE: Input and Output ---
with col2:
    st.title("📰 AI News Detector")
    st.caption("Detect whether a news article is fake or real — and fix it if needed.")

    user_input = st.text_area("📝 Enter news content:", height=200, placeholder="Paste a news headline or article here...")

    if st.button("🔍 Analyze", key="analyze_btn"):
        if not user_input.strip():
            st.warning("Please enter some news content.")
        else:
            # 👉 Use actual backend classifier
            is_fake, confidence = classify_news(user_input)

            st.session_state.analyze_clicked = True
            st.session_state.generated = False
            st.session_state.confidence = confidence
            st.session_state.is_fake = is_fake
            st.session_state.input_text = user_input
            st.rerun()

    if st.session_state.analyze_clicked:
        st.subheader("🧠 Result")
        if st.session_state.is_fake and not st.session_state.generated:
            st.error(f"❌ This news is likely **Fake** ({st.session_state.confidence:.1%} confidence)")
        elif st.session_state.generated:
            st.success("✅ This is a trustworthy real version of the news.")

    if st.session_state.generated:
        st.subheader("📰 Realistic Version")
        st.success(st.session_state.real_version or "Generated news will appear here.")
