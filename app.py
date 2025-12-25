import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="Document Reader", layout="wide")

st.title("📄 Document Reader")
st.write("Upload a PDF and ask a basic question")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask a question")
ask = st.button("Submit")

if ask:
    if not uploaded_file:
        st.warning("Please upload a PDF")
    elif not question:
        st.warning("Please type a question")
    else:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()

        if not text.strip():
            st.error("No readable text found in this PDF")
        else:
            st.success("Answer")
            st.write(text[:1200] + "...")
