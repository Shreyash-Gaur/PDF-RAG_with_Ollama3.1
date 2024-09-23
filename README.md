

---

# PDF-Based Question Answering with Retrieval-Augmented Generation (RAG)

This repository implements a question-answering system using **LangChain** and **Ollama embeddings**. The system answers questions by retrieving relevant contexts from PDF documents and generating responses using a **Retrieval-Augmented Generation (RAG)** approach.

## Project Overview

The project focuses on building a pipeline that loads, processes, and stores PDF documents for retrieval-based question answering. By combining **Ollama’s "llama3.1" model** and **Chroma vector storage**, it allows efficient similarity search and generation of accurate responses based on the context of the PDFs.

### Key Features

- **Retrieval-Augmented Generation (RAG):** A retrieval-based framework that retrieves relevant information from documents and generates context-based answers.
- **Ollama Embeddings:** Embeds PDF text chunks using Ollama's **llama3.1** model for effective vector representation.
- **Chroma Vector Store:** Stores document embeddings and enables similarity search to fetch the most relevant chunks.
- **PDF Processing:** Supports loading and chunking of PDF documents for storage and retrieval.
- **Test Framework:** Provides a script for testing the accuracy of the system's answers.

## What is Retrieval-Augmented Generation (RAG)?

RAG combines retrieval and generation to answer questions. It retrieves relevant document chunks based on a query and uses a language model to generate a response from the retrieved context. This approach ensures that the generated answer is grounded in the document contents.

### How the System Works

1. **Embedding Generation:**
   - Text chunks from PDFs are embedded using **Ollama's "llama3.1"** model, which converts text into vector representations.
   
2. **Vector Storage:**
   - The embeddings are stored in **Chroma**, a vector database that enables efficient retrieval of document chunks similar to a user query.

3. **Question Answering:**
   - When a query is provided, the system retrieves the most relevant document chunks using similarity search, and the Ollama model generates a response based on the context of the retrieved chunks.

4. **Testing:**
   - The system's accuracy is evaluated by running test cases using predefined questions and expected answers.

## Repository Structure

- **`get_embedding_function.py`**: Defines the function to create embeddings using the Ollama model.
- **`populate_database.py`**: Loads and processes PDF files, splitting them into chunks and storing them in the Chroma vector store.
- **`query_data.py`**: Queries the vector store and generates answers based on the retrieved context.
- **`test_rag.py`**: Script to test the system’s question-answering performance using predefined queries.

## Files Overview

### `get_embedding_function.py`

This file defines the function to initialize **Ollama LLaMA embeddings**.

```python
from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="llama3.1")
    return embeddings
```

### `populate_database.py`

This script loads PDFs, splits them into chunks, and stores the chunks in the **Chroma** vector store for retrieval.

- Use `--reset` to clear and rebuild the database.
- Loads PDFs from the `data` directory.
- Splits documents into chunks and assigns unique IDs.

### `query_data.py`

This script queries the Chroma database with a user-provided question. It retrieves the most relevant document chunks and generates a response using the Ollama model.

- Retrieves context from stored PDFs.
- Constructs a prompt for the Ollama model to generate a response.
- Provides the answer along with document sources.

### `test_rag.py`

This script contains predefined test cases to evaluate the performance of the RAG system.

- It tests the system’s response accuracy by comparing actual answers to expected answers.


## Example Usage

1. **Populating the Database:**

```bash
python populate_database.py --reset
```

This command processes PDFs from the `data` directory and stores their embeddings in the Chroma database.

2. **Querying the System:**


```bash
python query_data.py "How many days did the Kurukshetra war last?"
```

Expected response: "15 days".

This retrieves the relevant context from the PDFs and generates a response using the Ollama model.

3. **Running Tests:**

```bash
python test_rag.py
```

Executes test cases to evaluate the accuracy of the system.

## Future Work

- **Support for Additional Formats:** Extend the system to process Word documents and text files.
- **Advanced Answer Generation:** Experiment with more advanced RAG frameworks or models for enhanced answer quality.
- **Improved Testing:** Implement more complex evaluation metrics to validate system performance.

## Conclusion

This project demonstrates how **LangChain**, **Ollama embeddings**, and **Chroma** can be used in combination for document-based question answering. It leverages retrieval-augmented generation to provide context-grounded answers, with future potential for broader use cases in document search and QA systems.

---

