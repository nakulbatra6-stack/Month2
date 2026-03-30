pip install nltk spacy
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


python -m spacy download en_core_web_sm

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