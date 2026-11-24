"""Opt-in budgeted assistant workspace; paid operations require explicit selection."""
import json
import os

from src.budgeted_rag import run_budgeted
from src.app_runtime import configure_credentials
from dotenv import load_dotenv


def paid_enabled():
    import streamlit as st
    enabled = os.getenv("THREAT_ENABLE_PAID_RAG", "").lower() in {"1", "true"}
    if not enabled:
        try:
            value = st.secrets["THREAT_ENABLE_PAID_RAG"]
            enabled = value is True or str(value).lower() in {"1", "true"}
        except (KeyError, FileNotFoundError):
            pass
    return enabled


def render_budgeted(root):
    import streamlit as st

    st.subheader("Budgeted evidence-first assistant")
    st.caption("Exact-CVE source lookup: zero provider calls. Optional RAG: at most three provider operations.")
    st.warning("Quote membership is not proof that a quote supports a claim. Generated claims require human review.")
    enabled = paid_enabled()
    if not enabled:
        st.caption("Paid RAG is disabled by server configuration. Exact-CVE source lookup remains available.")
    with st.form("budgeted_assistant"):
        question = st.text_input("Question for budgeted assistant", max_chars=1000)
        paid = st.checkbox("Allow paid RAG for non-CVE questions", value=False, disabled=not enabled)
        model = st.text_input("Available Anthropic model ID", value=os.getenv("ANTHROPIC_MODEL", ""), max_chars=107,
                              help="Select a model available in your own account; availability is not verified offline.")
        submitted = st.form_submit_button("Run budgeted request")
    paid = bool(paid and enabled)
    key = (question.strip(), paid, model.strip())
    if submitted:
        if paid:
            load_dotenv(root / ".env")
            configure_credentials(st.secrets)
        st.session_state["budgeted_result"] = (
            key, run_budgeted(question.strip(), allow_paid=paid, model=model.strip(), root=root))
    stored = st.session_state.get("budgeted_result")
    if stored is None or stored[0] != key:
        return
    report = stored[1]
    st.write("Status:", report["status"])
    st.info(report["message"])
    if "source_lookup" in report:
        for source in report["source_lookup"]["sources"]:
            st.text(source["report_title"])
            st.code(source["source_file"] + ":" + source["source_location"], language=None)
            st.text(source["excerpt"])
    for claim in report["claims"]:
        st.markdown("**Candidate claim — review required**")
        st.text(claim["text"])
        st.code(claim["source_id"], language=None)
        st.text("Supporting quote: " + claim["quote"])
    left, right = st.columns(2)
    left.metric("Provider operations attempted", report["provider_calls"])
    right.metric("Generation context characters", report["context_chars"])
    st.caption("Usage is provider-reported when available. No dollar saving, accuracy gain or hard dollar cap is established.")
    with st.expander("Inspect evidence, request limits and usage"):
        st.json(report)
    st.download_button("Download budgeted request receipt", json.dumps(report, indent=2),
                       file_name="budgeted_request.json", mime="application/json")
