import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="Document Reader", layout="wide")

st.title("📄 Document Reader")
st.write("Upload a PDF and see its content")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    if text.strip():
        st.success("PDF text extracted")
        st.write(text[:1500])
    else:
        st.error("No readable text found")
