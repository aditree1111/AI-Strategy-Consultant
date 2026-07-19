import fitz

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)

    full_text = ""
    total_pages = len(document)

    for page in document:
        full_text += page.get_text() + "\n"

    document.close()

    return full_text, total_pages