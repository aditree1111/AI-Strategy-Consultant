import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_gemini(context, question):

    prompt = f"""
You are a Bain & Company strategy consultant.

Use only the context below.

Context:
{context}

Question:
{question}

Answer professionally using headings and bullet points.
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text