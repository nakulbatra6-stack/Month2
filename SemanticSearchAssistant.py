import  re
import nltk
import numpy as np
import spacy    
from nltk.stem import PorterStemmer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer('all-MiniLM-L6-v2')#Load a brain that understands language

nlp = spacy.load("en_core_web_sm")
nltk.download('punkt_tab')
nltk.download('stopwords')
stemmer = PorterStemmer()

data = [
    "I love machine learning",
    "AI is fascinating",
    "I enjoy playing football",
    "Deep learning is powerful"
]

sen = input("Enter Sentence ")
print(sen)

# Preprocess the input sentence
def preprocess(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = nltk.sent_tokenize(text)  # Tokenize the sentence
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  # Remove stop words
    tokens = [stemmer.stem(word) for word in tokens]  # Apply stemming
    text = " ".join(tokens)  # Join tokens back to a string 
    doc = nlp(text)
    return tokens

# Preprocess the input sentence and the data
preprocessed_sen = preprocess(sen)
print("Preprocessed Sentence:", preprocessed_sen)
embeddings = model.encode(preprocessed_sen)

for word,emb in zip(preprocessed_sen, embeddings):
    print(word, emb[:2])  # first 5 numbers

for d in data:
    preprocessed_d = preprocess(d)
    print("Preprocessed Data:", preprocessed_d)
    d_embeddings = model.encode(preprocessed_d)
    sim = cosine_similarity([embeddings[0]], [d_embeddings[0]])
    # print("Similarity:", sim[0][0])
    ranked_indices = np.argsort(sim)[::-1]

    print(f"Similarity between '{sen}' and '{d}': {sim[0][0]}")
