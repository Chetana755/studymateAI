from rank_bm25 import BM25Okapi
import re


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


class BM25Search:

    def __init__(self):
        self.documents = []
        self.metadatas = []
        self.bm25 = None

    def add_documents(self, documents, metadatas):

        self.documents.extend(documents)
        self.metadatas.extend(metadatas)

        tokenized_documents = [
            tokenize(doc)
            for doc in self.documents
        ]

        if tokenized_documents:
            self.bm25 = BM25Okapi(
                tokenized_documents
            )

    def search(self, query, top_k=5):

        if self.bm25 is None or not self.documents:
            return [], []

        query_tokens = tokenize(query)

        if not query_tokens:
            return [], []

        scores = self.bm25.get_scores(
            query_tokens
        )

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        documents = []
        metadatas = []

        for i in ranked_indices:

            if scores[i] > 0:

                documents.append(
                    self.documents[i]
                )

                metadatas.append(
                    self.metadatas[i]
                )

        return documents, metadatas


bm25_search = BM25Search()