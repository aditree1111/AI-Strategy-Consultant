# 📊 AI Strategy Consultant

An AI-powered strategy consulting application that analyzes public company annual reports using **Retrieval-Augmented Generation (RAG)** and **Google Gemini**. Users can upload a company's annual report and receive AI-generated strategic insights, including SWOT analysis, business risks, growth opportunities, and recommendations.

---

## 🚀 Features

- 📄 Upload annual report PDFs
- 📝 Automatic text extraction and preprocessing
- ✂️ Semantic text chunking
- 🧠 Vector embeddings using Sentence Transformers
- 🗄️ ChromaDB vector database for semantic search
- 💬 Ask natural language questions about the company
- 🏢 Generate Company Overview
- 📈 SWOT Analysis
- ⚠️ Business Risk Assessment
- 🌱 Growth Opportunity Identification
- 🎯 Strategic Recommendations

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- ChromaDB
- Sentence Transformers
- PyMuPDF (fitz)
- Retrieval-Augmented Generation (RAG)

---

## 🏗️ Project Workflow

```text
Upload Annual Report (PDF)
          │
          ▼
Extract Text (PyMuPDF)
          │
          ▼
Clean & Chunk Text
          │
          ▼
Generate Embeddings
          │
          ▼
Store in ChromaDB
          │
          ▼
Semantic Search
          │
          ▼
Gemini LLM
          │
          ▼
Strategic Business Insights
```

---

## 📸 Key Capabilities

- Company Overview
- Interactive Q&A on Annual Reports
- SWOT Analysis
- Business Risk Analysis
- Growth Opportunity Analysis
- Strategic Recommendations

---

## 📂 Project Structure

```
AI-Strategy-Consultant/
│
├── app.py
├── requirements.txt
├── README.md
├── uploads/
│
└── utils/
    ├── pdf_reader.py
    ├── text_processing.py
    ├── embeddings.py
    ├── vector_store.py
    └── gemini.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aditree1111/AI-Strategy-Consultant.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 Example Questions

- What does this company do?
- What are the company's biggest business risks?
- Summarize the business model.
- What are the major growth opportunities?
- Generate a SWOT analysis.
- Recommend strategic initiatives.

---

## 🔮 Future Improvements

- Export AI-generated reports as PDF
- Interactive financial dashboards
- Multi-document analysis
- Financial ratio visualization
- Cloud deployment
- Conversation history
- Support for additional LLM providers

---

## 👤 Author

**Aditree Bajpai**

GitHub: https://github.com/aditree1111

---
