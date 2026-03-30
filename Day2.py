import nltk
nltk.download('punkt_tab') 

from nltk.tokenize import word_tokenize, sent_tokenize

text = "AI is amazing. You should learn it today!"

# Sentence tokenization
print(sent_tokenize(text))#['AI is amazing.', 'You should learn it today!']

# Word tokenization
print(word_tokenize(text))#['AI', 'is', 'amazing', '.', 'You', 'should', 'learn', 'it', 'today', '!']
print(text.split())#['AI', 'is', 'amazing.', 'You', 'should', 'learn', 'it', 'today!']
