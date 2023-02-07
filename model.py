import keras
from keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from keras.callbacks import ModelCheckpoint
import regex as re
import numpy as np

from keras.utils import np_utils
import pickle


df = pd.read_csv('../raw_data/pink_floyd_lyrics.csv')


tokenizer = Tokenizer(char_level=False)
tokenizer.fit_on_texts([df.lyrics.iloc[1].replace('\n',' \n ')])
tokenizer.word_index

text = df.lyrics.iloc[1].split('\n')
text = [re.sub(r'\d+', '', i) for i in text]
corpus = list(set(text))
