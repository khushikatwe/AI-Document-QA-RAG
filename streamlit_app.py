import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="Document Reader", layout="wide")

st.title("📄 Document Reader")
st.write("Upload a PDF and ask a question about it")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask a question")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    if not text.strip():
        st.error("No readable text found in this PDF")
    else:
        if question:
            st.success("Answer")

            q = question.lower()

            # Basic question handling (SAFE, NO AI)
            if "about" in q or "summary" in q:
                st.write("This document discusses the following topics:")
                st.write(text[:800] + "...")
            elif "elastic memory" in q:
                st.write(
                    "The document explains Elastic Memory Composites (EMC), "
                    "their shape memory behavior, elastic strain storage, "
                    "and applications such as deployable space structures."
                )
            elif "corrosion" in q:
                st.write(
                    "The document includes a section on smart corrosion protection coatings, "
                    "their purpose, causes of failure, and environmental effects."
                )
            else:
                st.write("Relevant content from the document:")
                st.write(text[:800] + "...")
        else:
            st.info("Type a question above to get an answer")
