import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')
# nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
text = open("data.txt").read()


def tokenize_text():
    sentences = sent_tokenize(text)
    print('sentences::', sentences)
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))

    print('words:::::', words)
    words = [word.lower() for word in words]

    print(words)
    # punctuation remove
    words = [word for word in words if word not in string.punctuation]

    print('punctuation::', words)
    # Stop word remove
    words = [word for word in words if word not in stop_words]

    print('stop_words::', words)

    stemmer = PorterStemmer()

    stemmed_words = [stemmer.stem(word) for word in words]

    print('stemmed_words::', stemmed_words)

    legitimatize = WordNetLemmatizer()

    lemmatized_words = [legitimatize.lemmatize(word) for word in words]

    print('lemmatized_words::', lemmatized_words)
