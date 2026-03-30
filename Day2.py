import nltk
import spacy
nltk.download('punkt_tab') 
nltk.download('stopwords')


from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

text = "AI is amazing. You should learn it today!"
# Sentence tokenization
# print(sent_tokenize(text))#['AI is amazing.', 'You should learn it today!']
# Word tokenization
# print(word_tokenize(text))#['AI', 'is', 'amazing', '.', 'You', 'should', 'learn', 'it', 'today', '!']
words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
# print(stop_words)
filtered = [w for w in words if w.lower() not in stop_words]
print(filtered) #['AI', 'amazing', '.', 'learn', 'today', '!']


#STEMMING:
stemmer = PorterStemmer()
for w in words:
    print(w, "->", stemmer.stem(w))

#Lemmatization:Convert words to meaningful base form
lemmatizer = WordNetLemmatizer()

# words = ["running", "better", "feet"]

for w in words:
    print(w, "->", lemmatizer.lemmatize(w))


nlp = spacy.load("en_core_web_sm")
text = "The children are playing and running better than before"
doc = nlp(text)

for token in doc:
    print(token.text, "->", token.lemma_)