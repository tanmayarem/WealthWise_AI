import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from src.agents.research_agent import ResearchAgent
from src.agents.finance_analyst import FinanceAnalyst
from src.data.vector_store import VectorStore

st.set_page_config(page_title="WealthWise AI", page_icon="💰")
st.title("💰 WealthWise AI")
st.caption("Agentic Q&A for financial advisory — dual-agent RAG prototype")

@st.cache_resource
def load_components():
    return ResearchAgent(), FinanceAnalyst(), VectorStore()

research_agent, analyst_agent, vector_store = load_components()

query = st.text_input("Ask a financial question:", placeholder="What's the P/E ratio of Apple?")

if query:
    with st.spinner("Research Agent analyzing query..."):
        analysis = research_agent.analyze_query(query)
    with st.expander("🔍 Research Agent output"):
        st.json(analysis)

    with st.spinner("Retrieving relevant documents..."):
        docs = vector_store.query(analysis.get("search_query", query))

    with st.spinner("Finance Analyst synthesizing response..."):
        answer = analyst_agent.synthesize_response(query, docs)

    st.markdown(answer)