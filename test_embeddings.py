from utils.embeddings import create_embeddings

chunks = [
    "Tesla manufactures electric vehicles.",
    "Apple develops iPhones and Macs."
]

embeddings = create_embeddings(chunks)

print(type(embeddings))
print(embeddings.shape)