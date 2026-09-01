import os
from groq import Groq
from src.utils.prompt_templates import FINANCE_ANALYST_PROMPT

class FinanceAnalyst:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def synthesize_response(self, query: str, retrieved_docs: list[str]) -> str:
        context = "\n".join(f"- {d}" for d in retrieved_docs) or "No relevant documents found."
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": FINANCE_ANALYST_PROMPT},
                {"role": "user", "content": f"Question: {query}\n\nContext:\n{context}"}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

