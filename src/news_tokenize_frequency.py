import string
from collections import Counter
import nltk
import pandas as pd
from train_model_store import NewsTokenizer
import train_model_store

nltk.download('punkt')
nltk.download('stopwords')
snowball_stemmer = nltk.stem.SnowballStemmer('russian')
stop_words = nltk.corpus.stopwords.words('russian')


# Load saved news data
def news_data_handler(file_name):
    corpus = pd.read_csv(file_name,
                         header=None,
                         names=['class', 'title', 'description'])
    tf_model = []
    steams = []
    all_classes = corpus['class']
    all_news = corpus['title'] + " " + corpus['description']

    index = 0
    for news in all_news:
        for token in tokenize(news, steams):
            pass

        counter = Counter(steams)

        optimized_counter_array = []
        for c in counter.items():
            if c[1] == 1:
                continue
            else:
                optimized_counter_array.append(c)

        optimized_counter = dict(optimized_counter_array)

        tf_model.append(NewsTokenizer(all_classes[index], optimized_counter))
        steams.clear()
        index += 1

    return tf_model


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


def save_model(data):
    train_model_store.save(data, "trained-model/news_tokenize_frequency.json")


def load_model():
    return train_model_store.load("trained-model/news_tokenize_frequency.json")


def recognize_test_news(news_tf_model, file_name):
    print("Recognizing news...")
    real_news_tf_model = news_data_handler(file_name)

    positive_counter = 0
    negative_counter = 0
    test_news_count = 0
    category_counter = {}
    for rnt in real_news_tf_model:
        real_news_class = rnt.news_class_name
        for tn in news_tf_model:
            news_class = tn.news_class_name
            for rnt_item in rnt.counter.items():
                for tn_item in tn.counter.items():
                    if rnt_item[0] == tn_item[0]:
                        category_counter[news_class] = category_counter.get(news_class, 0) + 1

        max_count = -1
        max_category = ""
        for key in category_counter.keys():
            if category_counter[key] > max_count:
                max_count = category_counter[key]
                max_category = key

        print(str(real_news_class) + " - " + max_category + " - " + str(real_news_class == str(max_category)))

        if str(real_news_class) == str(max_category):
            positive_counter += 1
        else:
            negative_counter += 1

        category_counter = {}
        test_news_count += 1

    print("=======================\nAccuracy:" + str(positive_counter / test_news_count))


if __name__ == '__main__':
    # news_data_tokenizers = news_data_handler('train-data-source/train.csv')
    # save_model(news_data_tokenizers)
    t = load_model()
    recognize_test_news(t, 'train-data-source/test.csv')
