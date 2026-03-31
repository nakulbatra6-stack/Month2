#pip install sentence-transformers
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')#Load a brain that understands language

# Convert text → embeddings
sentences = ["king", "queen", "man", "woman"]

embeddings = model.encode(sentences)

# Print embeddings
for word, emb in zip(sentences, embeddings):
    print(word, emb[:5])  # first 5 numbers


sim = cosine_similarity([embeddings[0]], [embeddings[1]])
print("Similarity between king & queen:", sim[0][0])

print("king vs queen:", cosine_similarity([embeddings[0]], [embeddings[1]])[0][0])
print("king vs man:", cosine_similarity([embeddings[0]], [embeddings[2]])[0][0])
print("king vs woman:", cosine_similarity([embeddings[0]], [embeddings[3]])[0][0])