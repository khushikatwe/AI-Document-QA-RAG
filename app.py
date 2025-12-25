import streamlit as st
from groq import Groq
from pypdf import PdfReader

st.set_page_config(page_title="AI Document Assistant", layout="wide")

st.title("📄 AI Document Assistant")
st.write("Upload a PDF and ask questions")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask a question")
ask = st.button("Ask AI")

if ask:
    if not uploaded_file:
        st.warning("Upload a PDF")
    elif not question:
        st.warning("Enter a question")
    else:
        with st.spinner("Thinking..."):
            # Read PDF text
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            # Call LLM
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "system",
                        "content": "Answer the question using the given document only."
                    },
                    {
                        "role": "user",
                        "content": f"Document:\n{text}\n\nQuestion: {question}"
                    }
                ],
            )

            st.success("Answer")
            st.write(completion.choices[0].message.content)
