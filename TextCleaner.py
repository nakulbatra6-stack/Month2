import re

# def clean_text(text):
#     text = text.lower() # 1. Lowercasing
#     text = re.sub(r"[^\w\s]", "", text) # 2. Remove punctuation
#     #[^\w\s] #Match anything that is NOT a letter, digit, underscore, or space
#     return text

# samples = [
# "I LOVE AI!!!",
# "AI is Amazing :)",
# "Hello World!!!",
# "heLLo worLD"
# ]

# for s in samples:
#     print("Original:", s)
#     print("Cleaned :", clean_text(s))
#     print("-" * 30)


# def clean_text(text):
#     text = text.lower()
#     text = re.sub(r"[^\w\s]","",text)
#     return text

# def are_same(text1, text2):
#     return clean_text(text1) == clean_text(text2)

# print(are_same("I LOVE AI!!!", "i love ai")) # True
# print(are_same("Hello!!", "hello")) # True
# print(are_same("AI is cool", "AI is bad")) # False