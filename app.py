import streamlit as st
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------
def load_css():
    css_path = Path("assets/style.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
<h1 style="text-align:center;">📄 AI Document Assistant</h1>
<p style="text-align:center; font-size:18px; color:#6B7280;">
Upload PDFs • Ask questions • Get instant answers
</p>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# MAIN LAYOUT
# --------------------------------------------------
left, right = st.columns([1, 2])

with left:
    st.markdown("### 📂 Upload Document")
    uploaded_file = st.file_uploader(
        "Upload a PDF file",
        type=["pdf"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="font-size:14px; color:#6B7280;">
    • Supports PDF files only  
    • Best for notes, reports, textbooks  
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("### 💬 Ask a Question")
    question = st.text_input(
        "Type your question here",
        placeholder="e.g. What is the main topic of this document?"
    )

    ask_btn = st.button("✨ Ask AI")

# --------------------------------------------------
# LOGIC (PLACEHOLDER – SAFE)
# --------------------------------------------------
if ask_btn:
    if uploaded_file is None:
        st.warning("⚠️ Please upload a PDF first.")
    elif question.strip() == "":
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("🤖 Thinking..."):
            # ---- PLACEHOLDER RESPONSE ----
            # Replace this later with your RAG / LLM logic
            st.success("✅ Answer")
            st.write(
                "This is a sample response. "
                "Connect your RAG / LLM logic here to generate real answers."
            )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<hr>
<p style="text-align:center; font-size:13px; color:#9CA3AF;">
Built with ❤️ using Streamlit • AI-powered Document Q&A
</p>
""", unsafe_allow_html=True)
