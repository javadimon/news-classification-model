from datetime import datetime

import nltk
import string
import pandas as pd
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')


class NewsTokenizer:
    def __init__(self, news_class_name, counter):
        self.news_class_name = news_class_name
        self.counter = counter


# Load saved news data
def news_data_handler():
    corpus = pd.read_csv('train-data-source/train.csv',
                         header=None,
                         names=['class', 'title', 'description'])
    steams = []
    news_tokenizers = []
    index = 0
    classes = corpus['class']
    news_all = corpus['title'] + " " + corpus['description']

    for news in news_all:
        # if classes[index] != 1:
        #     break
        for token in tokenize(news, steams):
            pass

        count = Counter(steams)
        news_tokenizers.append(NewsTokenizer(classes[index], count))
        steams.clear()
        # print(news_tokenizers[0].news_class_name)
        # print(str(news_tokenizers[0].counter))
        # print("\n")
    return news_tokenizers


# Tokenization function
def tokenize(text, steams):
    stem = nltk.stem.SnowballStemmer('russian')
    text = text.lower()
    stop_words = nltk.corpus.stopwords.words('russian')

    for token in nltk.word_tokenize(text):
        if token in string.punctuation:
            continue
        if token in stop_words:
            continue
        # print("tokenize: " + token)
        steams.append(stem.stem(token))
        yield stem.stem(token)


def recognize_news(tokenized_news):
    print("Recognizing news...")


if __name__ == '__main__':
    print(datetime.now())
    news_tokenizers = news_data_handler()
    print(len(news_tokenizers))
    recognize_news(news_tokenizers)
    print(datetime.now())
