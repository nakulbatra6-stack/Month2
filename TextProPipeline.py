import re
import nltk
import spacy
nltk.download('punkt_tab')
nlp = spacy.load("en_core_web_sm")


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')


def preprocess(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words] #list comprehension to remove stop words
    #Use SpaCy for correct lemmatization, here nlp takes string and returns a doc object which contains tokens and their lemmas.
    doc = nlp(" ".join(tokens))
    tokens = [token.lemma_ for token in doc]
    return tokens

text = "AI is transforming the world! Machines are learning faster."
print(preprocess(text))


#expected output 
#['ai', 'transform', 'world', 'machine', 'learn', 'fast']