"""Streamlit interface for the Threat-Intel RAG Assistant."""
import streamlit as st
from dotenv import load_dotenv
from src.app_runtime import ROOT, configure_credentials, index_count, initialize_index

st.set_page_config(page_title="Threat-Intel RAG Assistant", page_icon="🛡️", layout="wide")
load_dotenv(ROOT / ".env")
missing = configure_credentials(st.secrets)

st.title("🛡️ Threat-Intel RAG Assistant")
st.caption("Ask questions about the indexed Unit 42 reports and inspect the supporting excerpts.")


def choose_example(question):
    st.session_state["query"] = question


@st.cache_resource
def load_graph():
    from src.graph import app
    return app


with st.sidebar:
    st.header("About this prototype")
    st.write("LangGraph rewrites the query, retrieves excerpts, reranks them with Cohere, "
             "generates an answer, and runs a model self-check with up to two attempts.")
    st.write("Routing currently uses simple retrieval. Multi-hop reasoning is not implemented.")
    st.write("Answer correctness and citation quality are under evaluation.")
    st.link_button("GitHub repository", "https://github.com/AimanManzoor/Threat-intel-rag-assistant")
    st.subheader("Try a question")
    for question in [
        "According to the RansomHouse report, which group operates RansomHouse?",
        "What bootkit mechanism is associated with RayInitiator in the Cisco ASA report?",
        "What was Anthropic's revenue in 2025?",
    ]:
        st.button(question, on_click=choose_example, args=(question,), use_container_width=True)

if missing:
    st.info("Configure these keys in your local .env or Streamlit app secrets: " + ", ".join(missing))

try:
    count = index_count()
except Exception as error:
    count = 0
    st.error(f"Search index could not be opened ({type(error).__name__}).")

if count:
    st.success(f"Search index ready: {count} excerpts.")
else:
    st.warning("Search index is missing or incomplete. Initialize it before asking questions.")
    st.caption("Initialization embeds the processed reports using Cohere and may incur API charges. "
               "It may be needed again after cloud storage is reset. No LLM contexts are generated.")
    if st.button("Initialize search index", disabled=bool(missing)):
        try:
            with st.spinner("Preparing report embeddings..."):
                initialize_index()
            st.rerun()
        except Exception as error:
            st.error(f"Index initialization failed ({type(error).__name__}). "
                     "Check credentials and provider availability before retrying.")

with st.form("question_form"):
    query = st.text_input("Your question", key="query", max_chars=1000,
                          placeholder="Ask about the indexed Unit 42 reports...")
    submitted = st.form_submit_button("Run query", type="primary", disabled=bool(missing) or not count)

if submitted:
    st.session_state.pop("result", None)
    if not query.strip():
        st.warning("Enter a question first.")
    else:
        try:
            with st.spinner("Retrieving evidence and preparing an answer..."):
                st.session_state["result"] = load_graph().invoke({"query": query.strip(), "attempts": 0})
        except Exception as error:
            if getattr(error, "status_code", None) == 429:
                st.error("Provider rate limit reached. Wait before trying again.")
            else:
                st.error(f"Query failed ({type(error).__name__}). Check provider availability and configuration.")

result = st.session_state.get("result")
if result:
    st.subheader("Answer")
    st.write(result.get("answer", "No answer returned."))
    columns = st.columns(4)
    columns[0].metric("Route", result.get("route", "unknown"))
    columns[1].metric("Model self-score", f"{result.get('confidence', 0.0):.2f}")
    columns[2].metric("Attempts", result.get("attempts", 0))
    columns[3].metric("Citation IDs", len(result.get("citations", [])))
    st.caption("The model self-score is not a measured accuracy or calibrated probability.")
    documents = result.get("reranked", [])
    valid_ids = {doc.metadata.get("doc_id") for doc in documents}
    citations = result.get("citations", [])
    if any(citation not in valid_ids for citation in citations):
        st.warning("Some citation IDs do not exactly match the retrieved source IDs. Verify the answer below.")
    if citations:
        st.subheader("Citation IDs returned")
        for citation in citations:
            st.code(citation, language=None)
    with st.expander("Inspect rewritten query and supporting excerpts"):
        st.write("Rewritten query:", result.get("rewritten", ""))
        for number, document in enumerate(documents, 1):
            st.text(f"{number}. {document.metadata.get('doc_id', 'unknown')}")
            st.text(document.metadata.get("raw_chunk", document.page_content))
