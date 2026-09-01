import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.data.vector_store import VectorStore

sample_docs = [
    "Apple Inc. (AAPL) trailing P/E ratio is approximately 29.5 as of Q2 2026, above the tech sector average of 24.",
    "Microsoft (MSFT) reported Q2 2026 revenue growth of 14% YoY, driven by Azure cloud and AI services.",
    "Alphabet/Google (GOOGL) revenue grew 11% YoY in Q2 2026, with search ad revenue as the primary driver.",
    "Persistent inflation above 3% has historically compressed tech stock valuations by increasing discount rates on future earnings.",
    "Current market risks include elevated interest rates, AI-capex overbuild concerns, and geopolitical trade tensions."
]

if __name__ == "__main__":
    vs = VectorStore()
    vs.add_documents(sample_docs)
    print(f"Seeded {len(sample_docs)} documents.")