import streamlit as st
from llama_index.core import (
    StorageContext,
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
    load_index_from_storage
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os

# ---------------- SETTINGS ----------------
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
Settings.llm = None  # No LLM

DATA_DIR = "data"
STORAGE_DIR = "storage"

os.makedirs(DATA_DIR, exist_ok=True)

# ---------------- UI HEADER ----------------
st.set_page_config(
    page_title="AI Document QA",
    page_icon="📄",
    layout="wide"
)


# ---------------- PDF UPLOAD ----------------
uploaded_file = st.file_uploader("📤 Upload a PDF", type=["pdf"])

if uploaded_file:
    file_path = os.path.join(DATA_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully!")

    documents = SimpleDirectoryReader(DATA_DIR).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=STORAGE_DIR)

    st.info("📚 Document indexed. Ready for Q&A.")

st.divider()

# ---------------- SUMMARY BUTTON ----------------
if os.path.exists(STORAGE_DIR):
    if st.button("📝 Summarize Document"):
        storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
        index = load_index_from_storage(storage_context)

        retriever = index.as_retriever(similarity_top_k=5)
        nodes = retriever.retrieve("summary overview main topics")

        st.subheader("📌 Document Summary")
        for node in nodes:
            st.write("•", node.text)

st.divider()

# ---------------- QUESTION AREA ----------------
st.subheader("❓ Ask a Question")

query = st.text_input("Type your question here")

if query and os.path.exists(STORAGE_DIR):
    storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
    index = load_index_from_storage(storage_context)

    retriever = index.as_retriever(similarity_top_k=1)
    nodes = retriever.retrieve(query)

    if nodes:
        st.success("✅ Best Answer")
        st.write(nodes[0].text)
    else:
        st.warning("No relevant content found.")
