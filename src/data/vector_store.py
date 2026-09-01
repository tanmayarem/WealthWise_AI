import chromadb

class VectorStore:
    def __init__(self, path="./chroma_db"):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection("financial_docs")

    def add_documents(self, docs: list[str], ids: list[str] = None):
        ids = ids or [f"doc_{i}" for i in range(len(docs))]
        self.collection.add(documents=docs, ids=ids)

    def query(self, query_text: str, n_results: int = 3):
        results = self.collection.query(query_texts=[query_text], n_results=n_results)
        return results["documents"][0] if results["documents"] else []