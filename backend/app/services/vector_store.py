from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)

def add_texts(texts):
    embeddings = model.encode(texts)
    index.add(np.array(embeddings))

def search(query, k=3):
    q_emb = model.encode([query])
    _, indices = index.search(np.array(q_emb), k)
    return indices.tolist()
