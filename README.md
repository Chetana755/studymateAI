````markdown
# StudyMate AI

## RAG-Based AI Study Assistant

StudyMate AI is an AI-powered study assistant that allows students to upload study materials such as PDFs and ask questions about their content.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate contextual answers using Google's Gemini model.

It also supports multiple study modes, including Normal, Summary, Exam, and Quiz.

## Features

- PDF document upload
- PDF text extraction
- Document chunking
- Semantic search using vector embeddings
- ChromaDB vector storage
- Keyword search using BM25
- Hybrid retrieval using semantic and keyword search
- Duplicate chunk removal
- Gemini-powered answer generation
- Source attribution
- Multiple study modes
  - Normal
  - Summary
  - Exam
  - Quiz
- RAGAS-based evaluation
- FastAPI backend
- React frontend
- Markdown-formatted answers
- Retrieval statistics

## System Architecture

```text
                    React Frontend
                          |
                          v
                    FastAPI Backend
                          |
              +-----------+-----------+
              |                       |
              v                       v
       Semantic Search          Keyword Search
         ChromaDB                    BM25
              |                       |
              +-----------+-----------+
                          |
                          v
                 Hybrid Retrieval
                          |
                          v
                Duplicate Removal
                          |
                          v
                   Prompt Builder
                          |
                          v
                    Gemini LLM
                          |
                          v
                  Answer + Sources
                          |
                          v
                    React Frontend
````

## RAG Pipeline

### 1. Document Upload

The user uploads a PDF through the React frontend.

### 2. Text Extraction

The backend extracts text from the uploaded PDF.

### 3. Chunking

The extracted text is divided into smaller chunks so that relevant sections can be retrieved efficiently.

### 4. Embeddings

Each document chunk is converted into a vector representation using a sentence-transformer embedding model.

### 5. Vector Storage

The document chunks, embeddings, and metadata are stored in ChromaDB.

### 6. Semantic Retrieval

When the user asks a question, the question is converted into an embedding.

ChromaDB retrieves the chunks that are semantically similar to the question.

### 7. Keyword Retrieval

BM25 performs keyword-based retrieval over the document chunks.

This is useful when the question contains specific technical terms.

### 8. Hybrid Retrieval

The semantic and keyword results are combined.

Duplicate chunks are removed, and the most relevant unique chunks are used as context for answer generation.

The system retrieves up to 8 unique chunks for the final context.

### 9. Study Mode Detection

The system supports different study modes that control how the retrieved information is presented.

### 10. Prompt Construction

The question, retrieved context, and selected study mode are passed to the prompt builder.

### 11. Answer Generation

Gemini generates the final answer using the retrieved context.

### 12. Source Attribution

The response includes metadata identifying the source document and retrieved chunks.

## Study Modes

### Normal

Provides a detailed explanation based on the uploaded study material.

### Summary

Produces a concise explanation containing important definitions, concepts, examples, and key points.

### Exam

Structures the response to help students prepare for examination-style questions.

### Quiz

Generates quiz-style content based on the retrieved study material.

## Hybrid Retrieval

StudyMate uses two complementary retrieval approaches.

### Semantic Search

Semantic search uses embeddings to understand the meaning of a question rather than relying only on exact word matches.

For example:

```text
What does React useState do?
```

can retrieve information related to:

```text
Manage component state using useState
```

even if the wording is different.

### BM25 Keyword Search

BM25 performs keyword-based retrieval.

This is particularly useful for technical terms such as:

```text
useState
useReducer
Context API
useEffect
```

### Combined Retrieval

The results from ChromaDB and BM25 are combined and duplicate chunks are removed.

Example response metadata:

```json
{
  "semantic_results": 5,
  "keyword_results": 5,
  "combined_results": 8
}
```

## RAG Evaluation

StudyMate uses RAGAS to evaluate the RAG pipeline.

The evaluation dataset contains questions and expected answers.

The current evaluation uses:

* Faithfulness
* Answer Relevancy

Example evaluation questions include:

```text
What is prompt engineering?
What is zero-shot prompting?
What is few-shot prompting?
What is Chain-of-Thought prompting?
What is ReAct prompting?
```

Run the evaluation with:

```bash
python evaluation/evaluate.py
```

## Technology Stack

### Frontend

* React
* Vite
* JavaScript
* Axios
* React Markdown
* remark-gfm

### Backend

* Python
* FastAPI
* Uvicorn

### AI and Machine Learning

* Google Gemini
* Sentence Transformers
* Retrieval-Augmented Generation
* RAGAS

### Retrieval

* ChromaDB
* BM25
* rank-bm25

### Document Processing

* PDF text extraction
* Document chunking

## Project Structure

```text
studymate/
|
├── backend/
|   |
|   ├── app.py
|   |
|   ├── routes/
|   |   ├── upload.py
|   |   └── search.py
|   |
|   ├── services/
|   |   ├── rag_service.py
|   |   ├── chroma_service.py
|   |   ├── bm25_service.py
|   |   ├── embedding_service.py
|   |   ├── gemini_service.py
|   |   ├── prompt_service.py
|   |   ├── intent_service.py
|   |   └── pdf_service.py
|   |
|   ├── evaluation/
|   |   ├── evaluate.py
|   |   └── dataset.json
|   |
|   └── requirements.txt
|
├── frontend/
|   |
|   ├── src/
|   |   ├── components/
|   |   |   ├── ChatBox.jsx
|   |   |   ├── FileUpload.jsx
|   |   |   └── AnswerCard.jsx
|   |   |
|   |   ├── pages/
|   |   |   └── Home.jsx
|   |   |
|   |   ├── services/
|   |   |   └── api.js
|   |   |
|   |   ├── App.jsx
|   |   └── main.jsx
|   |
|   └── package.json
|
├── .gitignore
└── README.md
```

## Installation

### Prerequisites

Make sure the following are installed:

* Python 3.12+
* Node.js
* npm
* Google Gemini API key

## Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `backend` directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Start the backend:

```bash
uvicorn app:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Frontend Setup

