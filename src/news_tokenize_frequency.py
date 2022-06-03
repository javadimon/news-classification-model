import nltk
import string
import pandas as pd
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')


# Load saved news data
def process():
    corpus = pd.read_csv('train-data-source/train.csv',
                         header=None,
                         names=['class', 'title', 'description'])
    titles = corpus['title']
    descriptions = corpus['description']
    index = 0
    for description in descriptions:
        if index > 0:
            break
        for token in tokenize(description):
            print("process: " + token)
        index += 1


# Tokenization function
def tokenize(text):
    stem = nltk.stem.SnowballStemmer('russian')
    text = text.lower()
    stop_words = nltk.corpus.stopwords.words('russian')
    print(stop_words)

    for token in nltk.word_tokenize(text):
        if token in string.punctuation: continue
        if token in stop_words: continue
        print("tokenize: " + token)
        yield stem.stem(token)


if __name__ == '__main__':
    process()
