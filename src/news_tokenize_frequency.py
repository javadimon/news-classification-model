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
    tokenizers = []
    steams = []
    classes = corpus['class']
    news_all = corpus['title'] + " " + corpus['description']

    index = 0
    for news in news_all:
        for token in tokenize(news, steams):
            pass

        counter = Counter(steams)
        tokenizers.append(NewsTokenizer(classes[index], counter))
        steams.clear()
        index += 1

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

    category_counter = {}
    for rnt in real_news_tokenizers:
        real_news_class = rnt.news_class_name
        for tn in tokenized_news:
            news_class = tn.news_class_name
            for rnt_item in rnt.counter.items():
                for tn_item in tn.counter.items():
                    if rnt_item[0] == tn_item[0] and rnt_item[1] > 1 and tn_item[1] > 1:
                        category_counter[news_class] = category_counter.get(news_class, 0) + 1
        print(real_news_class)
        print(category_counter)
        print("\n")
        category_counter = {}


if __name__ == '__main__':
    news_data_tokenizers = news_data_handler('train-data-source/train.csv')
    recognize_news(news_data_tokenizers, 'train-data-source/real_news.csv')
