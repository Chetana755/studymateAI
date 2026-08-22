from services.embedding_service import model
from services.chroma_service import search_embeddings
from services.bm25_service import bm25_search
from services.gemini_service import generate_answer
from services.intent_service import detect_intent
from services.prompt_service import build_prompt


def ask_question(question, mode=None):

    # -----------------------------------------
    # 1. Generate embedding for the question
    # -----------------------------------------

    query_embedding = model.encode(question)

    # -----------------------------------------
    # 2. Semantic search using ChromaDB
    # -----------------------------------------

    chroma_results = search_embeddings(
        query_embedding,
        top_k=5
    )

    chroma_documents = chroma_results["documents"][0]
    chroma_metadata = chroma_results["metadatas"][0]

    # -----------------------------------------
    # 3. Keyword search using BM25
    # -----------------------------------------

    bm25_documents, bm25_metadata = bm25_search.search(
        question,
        top_k=5
    )

    # -----------------------------------------
    # 4. Combine ChromaDB + BM25 results
    # -----------------------------------------

    combined = []

    for document, metadata in zip(
        chroma_documents,
        chroma_metadata
    ):
        combined.append(
            (document, metadata)
        )

    for document, metadata in zip(
        bm25_documents,
        bm25_metadata
    ):
        combined.append(
            (document, metadata)
        )

    # -----------------------------------------
    # 5. Remove duplicate chunks
    # -----------------------------------------

    unique_documents = []
    unique_metadata = []
    seen = set()

    for document, metadata in combined:

        if document not in seen:
            seen.add(document)

            unique_documents.append(document)
            unique_metadata.append(metadata)

    # Keep maximum 8 unique chunks
    unique_documents = unique_documents[:8]
    unique_metadata = unique_metadata[:8]

    # -----------------------------------------
    # 6. Build context for Gemini
    # -----------------------------------------

    context = "\n\n".join(unique_documents)

    # -----------------------------------------
    # 7. Determine study mode
    # -----------------------------------------

    if not mode:
        mode = detect_intent(question)

    # -----------------------------------------
    # 8. Build prompt
    # -----------------------------------------

    prompt = build_prompt(
        question=question,
        context=context,
        mode=mode
    )

    # -----------------------------------------
    # 9. Generate answer
    # -----------------------------------------

    answer = generate_answer(prompt)

    # -----------------------------------------
    # 10. Return response
    # -----------------------------------------

    return {
        "question": question,
        "mode": mode,
        "answer": answer,

        # Metadata used for displaying sources
        "sources": unique_metadata,

        # Actual retrieved chunks used by Gemini
        # Required for RAGAS evaluation
        "retrieved_contexts": unique_documents,

        # Retrieval statistics
        "retrieval": {
            "semantic_results": len(chroma_documents),
            "keyword_results": len(bm25_documents),
            "combined_results": len(unique_documents)
        }
    }