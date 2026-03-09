import streamlit as st

st.set_page_config(page_title="ORACLE", page_icon="🔮", layout="wide")

PAGES = ["Input", "Review", "Evaluation"]

st.sidebar.title("ORACLE")
st.sidebar.caption("AI Document Reasoning Engine")
page = st.sidebar.radio("Navigate", PAGES)

# ── Input ─────────────────────────────────────────────────────────────────────
if page == "Input":
    st.title("Submit Document")
    st.write("Upload a document or paste text to begin an ORACLE reasoning run.")

    upload = st.file_uploader("Upload document", type=["pdf", "txt", "docx"])
    text_input = st.text_area("Or paste document text here", height=300)
    company_name = st.text_input("Company name (for enrichment)")

    if st.button("Run ORACLE", type="primary"):
        if not (upload or text_input.strip()):
            st.error("Please provide a document or paste text.")
        else:
            st.info("Pipeline not yet connected — stub only.")

# ── Review ────────────────────────────────────────────────────────────────────
elif page == "Review":
    st.title("Review Reasoning Output")
    st.write("Inspect module-by-module reasoning results for a completed run.")

    run_id = st.number_input("Run ID", min_value=1, step=1)
    if st.button("Load Run"):
        st.info("API not yet connected — stub only.")

# ── Evaluation ────────────────────────────────────────────────────────────────
elif page == "Evaluation":
    st.title("Evaluation & Feedback")
    st.write("Review RQS scores and submit analyst feedback.")

    run_id = st.number_input("Run ID", min_value=1, step=1, key="eval_run_id")
    rating = st.slider("Overall Rating", min_value=1, max_value=5, value=3)
    comment = st.text_area("Comments")

    if st.button("Submit Feedback"):
        st.info("Feedback endpoint not yet connected — stub only.")
