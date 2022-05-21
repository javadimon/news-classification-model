from tensorflow.python import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout, LSTM, GRU
from keras import utils
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.callbacks import ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def teach():
    train = pd.read_csv('train.csv',
                        header=None,
                        names=['class', 'title', 'text'])
    print(train)


if __name__ == '__main__':
    print("NEWS")
    teach()