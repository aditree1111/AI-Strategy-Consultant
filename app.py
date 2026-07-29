import streamlit as st
from pathlib import Path

from utils.pdf_reader import extract_text_from_pdf
from utils.text_processing import clean_text, chunk_text
from utils.vector_store import build_vector_store, search_chunks
from utils.gemini import ask_gemini

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Strategy Consultant",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# Upload Folder
# ==========================================

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

# ==========================================
# Title
# ==========================================

st.title("📊 AI Strategy Consultant")

st.markdown("""
Upload any public company's **Annual Report (PDF)** and ask AI strategic questions.

### Supported Companies

- Apple
- Microsoft
- Amazon
- Tesla
- Reliance
- Infosys
- TCS
- Any public company
""")

st.divider()

# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("Navigation")
st.sidebar.success("Step 1: Upload Annual Report")

# ==========================================
# Upload PDF
# ==========================================

uploaded_file = st.file_uploader(
    "📄 Upload Annual Report",
    type=["pdf"]
)

# ==========================================
# Main Logic
# ==========================================

if uploaded_file is not None:

    file_name = uploaded_file.name
    file_size = uploaded_file.size / (1024 * 1024)

    file_path = UPLOAD_FOLDER / file_name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Annual Report Uploaded Successfully")

    try:

        # ----------------------------
        # Read PDF
        # ----------------------------

        text, total_pages = extract_text_from_pdf(file_path)

        # ----------------------------
        # Clean Text
        # ----------------------------

        text = clean_text(text)

        # ----------------------------
        # Chunk Text
        # ----------------------------

        chunks = chunk_text(text)

        # ----------------------------
        # Build Vector Database
        # ----------------------------

        with st.spinner("Building AI Knowledge Base..."):
            build_vector_store(chunks)

        st.success("✅ Knowledge Base Ready")

        # ----------------------------
        # Statistics
        # ----------------------------

        st.subheader("📊 PDF Statistics")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("Pages", total_pages)

        with col2:
            st.metric("Words", len(text.split()))

        with col3:
            st.metric("Characters", len(text))

        with col4:
            st.metric("Chunks", len(chunks))

        with col5:
            st.metric("Knowledge Base", "Ready")

        st.divider()

        # ----------------------------
        # Preview
        # ----------------------------

        st.subheader("📄 Text Preview")

        st.text_area(
            "First 2000 Characters",
            text[:2000],
            height=250
        )

        st.divider()

        # ----------------------------
        # Chunk Preview
        # ----------------------------

        st.subheader("🧩 First Chunk")

        st.text_area(
            "Chunk 1",
            chunks[0],
            height=200
        )

        st.divider()

        # ----------------------------
        # Ask Questions
        # ----------------------------

        st.header("💬 Ask the AI")

        question = st.text_input(
            "Ask anything about the company..."
        )

        if st.button("Generate Answer"):

            if question.strip() == "":
                st.warning("Please enter a question.")

            else:

                with st.spinner("Searching Annual Report..."):

                    docs = search_chunks(question)

                    context = "\n\n".join(docs)

                    answer = ask_gemini(
                        context,
                        question
                    )

                st.subheader("Answer")

                st.write(answer)
        st.divider()

        st.header("🏢 Company Analysis")

        # ----------------------------
        # Company Overview
        # ----------------------------

        if st.button("Generate Company Overview"):

            prompt = """
            Provide:
            - Company Overview
            - Industry
            - Business Model
            - Revenue Drivers
            - Competitive Position
            """

            docs = search_chunks(prompt)
            context = "\n\n".join(docs)

            answer = ask_gemini(context, prompt)

            st.subheader("Company Overview")
            st.write(answer)

        # ----------------------------
        # SWOT Analysis
        # ----------------------------

        if st.button("Generate SWOT Analysis"):

            prompt = """
            Generate a SWOT Analysis.

            Include:
            - Strengths
            - Weaknesses
            - Opportunities
            - Threats
            """

            docs = search_chunks(prompt)
            context = "\n\n".join(docs)

            answer = ask_gemini(context, prompt)

            st.subheader("SWOT Analysis")
            st.write(answer)

        # ----------------------------
        # Business Risks
        # ----------------------------

        if st.button("Identify Business Risks"):

            prompt = """
            Identify the company's biggest business risks.
            """

            docs = search_chunks(prompt)
            context = "\n\n".join(docs)

            answer = ask_gemini(context, prompt)

            st.subheader("Business Risks")
            st.write(answer)

        # ----------------------------
        # Growth Opportunities
        # ----------------------------

        if st.button("Growth Opportunities"):

            prompt = """
            Identify future growth opportunities.
            """

            docs = search_chunks(prompt)
            context = "\n\n".join(docs)

            answer = ask_gemini(context, prompt)

            st.subheader("Growth Opportunities")
            st.write(answer)

        # ----------------------------
        # Strategic Recommendations
        # ----------------------------

        if st.button("Strategic Recommendations"):

            prompt = """
            Act as a Bain & Company consultant.

            Recommend five strategic initiatives.
            """

            docs = search_chunks(prompt)
            context = "\n\n".join(docs)

            answer = ask_gemini(context, prompt)

            st.subheader("Strategic Recommendations")
            st.write(answer)

    except Exception as e:

        st.error("An error occurred while processing the PDF.")
        st.exception(e)

else:

    st.info("⬆️ Upload a PDF annual report to begin.")