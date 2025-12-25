# AI Document Q&A System (RAG)

This project implements a Retrieval-Augmented Generation (RAG) based document question answering system.  
Users can upload PDF documents, ask questions, and retrieve the most relevant content using semantic search.

The system is fully local and does not rely on paid APIs.

---

## Features

- Upload PDF documents through a web interface  
- Semantic question answering from documents  
- Retrieval-based document summarization  
- Best-answer extraction from relevant content  
- Clean and minimal Streamlit UI  
- No external API dependency  

---

## Tech Stack

- Python  
- Streamlit  
- LlamaIndex  
- HuggingFace Sentence Transformers  
- Local vector storage  

---

## How It Works

- PDF text is extracted and converted into embeddings  
- User queries are embedded using the same model  
- Semantic similarity is used to retrieve relevant sections  
- The best matching content is displayed to the user  
- Summary is generated using retrieval-based techniques  

---

## Academic Explanation

This project demonstrates semantic retrieval for document-based question answering.  
HuggingFace embeddings are used to convert text into vector representations, and LlamaIndex retrieves the most relevant document sections based on user queries.

---

## Author

Khushi Katwe  
B.Tech – Information Science and Engineering  
REVA University
