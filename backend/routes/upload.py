import os
import shutil

from fastapi import APIRouter, File, UploadFile
from services.chroma_service import store_embeddings, total_vectors
from services.chunk_service import chunk_text
from services.embedding_service import generate_embeddings
from services.pdf_service import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed"}

    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text_from_pdf(file_path)

    if not text or not text.strip():
        return {
            "error": "No text could be extracted from this PDF."
        }

    print(f"Text length: {len(text)}")

    # Split into chunks
    chunks = chunk_text(text)

    if len(chunks) == 0:
        return {
            "error": "No chunks were generated.",
            "text_length": len(text)
        }

    print(f"Total chunks: {len(chunks)}")

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    if len(embeddings) == 0:
        return {
            "error": "Embedding generation failed."
        }

    print(f"Embedding shape: {embeddings.shape}")

    # Store in ChromaDB
    store_embeddings(
        chunks=chunks,
        embeddings=embeddings,
        filename=file.filename
    )

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "text_length": len(text),
        "total_chunks": len(chunks),
        "vectors_in_database": total_vectors()
    }