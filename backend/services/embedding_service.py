from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):
    if not chunks:
        return []

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings