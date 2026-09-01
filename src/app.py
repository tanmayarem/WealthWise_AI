import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from src.agents.research_agent import ResearchAgent
from src.agents.finance_analyst import FinanceAnalyst
from src.data.vector_store import VectorStore

st.set_page_config(page_title="WealthWise AI", page_icon="💰")
st.title(" WealthWise AI 💰")
st.caption("Agentic Q&A for financial advisory — dual-agent RAG prototype")

@st.cache_resource
def load_components():
    return ResearchAgent(), FinanceAnalyst(), VectorStore()
