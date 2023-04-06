import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
text = open("data.txt").read()
print(text)
def tokenize_text():
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words
    words = [word_tokenize(sentence) for sentence in sentences]

    # Return the tokenized text
    return sentences, words