import chromadb

from services.bm25_service import bm25_search


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(chunks, embeddings, filename):

    ids = [
        f"{filename}_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        {
            "source": filename,
            "chunk": i
        }
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    # Add the same chunks to BM25
    bm25_search.add_documents(
        chunks,
        metadatas
    )


def search_embeddings(query_embedding, top_k=5):

    return collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=top_k
    )


def get_all_documents():

    return collection.get()


def total_vectors():

    return collection.count()


def load_from_chroma():

    data = get_all_documents()

    documents = data.get("documents", [])
    metadatas = data.get("metadatas", [])

    if documents:
        bm25_search.add_documents(
            documents,
            metadatas
        )