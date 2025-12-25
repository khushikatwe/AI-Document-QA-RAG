import streamlit as st
from pypdf import PdfReader
from openai import OpenAI

st.set_page_config(page_title="AI Document Assistant", layout="wide")

st.title("📄 AI Document Assistant")
st.write("Upload a PDF and ask questions")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask a question")
ask = st.button("Ask AI")

if ask:
    if not uploaded_file:
        st.warning("Upload a PDF first")
    elif not question:
        st.warning("Enter a question")
    else:
        with st.spinner("Thinking..."):
            # Read PDF text
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()

            # Groq via OpenAI-compatible API
            client = OpenAI(
                api_key=st.secrets["GROQ_API_KEY"],
                base_url="https://api.groq.com/openai/v1"
            )

            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "Answer only using the document."},
                    {
                        "role": "user",
                        "content": f"Document:\n{text}\n\nQuestion: {question}"
                    }
                ]
            )

            st.success("Answer")
            st.write(response.choices[0].message.content)
