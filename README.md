# WealthWise AI: Agentic Q&A System for Financial Advisory

## 🎯 Project Vision

Building a conversational AI prototype that combines Retrieval-Augmented Generation (RAG) with agentic workflow design for finance domain Q&A.

## 🏗️ Architecture

```
User Query → Research Agent → Vector DB → Finance Analyst → Response
                ↓                ↓              ↓
           Query Analysis    Document      Synthesis
           Source Selection  Retrieval     with Context
```

## 🧠 Dual-Agent Design

### 1. Research Agent
- Analyzes user queries to identify key financial concepts
- Determines optimal data sources to query
- Extracts relevant financial metrics and parameters

### 2. Finance Analyst Agent
- Synthesizes responses using retrieved financial data
- Employs optimized system prompts with few-shot examples
- Structured output with: Summary → Key Findings → Recommendations → Disclaimer

## 🔧 Tech Stack

- **Framework:** Python
- **Vector DB:** ChromaDB / FAISS
- **LLM:** Groq API (Mixtral-8x7b)
- **Orchestration:** LangChain (optional)
- **UI:** Streamlit

## 📁 Planned Structure

```
wealthwise-ai/
├── src/
│   ├── agents/
│   │   ├── research_agent.py
│   │   └── finance_analyst.py
│   ├── data/
│   │   └── vector_store.py
│   ├── utils/
│   │   └── prompt_templates.py
│   └── app.py
├── data/
│   └── sample_financial_docs/
├── requirements.txt
└── .env
```

## 💡 Key Features

- **Agentic Decision Chain:** System decides which data sources to query based on user questions
- **Prompt Engineering:** Role-based instruction, output format control, context window management
- **Lightweight RAG:** Efficient retrieval from document corpus
- **Multi-Agent Foundation:** Laying groundwork for enterprise finance orchestration

## 🎯 Sample Use Cases

- "What's the P/E ratio of Apple?"
- "How has inflation affected tech stocks?"
- "Compare revenue growth of Microsoft vs Google"
- "What are the risks in the current market?"

## 📝 Prompt Engineering Approach

- Role-based system prompts with clear responsibilities
- Few-shot examples for consistent output formatting
- Structured response templates with financial disclaimers
- Temperature control for response consistency

## 🚀 Next Steps

1. Implement prompt templates with few-shot examples
2. Set up ChromaDB vector store with sample financial documents
3. Build Research Agent with Groq API integration
4. Create Finance Analyst Agent for response synthesis
5. Develop Streamlit UI for user interaction
6. Test agentic workflow with sample queries
7. Optimize retrieval and response quality

---

*Work in Progress - Building step by step*
```