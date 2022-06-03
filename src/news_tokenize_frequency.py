import nltk
import string
import pandas as pd
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')


# Load saved news data
def process():
    corpus = pd.read_csv('train-data-source/train.csv',
                         header=None,
                         names=['class', 'title', 'description'])
    titles = corpus['title']
    descriptions = corpus['title'] + " " + corpus['description']
    index = 0
    steams = []
    for description in descriptions:
        if index > 0:
            break
        for token in tokenize(description, steams):
            print("process: " + token)
        index += 1

    print("\nEND\nsteams: " + str(steams))
    counts = Counter(steams)
    print("\nEND\ncounts: " + str(counts))


# Tokenization function
def tokenize(text, steams):
    stem = nltk.stem.SnowballStemmer('russian')
    text = text.lower()
    stop_words = nltk.corpus.stopwords.words('russian')
    print(stop_words)

    for token in nltk.word_tokenize(text):
        if token in string.punctuation: continue
        if token in stop_words: continue
        print("tokenize: " + token)
        steams.append(stem.stem(token))
        yield stem.stem(token)


if __name__ == '__main__':
    process()
