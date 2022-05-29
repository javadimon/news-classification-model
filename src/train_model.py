from tensorflow.python import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout, LSTM, GRU
from keras import utils
from keras.utils import np_utils
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.callbacks import ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def train_model():
    # Максимальное количество слов
    num_words = 10000
    # Максимальная длина новости
    max_news_len = 30
    # Количество классов новостей
    nb_classes = 3

    train = pd.read_csv('train-data-source/train.csv',
                        header=None,
                        names=['class', 'title', 'text'])
    print(train)

    news = train['text']
    print(news[:5])

    y_train = np_utils.to_categorical(train['class'] - 1, nb_classes)
    print(y_train)

    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(news)
    print(tokenizer.word_index)

    sequences = tokenizer.texts_to_sequences(news)
    index = 1
    print(news[index])
    print(sequences[index])

    x_train = pad_sequences(sequences, maxlen=max_news_len)

    # Создание модели GRU
    model_gru = Sequential()
    model_gru.add(Embedding(num_words, 32, input_length=max_news_len))
    model_gru.add(GRU(16))
    model_gru.add(Dense(3, activation='softmax'))

    model_gru.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    model_gru.summary()

    model_gru_save_path = 'trained-model/best_model_gru.h5'
    checkpoint_callback_gru = ModelCheckpoint(model_gru_save_path,
                                              monitor='val_accuracy',
                                              save_best_only=True,
                                              verbose=1)
    history_gru = model_gru.fit(x_train,
                                y_train,
                                epochs=10,
                                batch_size=128,
                                validation_split=0.1,
                                callbacks=[checkpoint_callback_gru])

    plt.plot(history_gru.history['accuracy'],
             label='Доля верных ответов на обучающем наборе')
    plt.plot(history_gru.history['val_accuracy'],
             label='Доля верных ответов на проверочном наборе')
    plt.xlabel('Эпоха обучения')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()

    test = pd.read_csv('train-data-source/test.csv',
                       header=None,
                       names=['class', 'title', 'text'])
    y_test = np_utils.to_categorical(test['class'] - 1, nb_classes)
    print(y_test)

    test_sequences = tokenizer.texts_to_sequences(test['text'])
    x_test = pad_sequences(test_sequences, maxlen=max_news_len)
    model_gru.load_weights(model_gru_save_path)
    model_gru.evaluate(x_test, y_test, verbose=1)

    examples = [
        'Linux',
        'Java'
    ]
    results = tf.sigmoid(model_gru(tf.constant(examples)))
    print(results)


if __name__ == '__main__':
    train_model()
