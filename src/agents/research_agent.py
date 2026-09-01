import os, json
from groq import Groq
from src.utils.prompt_templates import RESEARCH_AGENT_PROMPT

class ResearchAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def analyze_query(self, user_query: str) -> dict:
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": RESEARCH_AGENT_PROMPT},
                {"role": "user", "content": user_query}
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )
        try:
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            return {"key_concepts": [], "sources_to_query": [], "search_query": user_query}

