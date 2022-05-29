import pandas as pd
from keras.utils import np_utils
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Embedding, GRU


def recognize():
    print("Recognizing news...")

    # Максимальное количество слов
    num_words = 10000
    # Максимальная длина новости
    max_news_len = 30
    # Количество классов новостей
    nb_classes = 3

    model_gru_save_path = 'trained-model/best_model_gru.h5'

    tokenizer = Tokenizer(num_words=num_words)

    # Создание модели GRU
    model_gru = Sequential()
    model_gru.add(Embedding(num_words, 32, input_length=max_news_len))
    model_gru.add(GRU(16))
    model_gru.add(Dense(3, activation='softmax'))

    model_gru.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    news = pd.read_csv('train-data-source/real_news.csv',
                       header=None,
                       names=['class', 'title', 'text'])
    print(news[:5])

    y_news = np_utils.to_categorical(news['class'] - 1, nb_classes)
    print(y_news)

    news_sequences = tokenizer.texts_to_sequences(news['text'])
    x_news = pad_sequences(news_sequences, maxlen=max_news_len)
    model_gru.load_weights(model_gru_save_path)
    model_gru.evaluate(x_news, y_news, verbose=1)


if __name__ == '__main__':
    recognize()
