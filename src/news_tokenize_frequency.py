from datetime import datetime

import nltk
import string
import pandas as pd
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
snowball_stemmer = nltk.stem.SnowballStemmer('russian')
stop_words = nltk.corpus.stopwords.words('russian')


class NewsTokenizer:
    def __init__(self, news_class_name, counter):
        self.news_class_name = news_class_name
        self.counter = counter


# Load saved news data
def news_data_handler(file_name):
    corpus = pd.read_csv(file_name,
                         header=None,
                         names=['class', 'title', 'description'])
    steams = []
    tokenizers = []
    index = 0
    classes = corpus['class']
    news_all = corpus['title'] + " " + corpus['description']

    for news in news_all:
        for token in tokenize(news, steams):
            pass

        counter = Counter(steams)
        tokenizers.append(NewsTokenizer(classes[index], counter))
        steams.clear()
    return tokenizers


# Tokenization function
def tokenize(text, steams):
    text = text.lower()

    for token in nltk.word_tokenize(text):
        if token in string.punctuation:
            continue
        if token in stop_words:
            continue
        steams.append(snowball_stemmer.stem(token))
        yield snowball_stemmer.stem(token)


def recognize_news(tokenized_news, file_name):
    print("Recognizing news...")
    real_news_tokenizers = news_data_handler(file_name)
    print("News tokenizers items : " + str(real_news_tokenizers[0].counter.items()))
    # for tn in tokenized_news:
    #     for rne in real_news_tokenizers[0].counter.items():
    #         for tni in tn.counter.items():
    #             print("DEBUG: " + tni[0] + " " + rne[0])
    #             if tni[0] == rne[0]:
    #                 print("YES!")

    # for item in real_news_tokenizers[0].counter.items():
    #     print("Item: " + item[0] + ": " + str(item[1]))


if __name__ == '__main__':
    news_data_tokenizers = news_data_handler('train-data-source/train.csv')
    recognize_news(news_data_tokenizers, 'train-data-source/real_news.csv')