Open a new terminal and navigate to the frontend:

```bash
cd frontend
```

Install the dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at the URL provided by Vite, usually:

```text
http://localhost:5173
```

## Environment Variables

API keys should never be committed to GitHub.

The local `.env` file should contain:

```env
GEMINI_API_KEY=your_api_key_here
```

A `.env.example` file can be created for other developers:

```env
GEMINI_API_KEY=
```

## Example Usage

Upload a PDF containing study material.

Then ask:

```text
What is useState?
```

Select a study mode such as:

```text
Normal
```

StudyMate retrieves relevant chunks from the uploaded documents and generates an answer using Gemini.

The same question can then be asked using:

```text
Summary
Exam
Quiz
```

to receive the answer in different formats.

## Example API Response

A typical `/chat` response contains:

```json
{
  "question": "What is useState?",
  "mode": "normal",
  "answer": "Generated answer based on retrieved context",
  "sources": [
    {
      "source": "React_Hooks_Practice_Questions.pdf",
      "chunk": 1
    }
  ],
  "retrieval": {
    "semantic_results": 5,
    "keyword_results": 5,
    "combined_results": 8
  }
}
```

## Retrieval Information

The API exposes retrieval statistics for each question.

For example:

```json
{
  "semantic_results": 5,
  "keyword_results": 5,
  "combined_results": 8
}
```

Where:

* `semantic_results` is the number of results retrieved through ChromaDB.
* `keyword_results` is the number of results retrieved through BM25.
* `combined_results` is the number of unique chunks remaining after combining both retrieval methods.

## Security

The following files and directories are excluded from Git:

```text
.env
venv/
node_modules/
chroma_db/
uploads/
config.txt
```

API keys and other sensitive configuration values should never be committed to the repository.

## Future Improvements

* Document-specific retrieval filtering
* Better chunk ranking and reranking
* Conversation history
* Persistent user sessions
* Flashcard generation
* Student progress tracking
* Additional RAGAS evaluation metrics
* Improved PDF and table extraction
* Streaming responses
* Authentication
* Cloud deployment
* Improved document citation and source highlighting

## Author

Chetana Parakala

StudyMate AI was built as an AI-powered study assistant using Retrieval-Augmented Generation, hybrid search, and Gemini.

```
```
