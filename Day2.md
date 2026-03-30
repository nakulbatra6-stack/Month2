command 1: pip install nltk spacy
NLTK (Natural Language Toolkit)


Beginner-friendly NLP library
Used for:
Tokenization (breaking text into words)
Stopwords removal
Stemming / Lemmatization

spaCy
Fast & production-ready NLP library
Used in real-world applications
Supports:
Named Entity Recognition (NER)
POS tagging
Dependency parsing


command 2: python -m spacy download en_core_web_sm

downloads a language model for spaCy.

Pre-trained English NLP model
Contains:
Vocabulary
Grammar rules
Statistical patterns

Without this → spaCy won’t understand text

AI models don’t read text like humans

They:

Break text → tokens
Convert tokens → numbers
Process numbers → predictions

Raw text = Paragraph in a book 📖
Tokens = Words separated on paper ✂️
Numbers = Language AI understands 🔢


1)Tokenization #from nltk.tokenize import word_tokenize, sent_tokenize
2)Remove Stopwards#from nltk.corpus import stopwords #Remove useless words like is, the, and
🔑 Simple Rule to Remember

👉 Remove stopwords when:
You are doing traditional ML (TF-IDF, BoW)Bag of Words (BoW) and (Term Frequency-Inverse Document Frequency)
You want speed + simplicity

👉 Don’t remove when:
Meaning depends on context
You're using modern NLP (BERT, embeddings, LLMs)

3)STEMMING: from nltk.stem import PorterStemmer
4)Lemmatization:Convert words to meaningful base form majorly used from spacy