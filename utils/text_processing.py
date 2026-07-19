import re


def clean_text(text):
    """
    Clean extracted PDF text.
    """

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove extra blank lines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def chunk_text(text, chunk_size=1000):
    """
    Split text into chunks of approximately
    chunk_size characters.
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size

    return chunks