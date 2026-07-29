from utils.rag import create_vector_store
import streamlit as st
from pathlib import Path
from utils.pdf_reader import extract_text_from_pdf
from utils.text_processing import clean_text, chunk_text

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="AI Strategy Consultant",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# Create Upload Folder
# ==========================================
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

# ==========================================
# App Title
# ==========================================
st.title("📊 AI Strategy Consultant")

st.markdown("""
Upload any public company's **Annual Report (PDF)** to begin AI-powered strategic analysis.

### Supported Companies
- Apple
- Microsoft
- Amazon
- Tesla
- Reliance
- Infosys
- TCS
- Any other public company
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
    "📄 Upload Annual Report (PDF)",
    type=["pdf"]
)

# ==========================================
# Process Uploaded File
# ==========================================
if uploaded_file is not None:

    # File Details
    file_name = uploaded_file.name
    file_size_mb = uploaded_file.size / (1024 * 1024)

    st.success("✅ Annual Report Uploaded Successfully!")

    st.subheader("📄 File Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("File Name", file_name)

    with col2:
        st.metric("File Size", f"{file_size_mb:.2f} MB")

    # ==========================================
    # Save PDF
    # ==========================================
    file_path = UPLOAD_FOLDER / file_name

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("📁 Report saved successfully!")
    st.info(f"Saved to: {file_path}")

    # ==========================================
    # Extract Text from PDF
    # ==========================================
    try:
        text, total_pages = extract_text_from_pdf(file_path)
        text = clean_text(text)
        chunks = chunk_text(text)
        with st.spinner("Creating AI Knowledge Base..."):
            vector_db = create_vector_store(chunks)

        st.success("Knowledge Base Created!")
        st.divider()
        st.metric("Knowledge Base", "Ready")
        st.subheader("📚 PDF Statistics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Pages", total_pages)

        with col2:
            st.metric("Words", f"{len(text.split()):,}")

        with col3:
            st.metric("Characters", f"{len(text):,}")

        with col4:
            st.metric("Chunks", len(chunks))
        st.divider()

        st.subheader("📄 Text Preview")

        preview = text[:2000]

        st.text_area(
            "First 2000 Characters",
            preview,
            height=350
        )
        st.divider()

        st.subheader("🧩 First AI Chunk")

        st.text_area(
            "Chunk 1",
            chunks[0],
            height=250
)
        st.divider()

        st.subheader("📋 Upload Summary")

        st.write(f"**Company Report:** {file_name}")
        st.write(f"**File Size:** {file_size_mb:.2f} MB")
        st.write(f"**Pages:** {total_pages}")
        st.write("**Status:** Ready for AI Analysis ✅")

        st.divider()

        st.subheader("🚀 Next Step")

        st.write("""
In the next lesson, we will:

- Clean the extracted text
- Split the report into chunks
- Prepare the report for RAG
- Generate embeddings
- Build a searchable knowledge base
""")

    except Exception as e:
        st.error("❌ Error reading the PDF.")
        st.exception(e)

else:
    st.info("⬆️ Please upload a PDF annual report to begin.")